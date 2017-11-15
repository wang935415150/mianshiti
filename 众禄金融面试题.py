#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "yiguozhubuxia"
# Date: 2017/11/14
'''
#1请写出下面代码的输出结果：
class Parent():
    x=1
class Child1(Parent):
    pass
class Child2(Parent):
    pass

print(Parent.x,Child1.x,Child2.x)
#自己想的：1，1，1'
#答案:1 1 1
Child1.x=2
print(Parent.x,Child1.x,Child2.x)
#自己想的1，2，1
#结果1 2 1原因是子类不可以修改父类
Child1.x=3
print(Parent.x,Child1.x,Child2.x)
#结果1 3 1

'''
#====================

'''
#2请写出下面代码的输出结果
a =1
def fun(a):
    a=2
fun(a)
print(a)
#自己想的 2
#结果是1
a=[]
def fun(a):
    a.append(1)
fun(a)
print(a)
#空
#正确结果是[1]
'''

#===============
#3如何判断一个邮箱是否合法

#我们可以通过内置的re正则模块进行匹配，来得到一个合法的模块


#4 请实现一个装饰器，限制该函数被调用的频率，如10秒一次


'''
import time
def winner(func):
    b = [0,]
    def inner(*args,**kwargs):
        import time
        a=time.time()
        if a-b[0]==a and a-b[0]>10:
            c=func(*args,**kwargs)
            b[0]=a
        else:
            b[0]=a
            return 'time is no'
        return c
    return inner
@winner
def x():
    print('x')

x()
print('one')
time.sleep(3)
x()
print('two')
time.sleep(11)
print('three')
x()

'''

#5 请说一说lambda函数的作用，请用lambda和reduce实现1到100的累加
'''
lamdba函数又叫做匿名函数，他的好处是，不污染名称空间，因为它没有名字，
还可以和map，zip等内置函数进行联合使用，
他没有名字，他只是一个表达式
最常用的一个作用就是，我想用函数的return功能但我不想定义一个def函数

from functools import reduce
he=reduce(lambda x,y:x+y,[i for i in range(1,101)])
print(he)
'''

'''
#7请说明一下classmethod和staticmethod的区别
classmethod:类方法
staticmethod:静态方法
在python中，静态方法和类方法都是可以通过类对象和类对象实例进行访问的，但是区别在于
区别：
    1。@classmethod是一个函数修饰符或者通知，他表示接下来的一个类方法，而我们平常实用的大多是实例方法，
    类方法的第一个参数是cls就是类本身，而实例方法传入的第一个参数是self也就是实例化后的对象
    2。普通对象方法至少需要一个self参数，他是类的对象
    3。类方法有变量cls传入，从而可以用cls做一些相关的处理，如果有一个子类继承了他，那么传入进去的cls就是
    子类，调用的方式就是C.f()。
    4。静态方法则没有，他基本上跟一个全局函数相同，只是在这个类的文件被导入之后可以不用在本文件中在写一个静态方法了
    很少用

class Aclass():
    @staticmethod
    def staticfunc():
        print('this is static')

    def normafunc(self):
        print('this is norma',self)

    @classmethod
    def classfunc(cls):
        print('this is class func',cls)
a1=Aclass()

a1.normafunc()#this is norma <__main__.Aclass object at 0x102223320>

Aclass.classfunc()#this is class func <class '__main__.Aclass'>

a1.staticfunc()#this is static

'''
'''
#8请说明迭代器与生成器的理解
先说迭代器
迭代器可以被__next__或者next()的对象（python一切皆对象）
任何含有__next__方法的对象都可以称为迭代器
迭代器可以减少内存的占用因为他是通过next方法取值而不是通过

再说生成器
    任何一个含有yeild的函数都是生成器，生成器本质上也是一个迭代器

他俩的共同点就是都能通过for循环来进行迭代

用生成器写一个斐波那契

def fib(n):
    one,nex=0,1
    while n>0:
        n-=1
        yield nex
        one,nex=nex,nex+one
print([ i for i in fib(10)])

'''