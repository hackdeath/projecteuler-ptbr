from django import forms

class TranslationForm(forms.Form):
    author          = forms.CharField(max_length=100)
    name            = forms.CharField(max_length=100)
    translation     = forms.CharField(widget = forms.Textarea)
