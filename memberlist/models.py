# models.py
from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)
   # image = models.ImageField(upload_to='boxinggloves', blank=True)

    class Meta:
        db_table = "member"