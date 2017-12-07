#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "YGZBxia"
# Date: 2017/12/1
'''
61题750行重要
跳过了18页太他妈难了
第21页的最后有一个题最后写
简单实现一个stack
'''
#1如何实现对python列表去重并保持原先顺序
'''
li=['a','w','c','d','a']
li2=[]
se=set(li)
for i in li:
    if i in se :
        li2.append(i)
        se.remove(i)
print(li2)
'''

#2现有两个元祖(('a'),('b')),(('c'),('d')),请使用python中匿名函数生成列表
'''
set1=(('a'),('b'))
set2=(('c'),('d'))
c=lambda x,y:[{set1[i]:set2[i]} for i in range(len(set1))]
print(c(set1,set2))
'''
#3请给出二分查找的python实例代码
'''


def doubleindex(li,x):
    low = 0
    high=len(li)
    while low <=high:
        mid = int((low+high) /2)
        if li[mid] ==  x:
            return mid
        elif li[mid]<x:
            low = mid+1
        else:
            high=mid-1
    return -1

print(doubleindex(li,7))


li=[1,2,3,4,5,6,7,8,9,10,11,12]

def x(li,x):
    low=0
    high=len(li)
    while low<=high:
        mid = int((low+high)/2)
        if li[mid] == x :
            return mid
        elif li[mid] > x:
            high = mid-1
        else:
            low = mid+1
    return -1
print(x(li,3))
'''

#4在python中字符串格式化中， %和.format的主要区别是什么？
'''
1：format是python独有的格式化方法灵活性高
•传入“ 整数类型 ”的参数  
    •b，将10进制整数自动转换成2进制表示然后格式化  
    •c，将10进制整数自动转换为其对应的unicode字符  
    •d，十进制整数  
    •o，将10进制整数自动转换成8进制表示然后格式化；  
    •x，将10进制整数自动转换成16进制表示然后格式化（小写x）  
    •X，将10进制整数自动转换成16进制表示然后格式化（大写X）  
l = "numers:{:b},{:o},{:d},{:x},{:X},{:%}".format(15,15,15,15,15,15.32445,2)
print(l)

2：%的方式是由c继承来的一种方法
% s字符串（str()的显示）
% r字符串采用repr()显示
% c单个字符
% b二进制整数bin
% i十进制整数int
% o八进制整数oct
% x十六进制整数hex
% f浮点数
% e指数
% % 字符 % （前提是里面要有格式符的话需要这么写）
  
a = "i am %(name)s age %(age)d" % {"name":"alex","age":18}
print(a)
'''

#5：*args和**kwargs在什么情况下会用到？请给出使用**kwargs的实例
'''
在接收额外或者为定义的位置参数会使用*args必须放在关键字参数后面，**kwargs之前，在接收而而外的关键字参数时候会使用**kwargs

def wanner(func,*args,**kwargs):
    def inner(*args,**kwargs):
        c=func()
        return c
    return inner
'''

#6
'''
x='foo'
y=2
print(x*y)#foofoo
'''
#7
'''
dict1={'1':1,'2':2}
dict2=dict1
dict1['1']=5
sum=dict1['1']+dict2['1']
print(sum)#10因为dict1和dict2都指向同一个内存地址
'''

#8
'''
import sys

sys.path.append('/root/mods')#会添加一个新的python模块搜索路径

'''
#9
'''
dic1={}
def addone(country):
    if country in dic1:
        dic1[country]+=1
    else:
        dic1[country]=1
addone('China')
addone('Japan')
addone("china")
print(len(dic1))#3个主要判断字典是否区分大小写
'''

#10
'''
names1=['Amir','Barry','Chales',"Dao"]
names2=names1
names3 = names1[:]
names2[0] = 'Alice'
names3[1] = 'Bob'
sum=0
for ls in (names1,names2,names3):
    if ls[0] == "Alice":
        sum +=1
    if ls[1]=="Bob":
        sum += 10
print(sum) #12还是可变类型的问题 name1和name2指向同一个内存地址，name3的切片是指向新的内存地址
'''

#11
'''
d=lambda p:p*2
t=lambda p:p*3
x=2
x=d(x)
x=t(x)
x=d(x)
print(x)#24一步步的算没有什么难度的题
'''
#12
'''
x=True
y=False
z=False
if x or y and z:
    print('yes')
else:
    print('no')
python的判断顺序是not and or所以先算not在算and 再算or
但是这道题有个bug就是or在判断左侧为真的时候就不会再往后面算了，所以x=True那么后面都不需要看了
'''
#13如何实现list和tuple的转换
'''
li = [1,2,3,4]
tuple1=tuple(li)#列表转换成元祖，
li1 = list(tuple1)#元祖转换成列表
print(li1)
'''
#14请写出一段python代码实现删除一个 list里面的重复元素
'''
li=[1,2,3,4,5,6,7,8,8,9,9,9,9]
#li.count()#获取数量
def test(li):
    for i in li:
        while li.count(i)>1:
            li.pop(i)
    print(li)
test(li)
'''
#15如何得到列表list的交集与差集
'''

l1=[1,2,3,4,5]
l2=[3,4,5,6,7]

def jiaoji(l1,l2):
    l3=[]
    for i in l1:
        if i in l2:
            l3.append(i)
    return l3
print(jiaoji(l1,l2))


def chaji(l1,l2):
    l3=[]
    l4=[]
    for i in l2:
        if i not in l1:
            l3.append(i)
    for i in l1:
        if i not in l2 :
            l4.append(i)
    return l3+l4
print(chaji(l1,l2))
'''
#16
'''
def extendlist(val,list=[]):
    list.append(val)
    return list
print(extendlist(10)) #[10]
print(extendlist(123,[]))# [123]
print(extendlist('a'))#[10,'a']

def extendlist(val,list=[]):
    list.append(val)
    return list
l1=extendlist(10)#[10，'a']
l2=extendlist(123,[])# [123]
l3=extendlist('a')#[10,'a']
print(l1)
print(l2)
print(l3)
print(id(l1))
print(id(l3))


'''

