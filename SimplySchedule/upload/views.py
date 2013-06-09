from django.shortcuts import render
from upload.forms import upload_form
from django.http import HttpResponse, HttpResponseRedirect 
from django.conf import settings
from upload.assignworkshops import initialiseAndRunScheduler

import csv
import os.path
BASE = os.path.dirname(os.path.abspath(__file__))

def getFileUrlPath(filename):
    return settings.MEDIA_URL + filename

def getFileServerPath(filename):
    return settings.MEDIA_ROOT + "/" + filename

def upload_view(request):
    if request.method == 'POST':
        form = upload_form(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            filename = handle_uploaded_file(request.FILES['file'])
            try:
                nWorkshops, nSessions, workshopNames, conferenceName = read_form_values(cd)
                useMetadata = False
            except:
                nWorkshops = None
                nSessions = None
                workshopNames = None
                useMetadata = True
            dataLines, resultFilename, resultLines = run_scheduler(filename, nSessions, workshopNames, useMetadata)
            resultFullPath = getFileUrlPath(resultFilename)
            return render(request,'thanks.html', 
                {'formdata': cd, 'file': dataLines, 'result': resultLines, 'request': request, 'schedulefile':resultFullPath, 'name':conferenceName})
    else:
        form = upload_form(
            initial={'subject': 'I love your site!'}
      )
    return render(request, 'upload_form.html', {'form': form})  

def sample_view(request):
    filename = 'SampleData2.csv'
    dataLines, resultFilename, resultLines = run_scheduler(filename, None, None, True)
    resultFullPath = getFileUrlPath(resultFilename)
    return render(request,'thanks.html', {'file': dataLines, 'result': resultLines, 'request': request, 'schedulefile':resultFullPath, 'name':"Sample Conference"})

def file_to_response(filename):
    response = HttpResponse(mimetype="application/ms-excel")
    response['Content-Disposition'] = 'attachment; filename=%s' % filename
    return response

def file_server_view(request, requested_file):
    return file_to_response(requested_file)

def run_scheduler(filename, in_nSessions, in_workshopNames, useMetadata):
    dataLines = []
    uploadReader = csv.reader(open(getFileServerPath(filename), 'r'), delimiter=',', quotechar='|')
    for line in uploadReader:
        dataLines.append(line)

    resultFilename = initialiseAndRunScheduler(filename, in_nSessions, in_workshopNames, useMetadata)
    resultLines = []
    resultReader = csv.reader(open(getFileServerPath(resultFilename), 'r'), delimiter=',', quotechar='|')
    for line in resultReader:
        resultLines.append(line)

    return dataLines, resultFilename, resultLines

def handle_uploaded_file(f):
    if (f == None):
        return 'SampleData2.csv'
    tempLocation = 'uploadedFile.csv'
    destination = open(getFileServerPath(tempLocation), 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    return tempLocation

def read_form_values(cd):
    nWorkshops = int(cd['nWorkshops'])
    nSessions = int(cd['nSessions'])
    conferenceName = cd['conferenceName']
    workshopNames = cd['workshopNames'].split(',')
    if len(workshopNames) <> nWorkshops:
        raise Exception, ('Number of workshops %i did not match the number of workshop names given %i: %s', 
            nWorkshops, len(workshopNames), workshopNames)
    return nWorkshops, nSessions, workshopNames, conferenceName
