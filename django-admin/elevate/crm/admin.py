from django.contrib import admin

# Register your models here.

from . models import Employee

from import_export.admin import ImportExportModelAdmin

admin.site.register(Employee, ImportExportModelAdmin)