# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.views.generic import View

from pymongo.objectid import ObjectId

from forms import TextForm

import models
import utils

class Index(View):

    def get(self, request, *args, **kwargs):
        return render_to_response('index.html', {}, RequestContext(request))

    def post(self, request, *args, **kwargs):
        form = TextForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            title = cd.get('title')
            text = cd.get('text')
            image_list = utils.get_image(text)
            doc = {'title':title, 'text':text}
            text_id = str(models.insert(doc))
            return HttpResponseRedirect(reverse('views.detail', kwargs={'text_id': text_id}))
        text = u""
        if not form['text'].errors:
            text = form['text'].value 
        return render_to_response('index.html', {'text':text}, RequestContext(request))

def detail(request, text_id):
    text_id = ObjectId(text_id)
    text = models.get_text(text_id)
    return render_to_response('detail.html', {'text':text})
