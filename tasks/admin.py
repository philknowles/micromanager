from django.contrib import admin
from import_export import resources, fields

# Third Party
from import_export.admin import ImportExportModelAdmin

# App
from .models import Task


# Register your models here.
class TaskResource(resources.ModelResource):
    class Meta:
        model = Task


class TaskAdmin(ImportExportModelAdmin):
    resource_class = TaskResource


admin.site.register(Task, TaskAdmin)

