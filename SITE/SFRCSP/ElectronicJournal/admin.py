from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Groupa)
class ActiveAdmin(admin.ModelAdmin):
  list_display = ('nam', 'course', 'groupid')
  list_display_links = ('course', 'nam')
  ordering = ['course', 'nam']

admin.site.register(Active)
# admin.site.register(Groupa)
admin.site.register(Pair)
admin.site.register(Pairactive)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Typeactive)
admin.site.register(Typesubject)

admin.site.site_header = "Панель администрирования"