from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def blog_me(request):
    return HttpResponse("Hello Blog!")
# Create your views here.
