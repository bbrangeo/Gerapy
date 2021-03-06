from django.contrib import admin

# Register your models here.
from gerapy.server.core.models import Client, Project


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'ip', 'port', 'created_at', 'updated_at')


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'built_at', 'created_at', 'updated_at')


admin.site.register(Client, ClientAdmin)
admin.site.register(Project, ProjectAdmin)
