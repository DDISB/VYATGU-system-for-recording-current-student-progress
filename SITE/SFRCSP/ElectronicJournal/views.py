# from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import *

# Функция представления для главной страницы
def MainPageDef(request):
  if (request.user.is_authenticated):
    return redirect('Journal')
  else:
    return redirect('authentication:login')

# #Тестовая функция
# def TableTestingDef(request):
#   if (request.user.is_authenticated):
#     return redirect('authentication:login', permanent=True)
#   students = Student.objects.all()
#   #Список передаваемых атрибутов в шаблон
#   attrList = {
#     'title' : 'Test Page',
#     'students' : students,
#   }
#   return render(request, 'ElectronicJournal\TableTestingTemplate.html', attrList)

def JournalDef(request):
  
  if (not request.user.is_authenticated):
    return redirect('authentication:login')
  
  current_user = request.user
  if (current_user.is_staff == 0):
    current_student = Student.objects.get(user_id=current_user.id)
    
  # student = Student.objects.all()
  attrList = {
    'title' : 'Журнал',
    'student' : current_student
  }
  return render(request, "ElectronicJournal/student Journal.html", attrList)