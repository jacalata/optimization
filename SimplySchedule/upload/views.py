from django.shortcuts import render
from upload.forms import upload_form
from django.http import HttpResponseRedirect 
from upload.assignworkshops import runScheduler
import csv

def upload(request):
    if request.method == 'POST':
        form = upload_form(request.POST, request.FILES)
        if form.is_valid():
            cd = form.cleaned_data
            filename = handle_uploaded_file(request.FILES['file'])
            dataLines, resultFilename, resultLines = run_scheduler(filename)
            return render(request,'thanks.html', {'file': dataLines, 'result': resultLines})
    else:
        form = upload_form(
            initial={'subject': 'I love your site!'}
      )
    return render(request, 'upload_form.html', {'form': form})  

def sample_view(request):
    filename = 'SampleData2.csv'
    dataLines, resultFilename, resultLines = run_scheduler(filename)
    return render(request,'thanks.html', {'file': dataLines, 'result': resultLines})


def upload_thanks(request):
    return render(request, 'thanks.html')

def run_scheduler(filename):
    dataLines = []
    uploadedData = open(filename, 'r').read()
    uploadReader = csv.reader(open(filename, 'r'), delimiter=',', quotechar='|')
    for line in uploadReader:
        dataLines.append(line)

    resultFilename = runScheduler(filename)
    result = open(resultFilename, 'r').read()
    resultLines = []
    resultReader = csv.reader(open(resultFilename, 'r'), delimiter=' ', quotechar='|')
    for line in resultReader:
        resultLines.append(line)

    return dataLines, resultFilename, resultLines

def handle_uploaded_file(f):
    if (f == None):
        return 'SampleData2.csv'
    tempLocation = 'uploadedFile.csv'
    destination = open(tempLocation, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    return tempLocation

