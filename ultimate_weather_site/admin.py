from django.contrib import admin
from .models import *
# Register your models here.

class TemperaturesInLine(admin.TabularInline):
    model = Temperatures


class ServiceAdmin(admin.ModelAdmin):
    inlines = [TemperaturesInLine]


admin.site.register(Service,ServiceAdmin)