from django import forms

class upload_form(forms.Form):
    #subject = forms.CharField(max_length=100,min_length=3)
    #email = forms.EmailField(required=False, label='Your email address')
    #message = forms.CharField(widget=forms.Textarea)
    conferenceName = forms.CharField(label = "Conference title")
    nSessions = forms.CharField(required=False, label = 'Number of session times')
    nWorkshops = forms.CharField(required=False, label = 'Number of workshop options')
    workshopNames = forms.CharField(required=False, label = 'Workshop names, separated by commas')
    file  = forms.FileField()


    def clean_message(self):
    	message = self.cleaned_data['message']
    	num_words = len(message.split())
    	if num_words < 4:
    		raise forms.ValidationError('not enough words :(')
    	return message