#17
'''
1。python中定义函数时如何写可变参数和关键字参数 *args和**kwargs
2。什么是lambda表达式：
    又叫做匿名函数
        lambda x:x+1
        不脏名称空间
3。re的match()和search()有什么区别
一、解释：
match()函数只检测RE是不是在string的开始位置匹配
search()会扫描整个string查找匹配,会扫描整个字符串并返回第一个成功的匹配
也就是说match（）只有在0位置匹配成功的话才有返回，如果不是开始位置匹配成功的话，match()就返回none
二、例子：
match():
    print(re.match(‘super’, ‘superstition’).span())会返回(0, 5)
    print(re.match(‘super’, ‘insuperable’))则返回None
search():
    print(re.search(‘super’, ‘superstition’).span())返回(0, 5)
    print(re.search(‘super’, ‘insuperable’).span())返回(2, 7)

4。 1 or 2 和 1 and 2输出分别是什么为什么？
分别是1和2 
python是解释性语言 从左到右解释
1 or 2返回1是因为1是True所以后面不做运算直接返回
1 and 2返回2是因为前面判断完成开始判断后面的如果为真那么返回最后一个Ture结果


5。 1<(2==2)和1<2==2结果是什么，为什么
1<(2==2)结果是False是因为前面是数字转换成布尔是True而1转换成布尔也是True所以True<True是错误的返回了False
1<2==2是True是因为1<2返回的结果是True而2转换成布尔是True 两个True是相等的

6。 [i % 2 for i in range(10)] 和 (i %2 for i in range(10))输出的结果是什么

li=[i % 2 for i in range(10)]
si=(i % 2 for i in range(10))
print(li) #[0, 1, 0, 1, 0, 1, 0, 1, 0, 1]是一个列表
print(si) #<generator object <genexpr> at 0x10410e4c0>是一个生成器对象

7。python2和python3的区别
    python2是ascii编码python3是utf-8
    python2是<>python3是！=
    python2打印时print python3打印是print（）
    python2创建类需要继承object，python3自动继承
    python去除了long（）长整型
    python2的类继承是深度搜索，python3的类继承是广度搜索
    python2使用urllib python3使用requests

8。描述unicode、utf-8、gbk的编码之间关系
    utf-8 ---unicode---gbk才能转换
    如果说utf-8和gbk是两个不同国家的客户
    那么unicode就是翻译官
    

9。请描述with的用法？如果自己的类需要支持with语句那么如何书写


class A():
    def __enter__(self):
        print('in enter')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('in exit')
with A() as a:
    print('in with')

结果
in enter
in with
in exit

with是在需要让一个类在初始化前和初始化完成后进行一些操作的时候调用的方法
如果使用with需要类支持__enter__和__exit__两个方法才能使用
with 调用的类 as 被负值的对象

10。python中如何判断一个对象是否可调用对象？那些对象可以是可调用对象，如何定义一个类使其本身就是一个可调用对象？
    1。使用callable()返回True可以
    2。isinstance（func，FunctionType）
    3。hasattr（func，'__call__'）
    如果想要本身就是一个可调用对象可以创建单例模式
def maxSubArray2(li):
    num = li[0]
    sum2 = 0
    left = 0
    right = 0
    temp_left = 0
    for i in range(len(li)):
        sum2 += li[i]
        if sum2 > num:
            if sum(li[left:right+2]) < sum2:
                if temp_left:
                    left = temp_left
                else:
                    left = i
            num = sum2
            right = i
        if sum2 < 0:
            sum2 = 0
            temp_left = i + 1
    return num, li[left:right+1]

print(maxSubArray2([1,2,3,4,5,6,7]))
11。什么装饰器？写一个装饰其可以打印输出方法执行时长的装饰器
装饰器就是在不改变原来函数的的代码，和执行方式上添加新的功能

import time
def wanner(func):
    import time
    li=[]
    def inner(*args,**kwargs):
        li.append(time.time())
        c=func()
        print('runtime = %s' %(time.time()-li[0]))
        return c
    return inner
@wanner
def p10():
    time.sleep(3)
p10()

12.什么实线程，进程，协程
线程好比工厂的一条生产流水线，从开始到结束完成一件事情（因为是cpython所以一个进程下只能有一个线程运行，支持效果比较差，多线程解决io密集型还可以）
进程：好比多家流工厂，可以同时进行流水线实现并发的效果，一个进程至少有一个线程（正常支持也是解决大多数计算型的方法）
协程：通过一条线程实现并发的效果，好处是一条线程实现io复用

13。def f（a，b=【】）
如果这么些就会造成列表元素不清空的问题

14。哪些情况下，y!=x-(x-y)会成立
如果是集合的话x-y是求差集，要保证两个集合不同
如果是算术题的话 x=6。2 y=1。5就行
'''


#18题用python写一个九九乘法表
'''
for i in range(1,10):
    for c in range(1,i+1):
        print('%s * %s = %s' %(c,i,c*i),end='  ')
    print()
i=1

while i <10:
    c=0
    while c<=i:
        print("%s * %s = %s" %(c,i,c*i),end='  ')
        c+=1
    c=1
    print()
    i+=1
'''

#19 在数组中找到具有最大和的连续子数组（至少包含一个数字）
#例如给定数组[-2,1,-3,4,-1,1,1,-5,4]
#连续子阵列[4,-1,2,1]具有最大的sum=6

#20算法是指：解决问题的精确步骤护着解决问题的完美序列

#21 type（1+2l*3。14）结果是
# <type 'float'>

#22 若k为整形，下属weil的循环执行次数为
'''
k=1000
while k>1:
    print(k)
    k=k/2
li=[1000,500,250,125,62,31,15,7,3] #应该是9次
#但是python3是10次,因为会自动转换成浮点型所以不同，python2是直接取到整数部分，python3是//才可以
'''

# 23 判断是不是不合法的布尔表达式:无法输出True和False的就是不合法的
    #比方说 3=a就是不合法的

