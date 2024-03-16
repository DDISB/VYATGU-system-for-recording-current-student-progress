from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *

# Функция представления для главной страницы
def MainPageDef(request):
  if (request.user.is_authenticated):
    return HttpResponseRedirect(reverse('Journal'))
  else:
    return HttpResponseRedirect(reverse('authentication:login'))

#Тестовая функция
def TableTestingDef(request):
  if (request.user.is_authenticated):
    return HttpResponseRedirect(reverse('authentication:login'))
  students = Student.objects.all()
  #Список передаваемых атрибутов в шаблон
  attrList = {
    'title' : 'Test Page',
    'students' : students,
  }
  return render(request, 'ElectronicJournal\TableTestingTemplate.html', attrList)

def JournalDef(request):
  if (not request.user.is_authenticated):
    return HttpResponseRedirect(reverse('authentication:login'))
  students = Student.objects.all()
  attrList = {
    'title' : 'Test Page',
    'students' : students,
  }
  return render(request, 'ElectronicJournal\TableTestingTemplate.html', attrList)