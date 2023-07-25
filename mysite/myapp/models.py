from django.db import models
from datetime import datetime

# Create your models here.

class Note(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(null=False,default=False)
    content=models.TextField(null=False)
    created_at=models.DateTimeField(null=False,default=datetime)

    class Meta:
        managed=True
        db_table='notes'