#24 下列表达式结果为True的是
'''
python2中(3,2)<('a','b')是可以比较的
但是python3中(3,2)<('a','b')是报错的
'''
#25 python不支持得数据类型是 char这个在java和数据库里代表字符串

#26关于python中的复数，下列说法错误的事
'''
1. Phython中关于复数的概念：
   复数由实数部分和虚数部分构成，real + imag（J/j后缀）
   实数部分和虚数部分都是浮点数
>>> aComplex=4.23+8.5j
>>> aComplex
(4.2300000000000004+8.5j)
>>> aComplex.real     #num.real     返回复数的实数部分
4.2300000000000004
>>> aComplex.imag     #num.imag     返回复数的虚数部分
8.5
>>> aComplex.conjugate()     #num..conjugate()     返回复数的共轭复数
(4.2300000000000004-8.5j)
'''
#27关于字符串下列说法错误的是
    #python不是以/0来判断结尾的


#28关于闭包函数
'''
name='1'#4363068000

def func(name):
    print(id(name))
    def funcin(pr):
        print(id(name),id(pr))
    return funcin
c=func(name)

name='2'
c('cc')
print(id(name))
print('===================')
name2='3'
print(id(name2))
def fff(name2):
    print(id(name2))
fff(name2)
name2='4'
print(id(name2))
fff(name2)
闭包函数必须有内嵌函数
内嵌函数需要引用该嵌套函数上一级namespace中的变量
闭包函数必须返回内嵌函数
'''

#29不能创建一个字典的语句是（）
 #字典的key只允许是不可变类型

#30下列python语句正确的是
'''
x=1
y=2

while不能没有结束条件
if语句需要最后加上：
max = x>y ? x:y这是什么东西
'''

#31如何在python中拷贝一个对象？并说明他们之间的区别
'''
import copy

又分成深拷贝和浅拷贝

copy.copy()是前拷贝 主要是拷贝对象的第一层包括方法的但是指向背靠背的对象内存地址，
copy.deepcopy()是深拷贝，将对象整个复制一份然后进行使用
直接把对象付值给一个变量 这个变量指向原来对象的内存地址
'''

#32 谈谈你对python装饰器的理解：
'''
装饰器的特点有内外两层函数
装饰器可以在不改变原有函数的调用方式和改变原有函数的代码进行新的功能的添加
装饰器和已通过@甜品符号进行调用
也可以x=fun（x）然后在x()进行调用
'''
#33 python里面match()和search()的区别
'''
match从头开始匹配如果头部不是的话就会返回None
search 从任意位置匹配，如果没有返回None
'''

#34 获取list的元素个数，和像末尾追加元素所用的方法分别是
'''
count获取个数
append在末尾添加一个元素
'''

#35 判断dict有没有某个元素key的方法是
'''
    dict[a]
    dict.get(a)
'''
#36 l=range(100),
'''
取第一个到第三个元素用l[0:3]
取倒数第二个元素l[-2]
取后10个元素用l[-1:-11]

l=range(100)
print(l[0:3])
for i in l[:-11:-1]:
    print(i)
print(l[-2])
如果要复制一份并且是非引用传递的话 copy.copy()

'''
#37请打印户key，value对
'''
d = {'a':1,'b':2,'c':3}
set1=()
for i,v in d.items():
    print(i,v)
'''

#38如何判定一个变量是不是字符串
'''
c="a"
print(isinstance(c,str))
'''

#39list和tuple有什么不同
'''
tuple：不可变类型，
list ：可变类型
'''

#40 xrange和range有什么不同
'''
print(type(range(10))) 
print(type(xrange(10)))#python三没有xrange 同样也没有range因为python3的range就是python2的xrange
python2 的range返回一个列表，python2的xrange返回一个xrange对象是可迭代的
'''

#41'1,2,3'变成['1','2','3']
'''
x='1,2,3'
c=x.split(',')
print(c)

['1','2','3']变成[1，2，3]
for i in range(len(c)):
    c[i]=int(c[i])
print(c)


list(map(int,['1','2','3']))
'''
#42
'''
def add_end(L=[]):
    L.append('END')
    return L
print(add_end())#['END']
print(add_end())#['END', 'END']
#型参陷阱，因为在函数执行自后列表不清空

'''
#43写一个快拍
'''
def fun(li):
    if len(li) <=1 :return li
    temp=li[len(li)//2]
    left = [ i for i in li if i <temp]
    middel=[ i for i in li if i ==temp]
    right = [i for i in li if i >temp]
    return fun(left) + middel +fun(right)

c=fun([36,5,12,8,21])
print(c)
'''

#44函数中*args和**kwargs的作用
'''
接收为被定义的未知参数和关键参数
'''

#45 is和==的区别是
'''
is是判断两个变量的id地址是否相同
==是仅仅判断两个变量的值是否相等
'''

#46如何生成一个[1，4，9，16，25，36，49]的函数
'''
print([x*x for x in range(1,11)])

'''

#47生成器是什么，有什么作用，写一个生成器

'''
python中一个通过yield返回的函数就是生成器
生成器是一个可迭代的对象，省内存空间，惰性在调用时候才会生成值

def x():
    for i in range(100):
        yield i
'''

#48map (str,[1,2,3,4,5,6])输出什么
'''
map(str,[1,2,3,4,5,6])#会输出一个map对象<map object at 0x104102400>
print(map(str,[1,2,3,4,5,6]))
'''
#49 请写出log的实现（主要更能是打印函数名）
'''
@log
def now():
    print('2013-11-22')

>>>now()
输出:
call now()
2013-12-22


def log(func):
    def inner(*args,**kwargs):
        print('call %s() ' %func.__name__)
        c=func()
        return c
    return inner
@log
def now():
    print('2012-11-11')

now()
'''

#50 怎么取定义一个函数
'''
def <name>(arg1,arg2...argn)
'''

#51 python在linux下创建一个子进程的方法
'''
os.fork()
os.popen() 方法用于从一个命令打开一个管道。
os.system 是执行操作系统终端的方法
os.link() 创建链接，将一个长的文件路径与林一个短的路径进行转换
'''
#52 已知x=43，ch="A",y=1,则表达式(x>=y and ch<'B' and y)的值是
'''
x=43
ch="A"
y=1

print(x>=y and ch<"B" and y)#1
# > = <优先级高于 not and or

'''

