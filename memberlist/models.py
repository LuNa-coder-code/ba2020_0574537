# models.py
from django.db import models

class Member(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = "member"