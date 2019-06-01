from django.contrib import admin
from .models import Senadores, Governadores
# Register your models here.

admin.site.register(Senadores)
admin.site.register(Governadores)