from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    age = models.IntegerField(3)
    email = models.CharField(max_length=50)

    class Meta:
        db_table = "users_tb"

    def __str__(self):
        return self.username