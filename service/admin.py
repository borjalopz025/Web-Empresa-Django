from django.contrib import admin
from .models import Service

# Register your models here.
class projectSercice(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Service, projectSercice)