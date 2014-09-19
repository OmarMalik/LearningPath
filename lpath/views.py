from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request):
    context = RequestContext(request)
    return render_to_response('lpath/index.html', context)

def browse(request):
    context = RequestContext(request)
    return render_to_response('lpath/browse.html', context)