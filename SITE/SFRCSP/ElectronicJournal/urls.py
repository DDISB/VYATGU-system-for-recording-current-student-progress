from django.contrib.auth import views
from django.urls import path, re_path

from . import views

urlpatterns = [
  path('test', views.TableTestingDef),
  path('journal', views.JournalDef, name='Journal'),
  path('', views.MainPageDef, name='mainPage'),
]