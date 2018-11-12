from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from . import models


# Create your views here.
def hello(request, argument):
    data = "这是一个测试的模板文件"
    return render(request, "index/hello.html", {'info': data, 'arg': argument})


def number(request, num):
    return HttpResponse("这是数值url：" + num)


def letter(request, letter):
    return HttpResponse("这是字母url：" + letter)


def index(request, page="1"):
    # print(reverse('index'))
    return render(request, "index/index.html", {'page': page})


def pp(request, page="1", p="a"):
    # print(reverse('index'))
    return render(request, "index/pp.html", {'page': page, 'p': p})


###################################################################################
# form增删改查                                                                     #
###################################################################################
def select(request):
    '''查询'''
    ob = models.Users.objects.all()
<<<<<<< HEAD
    print(ob)
    return render(request, "form/add-select.html", {'accounts': ob})

=======
    # print(ob)
    return render(request,"form/add-select.html",{'accounts':ob})
>>>>>>> 8e41cce2a9d9748d564d993d80ed20e117a0d5b8

def add(request):
    '''添加'''
    data = request.GET.dict()

    try:
        if not data['age']:
            data['age'] = 0
        else:
            data['age'] = int(data['age'])
    except Exception:
        data['age'] = 0

    print(data)
    ob = models.Users(**data)
    ob.save()
    # return render(request,"form/add-select.html",{'accounts':ob})
    return redirect(reverse('select'))


def delete(request, id):
    '''删除'''
    ob = models.Users.objects.get(id=id)
    ob.delete()
    return redirect(reverse('select'))


def modify_1(request, id):
    '''修改'''
    ob = models.Users.objects.get(id=id)
    return render(request, 'form/modify.html', {'account': ob})


def modify_2(request, id):
    '''确认修改'''
    ob = models.Users.objects.get(id=id)
    data = request.GET.dict()

    try:
        if not data['age']:
            data['age'] = 0
        else:
            data['age'] = int(data['age'])
    except Exception:
        data['age'] = 0

    ob.username = data['username']
    ob.password = data['password']
    ob.email = data['email']
    ob.age = data['age']
    ob.save()
    return redirect(reverse('select'))


###########################################################################
# 一对一，一对多，多对多

### 一对一
def oto(request):
    o1 = models.One.objects.create(oname='张三', oage=11, odate='2011-11-11')
    o2 = models.One.objects.create(oname='张三2', oage=12, odate='2012-12-12')

    t1 = models.Two.objects.create(tsub=o1, tfond='o1', tdes='我喜欢o1')
    t2 = models.Two.objects.create(tsub=o2, tfond='o2', tdes='我喜欢o2')

    # 通过外键查找
    obj1 = models.Two.objects.get(tsub_id=1)
    return HttpResponse(str(obj1.tsub.oname))
    # 通过表名来反过来查找,表名小写
    # 删除操作
    # obj1 = models.One.objects.get(id=1)
    # return HttpResponse(str(obj1.two.delete()))
    # obj1 = models.Two.objects.get(tsub_id=2)
    # return HttpResponse(str(obj1.tsub.delete()))


########## 一对多
def p_c_add(request):
    p1 = models.People.objects.create(name='小王', card_num=4)
    p2 = models.People.objects.create(name='老王', card_num=40)

    c1 = models.Card(number='101', source='中国银行', person=p1)
    c2 = models.Card(number='102', source='中国农行', person=p1)
    c3 = models.Card(number='110', source='中国建行', person=p1)
    c1.save()
    c2.save()
    c3.save()

    c4 = models.Card(number='201', source='河南郑州美容美发', person=p2)
    c5 = models.Card(number='202', source='郑州交通一卡通', person=p2)
    c6 = models.Card(number='203', source='郑州逍遥镇胡辣汤', person=p2)
    c7 = models.Card(number='204', source='郑州惠济四附院', person=p2)

    c4.save()
    c5.save()
    c6.save()
    c7.save()
    return HttpResponse('添加成功')


def p_c_select(request):
    # 查找number=203的人
    c1 = models.Card.objects.get(number='203')
    print(c1.person.name)
    # 查找id为3对应的人
    c2 = models.Card.objects.get(id=3)
    print(c2.person.name)
    # 查找c2的所有卡
    result = c2.person.card_set.all()
    print(result)
    for res in result:
        print(res.source)
    # 查找名字为老王的所有卡种
    result = models.People.objects.get(name='老王')
    for card in result.card_set.all():
        print(card.source)
    return HttpResponse('查询成功')


###多对多
def book_add(request):
    p1 = models.Publication(pname='大象出版社', paddress='河南', )
    p2 = models.Publication(pname='北京出版社', paddress='北京')
    p3 = models.Publication(pname='清华出版社', paddress='河北')
    p1.save()
    p2.save()
    p3.save()

    b1 = models.Book(bname='海底两万里', bauthor='赵四')
    b2 = models.Book(bname='遮天', bauthor='辰东')
    b3 = models.Book(bname='童年', bauthor='xxxx')
    b4 = models.Book(bname='在人间', bauthor='yyyy')
    b5 = models.Book(bname='我的大学', bauthor='张飞')
    b6 = models.Book(bname='汤姆索亚历险记', bauthor='赵六儿')
    b1.save()
    b2.save()
    b3.save()
    b4.save()
    b5.save()
    b6.save()

    b1.publication.add(p1, p2, p3)
    b2.publication.add(p1, p2)
    b3.publication.add(p1, p3)
    b4.publication.add(p2, p3)
    b5.publication.add(p3)
    # 多对多关系，两个表不直接产生联系，而是将两个表之间的关系记录在中间表上
    # 中间表不需要创建，会自动生成
    return HttpResponse('添加成功')


def book_select(request):
    # 通过书籍查找对应的出版社
    b1 = models.Book.objects.get(bname='童年')
    # 获取出版童年的所有出版社
    b1_publication = b1.publication.all()
    for pub in b1_publication:
        print(pub.pname,pub.paddress)

    # 通过出版社查找所有的书
    p1 = models.Publication.objects.get(pname='清华出版社')
    all_book = p1.book_set.all()
    print('------------------')
    for book in all_book:
        print(book.bname,book.bauthor)
    return HttpResponse('查找成功')
