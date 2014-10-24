# -*- coding: utf-8 -*-
from django import forms

class TextForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.CharField(min_length=2, 
        error_messages={'min_length':u'这项要填哦!!'} ) 
    main_image = forms.CharField(required=False)
