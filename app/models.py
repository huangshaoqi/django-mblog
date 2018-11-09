from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=50)

    class Meta:
        db_table = "polls_users"  # 指定表名
