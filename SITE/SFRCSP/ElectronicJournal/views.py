from django.http import HttpResponse
from django.shortcuts import render
from .models import *

# Функция представления для главной страницы
def MainPageDef(request):

  attrList = {
    'title' : 'Главная страница',
  }
  return render(request, 'ElectronicJournal\mainPageTemplate.html', attrList)

#Тестовая функция
def TableTestingDef(request):

  #Список передаваемых атрибутов в шаблон
  attrList = {
    'title' : 'Test Page',
  }
  return render(request, 'ElectronicJournal\TableTestingTemplate.html', attrList)