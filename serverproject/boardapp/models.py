from django.db import models
from django.db.models.fields import DateField
# Create your models here.

class Board(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    file = models.FileField(null=True)
    image = models.ImageField(null=True)
    date = models.DateField(auto_now_add=True)
    #user = models.CharField(max_length=50) # 추후 테이블 매핑해야함


    def __str__(self):
        return self.title