#53
'''
字符编码中 0～9 A～Z a～z的顺序排列所以'abc'>'xyz'
python3 (3,2)<('a','b')是会报错的，但是python2就是True
'''

#54
'''
    python支持的数据类型有
        int整形 float浮点型 list列表 dict字典 tuple元祖 set集合 str字符串
'''
#55
'''
int不可以转换非数字字符串 "abcd"
(' " ')这种方式都不可以转化
'''

#56可以输出1，2，3结果的是
'''
a=[0,1,2]
for i in a:
    print(i+1)

for i in range(3):
    print(i+1)
'''

#57一下函数需要其中引入一个全局变量k，请填写语句：
'''
k=1
def fun():
    global k
    k=k+1
fun()
print(k)
'''
#58 请把一下函数转化为python的lambda匿名函数：
'''
def add(x,y):
    return x+y

x=lambda x,y:x+y
'''

#59 请简单解释python中的static method 和class method并补充完整
'''
staticmethod静态方法是封装在类中不需要调用类里面的任何参数，直接通过类调用或者对象调用
classmethod类方法，是传入的是类可以通过类调用不能通过对象调用

class A():
    def foo(self,x):
        print('foo %s' %x)
    @classmethod
    def class_foo(cls,x):
        print('class_foo %s' %x)
    @staticmethod
    def static_foo (x):
        print('static_foo %s' %x)

a=A()
如何调用static_foo方法穿参数
a.static_foo('a')
如何调用class_foo方法调用
A.class_foo('x')
如果直接调用foo
A.foo(a,'x')
a.foo('x')
'''

#60
'''
情书写一个函数，用于替换某个字符串的一个或几个字符,实现str的replace


def replse(li,str1,str2):
    import re
    return re.sub(r'{0}'.format(str1),str2,li)
li='hellow name'
print(replse(li,'name','word'))
'''
#61python实现单例模式
'''
# danli.py 写一个类并实例话

#第二种
class A():
    _instance=None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance=super(A,cls).__new__(cls,*args,**kwargs)
        return cls._instance

a=A()
b=A()


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
# Python2
# class MyClass(object):
#     __metaclass__ = Singleton
# Python3
class MyClass(metaclass=Singleton):
   pass
'''
#62什么事lambda函数：
'''
匿名函数，不会脏到名称空间，可以和map，zip等内置函数联合使用，用一次就会抛弃掉
lambda x：x*3

其中冒号前面的x代表型参 ，冒号代表return
冒号后面代表运行体
'''

#63请写出一段python 代码实现删除一个list里面的重复元素
'''
def deletelist(li):
    for i in li:
        while li.count(i)>1:
            li.remove(i)
    return li
li = [1,2,3,4,5,5,5,6,6,7,7]
'''

#64如何用python删除一个文件
'''
import os
os.remove()删除一个文件
os.removedirs()如果里面有文件则递归删除这个文件夹
os.rmdir()删除一个文件夹要求里面不能有文件
'''

#65python生成随机数
'''
import random
print(random.random())#生成0到1的小数
print(random.randint(1,20))#生成一个1到20的整数
'''
#66如何在def里面设置一个全局变量
'''
global k
'''
#67介绍一下except的用法何作用
'''
try:
    map()
except Exception as e:
    print(e)

如果try捕获到了错误，那么执行except的函数
'''

#68请用python写一下获取用户输入数字，并根据输入数字大小输出不同信息的脚本
"""
while True:
    a=input('''
请输入一个
''')
    if isinstance(a,int):
        print('请输入数字')
        continue
    elif int(a) >10:
        print('超出范围')
        continue
    elif int(a)<10:
        print('输入过小')
        continue
    else:
        print('输入正确')
        break
"""
#69 range和xrange区别：
'''在python2中 range返回一个列表而xrange返回一个可迭代的xrange对象'''

#70 解释生成器与函数的不同，并实现和使用简单的生成器：
'''
生成器也是一个函数，不过是通过yield进行返回而不是通过return进行返回这是最明显的一个特点,会在yield的时候进行截断需要通过__next__才能进行下去

def x():
    for i in range(10):
        yield i

for i in x():
    print(i)
    
'''
#71输入一个字符串，返回倒序排列的结果：如'abcdef'，返回'fedcba'
'''
s='abcdef'
print(s[::-1])
'''

#72请用自己的算法，按照生序合并如下两个list，并去除重复元素：
'''
li1=[2,3,8,4,9,5,6]
li2=[5,6,10,17,11,2]

def qsort(li):
    if len(li) <=1 : return li
    temp = li[len(li)//2]
    left= [x for x in li if x<temp ]
    model=[x for x in li if x == temp]
    right=[x for x in li if x>temp]
    return qsort(left) + model + qsort(right)

def quchong(li):
    for i in li :
        while li.count(i) >1:
            li.remove(i)
    return li

def panxuquchong(li1,li2):
    li=li2+li1
    li=quchong(li)
    li=qsort(li)
    return li

print(panxuquchong(li1,li2))
'''
#73 django中如何在Model保存前做一定的固定操作，比方说写入log：
'''
Django提供一种信号机制。其实就是观察者模式，又叫发布-订阅(Publish/Subscribe) 。当发生一些动作的时候，发出信号，然后监听了这个信号的函数就会执行。
大体有23个信号
常用的有 在Model操作前 pre_save
        在Model操作后 post_save
        
from django.db.models.signals import pre_save
from django.dispatch import receiver
from myapp.models import MyModel


@receiver(pre_save, sender=MyModel)
def my_handler(sender, **kwargs):
    print('我们要做的保存log')        
'''

#73python中，元祖和列表的主要区别是 ：列表是可变数据类型，元祖是不可变数据类型

#74 排好序的列表alist和字符串char，表示alist中存在char1则返回False，不存在返回True的表达式

'''
alit=['a','b','c']
char1='c'
c= False if char1 in alit else True
print(c)
'''

