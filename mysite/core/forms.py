from django import forms
from django.db.models import fields
from django.forms.fields import FileField

from .models import File

class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('filegroup','filenum','protocoll','hostname','json')
        