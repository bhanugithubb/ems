from django.contrib import admin

# Register your models here.
from pollapp.models import *

admin.site.register(Question)
admin.site.register(Choice)

admin.site.register(Answer)
