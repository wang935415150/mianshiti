#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "YGZBxia"
# Date: 2017/12/25


# n=5
# def foo(n):
#     res=map(lambda x:bin(x)[2:].count('1'),[i for i in range(n+1)])
#     return list(res)
# print(foo(n))
#
# # 匹配 可乐500ml中的500ml
# import re
# c=re.findall(r'\d+[mM]?[lL]','可乐500ml')
#
# print(c)
#

#求1-1000000的质数
# for n in range(2, 100000000000000000000):
#     for x in range(2, n+1):
#         if n % x == 0 and n/x!=1:
#             # print(n, '等于', x, '*', n // x)
#             break
#     else:
#         print(n, ' 是质数')

def test_1():
    func_array=[]
    for i in range(10):
        def func():
            print(i)
        func_array.append(func)
    func_array[0]()
    func_array[9]()
def test_2():
    func_array=[]
    for i in range(10):
        def func(i):
            def wrap():
                print(i)
            return wrap
        func_array.append(func(i))
    func_array[0]()
    func_array[9]()
print('test1')
test_1()
print('test2')
test_2()