from django.db import models


# Create your models here.
class Users(models.Model):
    username = models.CharField(max_length=32, default="user")
    password = models.CharField(max_length=32, default='123456')
    age = models.IntegerField(3, default=20)
    email = models.CharField(max_length=50, null=True)

    class Meta:
        db_table = "users_tb"

    def __str__(self):
        return self.username


###########################################################################
# 一对一，一对多，多对多


# 一对一
class One(models.Model):
    oname = models.CharField(max_length=20, null=True)
    oage = models.CharField(max_length=20, null=True)
    odate = models.DateField(null=True)


class Two(models.Model):
    # 设置一对一关系，是通过将表中的字段设置为主键完成的
    # on_delete=models.CASCADE 当父表中的某一条数据删除的时候
    # 相关字表中的数据也会被删除

    tsub = models.OneToOneField(One, on_delete=models.CASCADE, primary_key=True)  # 外键
    tfond = models.CharField(max_length=20, null=True)
    tdes = models.CharField(max_length=200, null=True)


####### 一对多
class People(models.Model):
    name = models.CharField(max_length=50)
    card_num = models.IntegerField(default=0)


class Card(models.Model):
    number = models.CharField(max_length=20)
    person = models.ForeignKey(People, on_delete=models.CASCADE)
    source = models.CharField(max_length=50)


###多对多

class Publication(models.Model):
    pname = models.CharField(max_length=200)
    paddress = models.CharField(max_length=200)


class Book(models.Model):
    bname = models.CharField(max_length=200)
    bauthor = models.CharField(max_length=200)
    publication = models.ManyToManyField(Publication)
