from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse


# Create your views here.
def hello(request,argument):
    data = "这是一个测试的模板文件"
    return render(request,"index/hello.html",{'info':data,'arg':argument})


def number(request,num):
    return HttpResponse("这是数值url："+num)


def letter(request,letter):
    return HttpResponse("这是字母url："+letter)

def index(request,page="1"):
    # print(reverse('index'))
    return render(request,"index/index.html",{'page':page})

def pp(request,page="1",p="a"):
    # print(reverse('index'))
    return render(request,"index/pp.html",{'page':page,'p':p})
