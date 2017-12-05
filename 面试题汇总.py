#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "YGZBxia"
# Date: 2017/12/1
'''
61题750行重要
跳过了18页太他妈难了


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


