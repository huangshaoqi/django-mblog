from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=32,default="user")
    password = models.CharField(max_length=32,default='123456')
    age = models.IntegerField(3,default=20)
    email = models.CharField(max_length=50,null=True)

    class Meta:
        db_table = "users_tb"

    def __str__(self):
        return self.username