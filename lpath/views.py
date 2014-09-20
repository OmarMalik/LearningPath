from django.template import RequestContext
from django.shortcuts import render_to_response, render
from lpath.models import Topic

def index(request):
    context = RequestContext(request)
    return render_to_response('lpath/index.html', context)


def browse(request):
    topics = Topic.objects.all().order_by('name')
    context = {'topics': topics}
    return render(request, 'lpath/browse.html', context)