#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "YGZBxia"
# Date: 2017/12/1

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

