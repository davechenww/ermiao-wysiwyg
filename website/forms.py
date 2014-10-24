# -*- coding: utf-8 -*-
from django import forms


class TextForm(forms.Form):
    title = forms.CharField(max_length=50)
    text = forms.CharField()
    cover = forms.CharField(required=False)