#75 列表变量alist，将alist分别赋予给maxvale和minValue的表达式；
'''
li1=[1,2,3,4,5]
maxvale,minValue = max(li1),min(li1)
print(maxvale,minValue)
'''

#76 列表
'''
li1=[{'a':5,"b":2},{'a':2,"b":8},{'a':8,"b":2}]
# 请写出以建"a"的值对li1进行排序操作
print(sorted(li1,key=lambda x:x['a']))
'''
#77阅读以下代码然后写出程序的结果
'''
my_dict={'a':0,'b':1}
def func(d):
    d['a']=1
    return d
func(my_dict)
my_dict['c']=2
print(my_dict)# {'a':1,'b':1,'c':2}
'''

#78下面列表输出结果为
'''
li1=[2,4,5,6,7]
for var in li1:
    if (var % 2) == 0:
        li1.remove(var)

print(li1)#[4,5,7]
'''

#79求列表li1和列表li2的交集表达式：
'''
li1=[1,2,3,4]
li2=[2,3,4,5]
print([i for i in li1 if i in li2])
'''

#80不依赖中间变量，交换变量a和b值的表达式：
'''
a=1
b=2
a,b=b,a
'''

#81现有列表 li=[3,1,-4,2]按其元素的绝对中大小进行排序的表达式：
'''
li=[3,1,-4,2]
print(sorted(li,key=lambda x:abs(x)))
'''
#82写出下面代码输出的结果是:

'''
n=5
print(-n)#-5
'''
#83python是一门解释性语言，面向对象的语言，高级语言，可移植，可拓展

#84哪个pep涉及到了代码规范pep8

#85 django，flask，tornado，web。py

#86有函数定义如下
'''
def ca(a,b,c,d=1,e=2):
    return (a+b)*(c-d) +e

print(ca(1,2,3,4,5))#2
print(ca(1,2,3))#8
# print(ca(1,2))#报错
print(ca(1,2,3,e=4))#10
print(ca(e=4,c=5,a=2,b=3))#24
# print(ca(1,2,3,d=5,4))#直接报错
'''

#87 3<4<5是什么的缩写 3<4 and 4<5的缩写

#88 获取python解释器版本的方法是
'''
import sys
sys.version
'''

#89如果是被倒入的模块，模块点__name__的值是,当前文件名称 ,如果该模块内__name__那么是__main__

#90python的内存管理中，为了追踪内存中的对象，使用了
'''
Python引入了一个机制：引用计数。
python内部使用引用计数，来保持追踪内存中的对象，Python内部记录了对象有多少个引用，即引用计数，当对象被创建时就创建了一个引用计数，当对象不再需要时，这个对象的引用计数为0时，它被垃圾回收。
'''

#91python的c语言解释器是cpython，python的java叫jython

#92python中，能直接显示释放内存的资源
'''
import gc
1.gc.set_debug（flags）设置gc的debug日志，一般设置为gc.DEBUG_LEAK
2.gc.collect([generation])显式进行垃圾回收，可以输入参数，0代表只检查第一代的对象，1代表检查
一，二代的对象，2代表检查一，二，三代的对象，如果不传参数，执行一个full collection，也就是等于传2.
返回不可达（unreachable objects）对象的数目
3.gc.get_threshold()获取的gc模块中自动执行垃圾回收的频率
4.gc.set_threshold(threshold0[,threshold1[,threshold2])设置自动执行垃圾回收的频率
5.gc.get_count()获取当前自动执行垃圾回收的计数器，返回一个长度为3的列表
'''

#93 以下代码将输出什么
'''
li=['a','b','c','d']
print(li[10:]) #[]
'''

#94与 16体重复了

'''
list2=extendleis('a',[])

'''

#95
'''
数组
nums = [2,7,11,15] 目标是9
返回 [0,1]索引


nums = [2,7,11,15]
num=13
def fun(li,ints):
    mins=0
    maxs=len(li)-1
    for i in range(len(li)):
        if (li[mins]+li[maxs]) == ints:
            return [mins ,maxs]
        elif (li[mins]+li[maxs])>ints:
            maxs-=1
        else:
            mins+=1
    return None
print(fun(nums,num))

'''


#96python，判断一个字典中是否有这些key："AAA","BB"
'''
dic1={'AAA':1,"BB":2,"DD":1,'EEE':1}
li=dic1.keys()
if "AAA" in li or "BB" in li or 'DD' in li or 'EEE'in li:
    print(True)

'''

#97 python取出1-100的偶数
'''
li =[x for x in range(1,101) if x%2==0]
print(li)
'''
#98 1，2，3，4，5组成多少个不重复并且没有相同数字的的3位数
'''
for i in range(1,6):
    for x in range(1,6):
        if i==x:
            continue
        for y in range(1,6):
            if i==x or i==y or x==y:
                continue
            print("%s%s%s" %(i,x,y))

'''

#99写出5中http请求：
'''
OPTIONS：返回服务器针对特定资源所支持的HTTP请求方法。也可以利用向Web服务器发送'*'的请求来测试服务器的功能性。 
HEAD：向服务器索要与GET请求相一致的响应，只不过响应体将不会被返回。这一方法可以在不必传输整个响应内容的情况下，就可以获取包含在响应消息头中的元信息。 
GET：向特定的资源发出请求。 
POST：向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的创建和/或已有资源的修改。 
PUT：向指定资源位置上传其最新内容。 
DELETE：请求服务器删除Request-URI所标识的资源。 
TRACE：回显服务器收到的请求，主要用于测试或诊断。 

CONNECT：HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。

   虽然HTTP的请求方式有8种，但是我们在实际应用中常用的也就是get和post，其他请求方式也都可以通过这两种方式间接的来实现。
'''
#100 描述多继承开发中join与daemon的区别：
'''
Daemon线程称为守护线程（非常喜欢这个名字）。线程一旦被设置为守护线程，当非守护线程结束，守护线程即使没有执行完，也必须随之全部结束。例如我们曾经玩儿过的坦克大战，一旦守护的老巢完蛋了，其它守护坦克没死也要结束。
join就像是手动的进行线程阻塞如果运行到join这里下面的代码需要等待
举个例子 如果我们在一个进程例开了多个子线程，那么我们可能有一个子线程是大量算术运算，这个时候主线程肯定早于子线程，我们需要加一个join这样，主线成就会在子线程运行完成了才会接着进行
'''
#101简单描述GIL对python性能的影响

