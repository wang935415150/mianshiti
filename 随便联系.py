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
for n in range(2, 100000000000000000000):
    for x in range(2, n+1):
        if n % x == 0 and n/x!=1:
            # print(n, '等于', x, '*', n // x)
            break
    else:
        print(n, ' 是质数')