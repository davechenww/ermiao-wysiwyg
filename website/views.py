# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from django.conf import settings

from forms import TextForm
from models import Entry


class Index(View):

    def get(self, request, *args, **kwargs):
        p = request.GET.get('p', 0)
        try:
            p = int(p)
        except ValueError:
            p = 0
        if p < 1:
            p = 1
        entries = Entry.get_list(page=p-1)
        return render_to_response('index.html', {
            'entries': entries,
        }, RequestContext(request))


class Create(View):

    def get(self, request, *args, **kwargs):
        form = TextForm()
        return render_to_response('create.html', {
            'form': form,
        }, RequestContext(request))

    def post(self, request, *args, **kwargs):
        form = TextForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            title = cd.get('title')
            text = cd.get('text')
            cover = cd.get('cover', '')
            entry = Entry.create(title, text, cover)
            return HttpResponseRedirect(
                reverse('detail', kwargs={'_id': str(entry.id)}))
        return render_to_response('create.html', {
            'form': form,
        }, RequestContext(request))


class Detail(View):

    def get(self, request, _id, *args, **kwargs):
        entry = Entry.get(_id)
        if not entry:
            raise Http404
        return render_to_response('detail.html', {
            'entry': entry,
        }, RequestContext(request))


class Upload(View):

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        return super(Upload, self).dispatch(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        image = request.FILES['file']
        url = self.save(image)
        return HttpResponse(url)

    def save(self, uploadfile):
        import os.path, uuid
        ext = os.path.splitext(uploadfile.name)[1]
        filename = os.path.join('uploads', '%s%s' % (uuid.uuid4().hex, ext))

        uri = os.path.join(settings.MEDIA_ROOT, filename)
        with open(uri, 'wb+') as dest:
            for chunk in uploadfile.chunks():
                dest.write(chunk)

        from urlparse import urljoin
        return urljoin(settings.MEDIA_URL, filename)
