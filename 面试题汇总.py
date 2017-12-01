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





