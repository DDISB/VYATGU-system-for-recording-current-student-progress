from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Active)
admin.site.register(Groupa)
admin.site.register(Pair)
admin.site.register(Pairactiv)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(Typeactive)
admin.site.register(Typesubject)
admin.site.register(CustomUser)