from django.urls import path, re_path

from .views import *

urlpatterns = [
  path('', MainPageDef, name='mainPage'),
  path('test', TableTestingDef),
]