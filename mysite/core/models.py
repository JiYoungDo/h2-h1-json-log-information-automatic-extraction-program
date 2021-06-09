from django.db import models

# Create your models here.


class ImamgeUpload(models.Model):
    title = models.CharField(max_length=100)
    pic = models.FileField(null=True, blank =True, upload_to="")

    def __str__(self):
        return self.title

# 해당 정보를 저장하려고 한다면. 
class user_Saved(models.Model):
    first_send = models.IntegerField() 
    last_recv = models.IntegerField()
    
    result = last_recv - first_send

    def __str__(self):
        return self.result