from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from . import models


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

# form增删改查

def select(request):
    '''查询'''
    ob = models.Users.objects.all()
    print(ob)
    return render(request,"form/add-select.html",{'accounts':ob})

def add(request):
    '''添加'''
    data = request.GET.dict()
    data['age'] = int(data['age'])
    print(data)
    ob = models.Users(**data)
    ob.save()
    # return render(request,"form/add-select.html",{'accounts':ob})
    return redirect(reverse('select'))

def delete(request,id):
    '''删除'''
    ob = models.Users.objects.get(id=id)
    ob.delete()
    return redirect(reverse('select'))

def modify_1(request,id):
    '''修改'''
    ob = models.Users.objects.get(id=id)

    return render(request,'form/modify.html',{'account':ob})

def modify_2(request,id):
    '''确认修改'''
    ob = models.Users.objects.get(id=id)
    data = request.GET.dict()
    data['age'] = int(data['age'])
    ob.username = data['username']
    ob.password = data['password']
    ob.email = data['email']
    ob.age = data['age']
    ob.save()

    return redirect(reverse('select'))