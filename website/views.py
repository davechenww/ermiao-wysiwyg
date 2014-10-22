# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import View


class Index(View):

    def get(self, request, *args, **kwargs):
        return render_to_response('index.html', {}, RequestContext(request))

    def post(self, request, *args, **kwargs):
        print request.POST
        return render_to_response('index.html', {}, RequestContext(request))
