#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "YGZBxia"
# Date: 2017/11/26

#1python中基本的数据结构的操作

'''
#元祖
tu=tuple(1,2,3)
#列表
li=list(1,2,3,4)
li.append(6)
li[1]=3
li.remove(3)
li.pop(3)
#字典
dic={'a':1,'b':2}
dic['c']=3
dic['a']=4
dic.pop('a')
dic.popitem()#随机删除一组
'''

#2

'''
# （1）请尽可能的例举 a=[1,2,3,4,5],a[::2]=?,a[-2:]=?
a=[1,2,3,4,5]
a[::2]#步长为2结果就是1,3,5
a[-2:]#从最后一个开始数结果是4，5,这是不一样的因为之后-1么有-0的索引方式
#（2）一行代码实现队列表a中的偶数位置的元素进行加3后求和
a=[1,2,3,4,5,6]

c=sum(map(lambda x:x+3,a[::2]))
print(c)
'''

#3
'''
将这个列表从大到小排列
li=[-2,1,3,-6]
def absfull(li):
    for  i in range(len(li)-1):
        for j in range(len(li)-1-i):
            if abs(li[j])>abs(li[j+1]):
                li[j],li[j+1]=li[j+1],li[j]
    return li
print(absfull(li))

……#######################
sort排序和sorted的区别
a=[1,2,6,2,3,8,12,3]
a.sort()#是直接修改了原来的列表返回值是None
sorted(a)#不修改原来的列表，返回一个新的列表
'''

#4统计一个文本a.txt中的单词数量并且返回其中最高的是个
dic=dict()
with open('a.txt','r',encoding='utf-8') as f:
    a=f.read()
    for i in a:
        c=a.count(i)
        dic[i]=c
    f=zip(dic.values(),dic.keys())
    f=sorted(f)
    print(f[-10:])



