from django import forms

class TranslationForm(forms.Form):
    number_question = forms.CharField()
    author          = forms.CharField(max_length=100)
    translation     = forms.CharField(widget = forms.Textarea)