'''
GIL是cpython解释器才存在的，他是一种考虑到线程安全的安全锁，所以它的出现，导致了一个python的一个进程中只能有一个线程在系统中运行者，其他线程需要等待这个线程本次执行被切换掉，释放权限（这里可以理解为一个把锁，当前运行的线程有一个钥匙，其他线程需要等这个线程释放这个钥匙）。然后其他线程在争夺，也就是说，python的多线程真正在一个时间上工作的只有一个线程，影响了python多线程去进行计算密集型操作。
'''

#102写一个斐波那契饿:1,2,3,5,8,13
'''
x=0
y=1
z=0
for i in range(100):
    if y >=4000000:
        print('四百万前是 %s' %y)
        print('索引为 %s' %i)
        break
    z=x
    x=y
    y=z+x
四百万前是 5702887
索引为 33
    '''
#103两个字典相加相同的key保留相加后的值不同的key保留
'''
dic1={'a':1,"b":2,"c":3,'d':4,'f':'hellow'}
dic2={'b':3,'d':5,'e':7,'m':9,'k':'world'}

dictc={}
for i in dic1:
    if i in dic2:
        dictc[i]=dic1[i]+dic2[i]
    else:
        dictc[i]=dic1[i]
for i in dic2:
    if i not in dictc:
        dictc[i]=dic2[i]
print(dictc)

def hebing(dic1,dic2):
    for i in dic1:
        if i in dic2:
            dic2[i]=dic1[i]+dic2[i]
        else:
            dic2[i]=dic1[i]
    return dic2
'''
#104海滩上有一堆桃子，共5个猴子第一个猴子分成5份多一个，扔到拿走一份，第二个猴子将剩下的部分分成5份后多一个丢掉，以此类推请问最后需要多少桃子
'''
分析：如果说每一次都扔到一个的话，证明每一次都缺少4个才能正确平分成5份，所以开始多给4个桃子，那么就能是被5整除的数字了，但是在第一只猴子拿走后我们多给了4个桃子所以要拿回来，这样给四个再拿走四个就可以保证每次都是被5整除，在最后一次平分的时候我们就做一次减四就好

def houzifentao(x):
    return x**5-4
'''

#105编程实现小程序，给出罗马数字，先判断是否是罗马数字，如果是，转换为阿拉伯数字
#

#106
'''
class Ob():
    x=1
class Ob1(Ob):
    pass
class Ob2(Ob):
    pass

print(Ob.x,Ob1.x,Ob2.x)
Ob1.x=2
print(Ob.x,Ob1.x,Ob2.x)
Ob.x=3
print(Ob.x,Ob1.x,Ob2.x)
1 1 1
1 2 1
3 2 3
'''
#107
'''
def m():
    return [lambda x:i*x for i in range(4)]
print([c(2) for c in m()])#6,6,6,6

def m():
    return (lambda x:x*i for i in range(4))
print([c(2) for c in m()])#0,2,4,6
'''

#108相隔为10的区间总共21个区间输入一数字确认等级：
'''
def fun(x):
    if x==0:
        print('请输入大于0的数字')
        return
    elif x>200:
        print('当前等级：21')
        return
    c,v=divmod(x,10)
    if v:
        print('当前的区间是：%s' % (x // (10 ) + 1))
        return
    else:
        print('当前的区间是：%s' % (x // 10 ))
        return
fun(199)
'''
#109
'''
data={
    'time':'2016-08-05',
    'some_id':'ID1234',
    'grp1':{
        'fld1':1,
        'fld2':2
    },
    'xxx2':{'fld3':0,'fld5':0.4},
    'fld6':11,
    'fld7':7,
    'fld46':8}
fields='fld2|fld3|fld7|fld19|fld5'

print(fields.split('|'))

def dict_get(data, objkey,defult):
    tmp = data
    for k,v in tmp.items():
        if k == objkey:
            return v
        else:
            if isinstance(v,dict):
                ret = dict_get(v,objkey,defult)
                if ret is not defult :
                    return ret
    return defult

def select(data,fields,defult=[]):
    result={}
    for i in fields.split('|'):
        v=dict_get(data,i,defult)
        if v!=defult:
            if v==False:
                result[i]=int(v)
            else:
                result[i]=v
    return result

print(select(data,fields))

'''

