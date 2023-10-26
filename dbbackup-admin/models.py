from django.db import models
from solo.models import SingletonModel
import json
from django.core.management import call_command
from django.db import connections


class Backup(SingletonModel):

    updated_date = models.DateTimeField(auto_now=True)
    message = models.TextField(default="Press Save Button To Backup Database",null=True)
    number_of_backups = models.IntegerField(null=True,blank=True)
    def  save(self, *args,**kwargs):
        try:
            call_command("dbbackup", interactive=False)
            connections["default"]=connections.create_connection("default")
            self.message="Press Save Button To Backup Database"
            self.number_of_backups += 1
            super(Backup, self).save(*args,**kwargs)
        except Exception as e:
            self.message=json.dumps(e.args)
            super(Backup, self).save(*args,**kwargs)
            
    def __str__(self) :
        return "Backup from database"

    class Meta:
          verbose_name =  "Backup Database"
