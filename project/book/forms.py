from django import forms
from .models import readingList

class ReadingForm(forms.ModelForm):
    class Meta:
        model= readingList
        fields=["title","report","img"]