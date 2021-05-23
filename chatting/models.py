from django.db import models

# Create your models here.

class Userinput(models.Model):
    idx = models.AutoField(primary_key=True)
    userinput = models.CharField(db_column='userInput', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'userInput'


class Conversation(models.Model):
    input_text = models.CharField(max_length=255)
    output_text = models.CharField(max_length=500)
    pos_tags = models.CharField(max_length=255, blank=True, null=True)
    tagging = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'conversation'