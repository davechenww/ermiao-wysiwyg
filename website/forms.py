from django import forms

class TextForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.CharField() 
