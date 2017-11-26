#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "YGZBxia"
# Date: 2017/11/26

#1python中基本的数据结构的操作
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