from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Create your views here.
def testDef(request):
  studid = Student.objects.get(personid = 1)
  return render(request, 'ElectronicJournal/index.html', {'testvar' : studid.lastname,})