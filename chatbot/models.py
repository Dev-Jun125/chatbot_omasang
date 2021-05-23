from django.db import models

# Create your models here.

class info(models.Model):
    created = models.CharField(
        max_length=45)
    idx = models.CharField(
        max_length=45)
    message = models.CharField(
        max_length=45
    )
    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'learn_chat'

class test(models.Model):
    idx = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    objects = models.Manager()
    class Meta:
        managed = False
        db_table = 'learn_chat'