from django import forms

from models import Picture

class PhotoUploadForm(forms.Form):
    #Keep name to 'file' because that's what Dropzone is using
    file = forms.ImageField(required=True)