#110:从输入一个网址到页面返回，中间经历了什么？
'''
1。 用户输入url
2。浏览器进行缓存检查
3。检查是否过期，如果不过期那么展示给用户发送302
4。如果过期了，那么通过dns解析
5。发送给解析后的ip进行tcp链接
6。服务器根据请求调取模版，数据库
7。在服务器进行封包 发送给浏览器
8。浏览器接收数据：
9。判定状态码
10。（200）浏览器进行dom树生成，css渲染，js交互
11。如果有ajax再次进行访问
12。完成
'''
#111：http协议状态吗有什么用，列出你知道的http协议的状态吗
'''
1XX系列：指定客户端应相应的某些动作，代表请求已被接受，需要继续处理。由于
HTTP / 1.0协议中没有定义任何1xx状态码，所以除非在某些试验条件下，服务器禁止向此类客户端发送1xx响应。
2XX系列：代表请求已成功被服务器接收、理解、并接受。这系列中最常见的有200、201状态码。
200状态码：表示请求已成功，请求所希望的响应头或数据体将随此响应返回
201状态码：表示请求成功并且服务器创建了新的资源，且其URI已经随Location头信息返回。假如需要的资源无法及时建立的话，应当返回'202 Accepted'
202状态码：服务器已接受请求，但尚未处理
3XX系列：代表需要客户端采取进一步的操作才能完成请求，这些状态码用来重定向，后续的请求地址（重定向目标）在本次响应的Location域中指明。这系列中最常见的有301、302状态码。
301状态码：被请求的资源已永久移动到新位置。服务器返回此响应（对GET或HEAD请求的响应）时，会自动将请求者转到新位置。
302状态码：请求的资源临时从不同的URI响应请求，但请求者应继续使用原有位置来进行以后的请求
304自从上次请求后，请求的网页未修改过。服务器返回此响应时，不会返回网页内容。 如果网页自请求者上次请求后再也没有更改过，您应将服务器配置为返回此响应(称为If - Modified - SinceHTTP标头。
4XX系列：表示请求错误。代表了客户端看起来可能发生了错误，妨碍了服务器的处理。常见有：401、404
状态码。
401状态码：请求要求身份验证。 对于需要登录的网页，服务器可能返回此响应。
403状态码：服务器已经理解请求，但是拒绝执行它。与401响应不同的是，身份验证并不能提供任何帮助，而且这个请求也不应该被重复提交。
404状态码：请求失败，请求所希望得到的资源未被在服务器上发现。没有信息能够告诉用户这个状况到底是暂时的还是永久的。假如服务器知道情况的话，应当使用410状态码来告知旧资源因为某些内部的配置机制问题，已经永久的不可用，而且没有任何可以跳转的地址。404
这个状态码被广泛应用于当服务器不想揭示到底为何请求被拒绝或者没有其他适合的响应可用的情况下。
5xx系列：代表了服务器在处理请求的过程中有错误或者异常状态发生，也有可能是服务器意识到以当前的软硬件资源无法完成对请求的处理。常见有500、503
状态码。
500状态码：服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。一般来说，这个问题都会在服务器的程序码出错时出现。
503状态码：由于临时的服务器维护或者过载，服务器当前无法处理请求。通常，这个是暂时状态，一段时间会恢复了解基本SEO状态码，是SEO优化人员必备知识。HTTP状态码是服务器和客户端之间交流信息的语言。通过查看网站日志的HTTP码，我们可以清楚查看搜索引擎在网站的爬取情况。
'''

#112python主要内置数据类型有哪些，可以变和不可变有什么区别
'''
不可变类型：(str,tuple,int)
可变类型:(set,dict,list)
id比可以变，但是值可以变就是最大的区别

'''

#113python中如何抛出异常，捕获，处理异常
'''
raise 主动抛出异常
try捕获一段代码中的异常
except:负责处理收到的异常异常 
'''

#114给定两个列表，找出相同元素和不同元素，可以打乱顺序
'''
a = t | s          # t 和 s的并集  
  
b = t & s          # t 和 s的交集  
  
c = t – s          # 求差集（项在t中，但不在s中）  
  
d = t ^ s          # 对称差集（项在t或s中，但不会同时出现在二者中）
'''
#115给定一个3g文件，每一行是酒店id和图片的名字，中间用'\t'分割，要求输出照片数量分别是[10,20],[5,10],[0,5]的三个列表

'''
def read_text():
    dic={}
    for i in open('a.txt','r'):
        host_id,jpeg=i.split(r'\t')
        if host_id in dic:
            dic[host_id]+=1
        else:
            dic[host_id]=1
            
    lis1=[]
    lis2=[]
    lis3=[]
    lis4=[]
    for k,v in dic.items():
        if v<5:
            lis1.append(k)
        elif 5<=v<10:
            lis2.append(k)
        elif 10<=v<20:
            lis3.append(k)
        else:
            lis4.append(k)
    with open('b.txt','w') as f:
        f.write('图片数量小于5的宾馆ID：')
        for i in lis1:
            f.write(i)        
        f.write('图片数量在5到9的宾馆ID：')
        for i in lis2:
            f.write(i)        
        f.write('图片数量在10到19的宾馆ID：')
        for i in lis3:
            f.write(i)        
        f.write('图片数量大于19的宾馆ID：')
        for i in lis4:
            f.write(i)
'''

#116什么是lambda函数，他有什么好处，另外python在函数时编程方面提供了些什么函数和语法
'''
匿名函数,
好处：不会脏到名称空间，可以用完就扔掉

map函数
abs函数求绝对值
cmp比大小
divmod求余数和
进制转换函数
filter函数删选
zip函数拉链
反射函数
hasattr
getattr
求最大值max，最小值min
'''

#117详细说明tuple、list、dict的用法他们的特点
'''
tuple不可变类型，元祖，生成后里面的值不可以修改
list列表可变类型，生成后里面值可以修改，
这两个都可以切片，但是元祖不可以替换
dict字典，通过key：value的方式储存数据，查询速度快，可变类型，通过get或者[]取值，内置__getitem__方法
'''

#118pyton中装饰器，迭代器的用法，描述下dict的items和iteritems方法的不同
'''
python的装饰器是在不该变原有的代码，和调用方式的基础上，对代码添加新的功能】通过@甜品符加上装饰器的名字进行使用，第二种方式是通过 函数名=装饰器（函数名）
python的迭代器可以通过for循环调用，也可以next()也可以迭代器__next__的方式使用
、

items返回的是（key，value）
iteritems返回的是iter对象
'''
#119讲讲对unicode,gbk,utf-8等的理解，python2是如何处理编码问题额
'''
unicode相当于翻译官将gbk通过unicode转换成utf-8也可以反过来转换
python2处理编码
都是讲其他编码转换成unicode进行处理，输出在进行转换
'''

#120python进行内存管理的，python的程序会内存泄漏吗，说说有没有什么方法防止或者检测内存泄漏
'''
python通过引用计数进行内存管理，如果计数为0那么释放内存，
python会存在内存泄漏的

避免方式：减少全局变量的定义，分散引用，通过一个变量减少多次引用，减少死循环

检测工具：objgraph
'''

#121在python程序的运行方面，有什么能够提升性能：

