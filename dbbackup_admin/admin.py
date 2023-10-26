from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import Backup

@admin.register(Backup)
class BackupAdmin(SingletonModelAdmin):
    readonly_fields = ("message","updated_date","number_of_backups")

