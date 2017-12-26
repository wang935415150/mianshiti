#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "YGZBxia"
# Date: 2017/12/25


n=5
def foo(n):
    res=map(lambda x:bin(x)[2:].count('1'),[i for i in range(n+1)])
    return list(res)
print(foo(n))

# 匹配 可乐500ml中的500ml
import re
c=re.findall(r'\d+[mM]?[lL]','可乐500ml')

print(c)