'''
1：sum函数尽量处理啊大数量级数据
2：合理的使用yield
3：尽量使用dict和set进行查找
4：尽量使用divmod
'''
#122list对象按照age进行由大到小排序
'''
alist=[{'name':'a','age':20},{'name':'b','age':30},{'name':'c','age':25}]

c=sorted(alist,key=lambda x:x['age'],reverse=True)
print(c)
'''
#123 两个list对象，合并去重
'''
lis1=['a','b','c','d','e','f']
lis2=['x','y','z','d','e','f']
endlis=list(set(lis1+lis2))
print(endlis)
'''

#124 打乱一个排好序的list对象
'''
import random
li=[1,2,3,4,5,6,7,7,4]
li=random.shuffle(li)
'''

#125 简单实现一个stack

#126输入某年某月末日，判断这一天是这一年的第几天（）
'''
import datetime

year=int(input('输入年'))
moun=int(input('输入月'))
day = int(input('输入日'))

nowdata=datetime.date(year,moun,day)
f=nowdata-datetime.date(nowdata.year-1,12,31)
print('是{0}年的第{1}天'.format(nowdata.year,f.days))
'''
#127将字符串：'k:1|k1:2|k2:3|k3:4',处理成字典
'''
li='k:1|k1:2|k2:3|k3:4'
nowli=li.split('|')
dic={}
for i in nowli:
    k,v=i.split(':')
    dic[k]=v
print(dic)
'''

#128 描述一下对pyton中数据类型列表，字典，元祖的理解
'''
列表list

可以包含不同类型的对象，可以增减元素，可以跟其他的列表结合或者把一个列表拆分，用[]来定义的 eg:aList=[123,’abc’,4.56,[‘inner’,’list’],7-9j] 
方法 
1.list(str):将str转换成list类型，str可以使字符串也可以是元组类型 
2.aList.append(‘test’):追加元素到列表中去 
3.del aList[1]:删除列表中下标为1的元素 del aList:删除整个列表 
4.cmp(list1,list2):比较两个列表的大小 
6.sorted(list):使用字典序对列表中元素进行排序 
7.reversed(list):倒置列表中的元素位置 
9.list.extend(seq):把序列seq的内容添加到list中 
10.list.insert(index,obj):在索引量为index的地方插入obj对象 
11.list.pop(index=-1):删除并返回指定位置的对象，默认是最后一个对象 
12.list.remove(obj):从list中删除obj对象。

元组tuple

可以包含不同类型的对象，但是是不可变的，不可以在增减元素，用()来定义 eg:aTuple=(123,’abc’,4.56,[‘inner’,’list’],7-9j) 
方法 
1.tuple(obj):将对象obj转换成tuple对象，obj可以是任意字符串或者列表 
2.适用于列表的del,cmp,len,max,min方法也适用于tuple，但是由于元祖是不可变的，替换、添加、排序等不可实现

字典dict

键值对，用{}来定义 eg:aDict={‘name’:’cynthia’,’age’:18} 
方法 
1.dict1=dict(([‘x’,1],[‘y’,2])):dict()创建字典 
2.dict1={}.fromkeys((‘x’,’y’),-1):fromkeys()创建一个默认字典，字典中元素具有相同的值 
3.dict1.keys():获取字典的键值列表 
4.dict1.has_key(‘x’):判断字典中是否有‘x’键值，返回bool型 
5.dict.get(key,default):返回键值key的值，若是key不存在，返回default的值 
6.dict.items():返回键值对列表值 
7.dict.values():返回字典中所有值的列表 
8.dict.update(dict2):将dict2的键值对列表添加到字典dict中去 
9.dict.pop(key)：返回键值key的value 
10.setdefault():类似get方法，能够获得给定key的value，此外setdefault还能在自动重不含有给定key的情况下设定相应的key-value 
11.clear():清除字典中所有的项。原地操作，无返回(或说返回值为None） 
12.copy():返回具有相同key-value的新字典，为浅复制(shallow copy)
'''
#129如何删除一个list中的元素，如何删除dict中的一段kv
'''
list删除：
    list.remove()有元素删除成功，没有报错
    list.pop()有元素删除成功，没有删除最后一个元素
dict删除:
    dict.pop()有key删除，
    dict.popitem()删除后返回被删除的k，v
'''
#130如何查找一个字符串中的特定字符？find（）和indexof（）两个函数哟什么差异
'''
li="12345678123411"
print(li.find('2'))

返回下角标，但是python中没有indexof
# print(li.indexOf('1'))
'''
#131python中使用过哪些三方健：
'''
    爬虫类:Scrapy,beautfulesoup，requests
    web类：tornado,Django
    数据类：numpy，pandas
'''

#132描述一下MVC架构：
'''
module-view-control
数据-试图-控制器架构：
module负责数据的存储过程
view负责返回给用户的数据操作。
control负责监控用户发送的信息
'''

#133描述一下表与视图的理解
'''
      1、视图是已经编译好的sql语句。而表不是  
      2、视图没有实际的物理记录。而表有。
      3、表是内容，视图是窗口
      4、表只用物理空间而视图不占用物理空间，视图只是逻辑概念的存在，表可以及时对它进行修改，但视图只能有创建的语句来修改
      5、表是内模式，视图是外模式
      6、视图是查看数据表的一种方法，可以查询数据表中某些字段构成的数据，只是一些SQL语句的集合。从安全的角度说，视图可以不给用户接触数据表，从而不知道表结构。
      7、表属于全局模式中的表，是实表；视图属于局部模式的表，是虚表。 
      8、视图的建立和删除只影响视图本身，不影响对应的基本表。
'''

#134 索引有什么作用，有哪些分类，有什么好处和坏处？
'''
简单的说，索引就好比一本书的目录，你只要浏览标题就可以快速的找到具体内容是放在哪一页的。也就是说用SELECT查找时不用直接去搜索表，只要查找索引，就可以直接定位到你想查找的内容位置。
索引带来的方便不是免费的，是以每次插入或更新（相当于删除并插入）时都要维护索引为代价的。
所以如果一张表更多是用于查询而很少插入，那么就可以建立尽量多的索引以优化查询性能。相反如果一张表要经常插入或更新，则尽可能少用索引，有时甚至连主键都不建。
'''