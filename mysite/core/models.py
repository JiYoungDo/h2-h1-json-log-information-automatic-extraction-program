from django.db import models

# Create your models here.


class File(models.Model):
    filegroup  = models.CharField(max_length=100)
    filenum  = models.CharField(max_length=100)
    json = models.FileField(upload_to='files/json/')

    # str 메소드 / 클래스 자체 내용 출력하고 싶을 대 형식 지정 메서드
    def __str__(self):
        return 'filegroup: {}, filenum; {}'.format(self.filegroup, self.filenum)

