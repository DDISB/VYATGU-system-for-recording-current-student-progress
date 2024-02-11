from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def testDef(request):
  return HttpResponse('Test message')