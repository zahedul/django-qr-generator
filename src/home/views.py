from django.shortcuts import render
from django.http import HttpResponse


import logging
logger = logging.getLogger('baseapp')

def index(request):
    context = {'content': "I am the content"}
    return render(request, 'home/index.html', context)