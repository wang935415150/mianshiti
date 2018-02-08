#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "YGZBxia"
# Date: 2017/12/1

def fun(li):
    if len(li) <=1 :return li
    temp=li[len(li)//2]
    left = [i for i in li if i < temp]
    middel = [i for i in li if i == temp]
    right = [i for i in li if i > temp]
    return fun(left) + middel + fun(right)

def func(li):
    if len(li) <= 1:
        return li
    temp = li[len(li)//2]
    left = [i for i in li if i < temp]
    middel = [i for i in li if i == temp]
    right = [i for i in li if i > temp]
    return func(left) + middel + func(right)

li = [1,2,3,4,13,55,11,23,12]
print(func(li))
# print(fun(li))