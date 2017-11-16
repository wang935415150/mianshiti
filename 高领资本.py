#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "Q1mi"
# Date: 2017/11/15

#1mysql有哪些储存引擎，优化mysql数据库的方法有哪些

'''
ISMA：最古老的引擎
MYISMA：mysql版本的isma引擎
HEAP：追求速度但是需要在关机前进行保存操作
innoDB：mysql创造了innodb同时innodb也造就了mysql，也是mysql发展起来的重要引擎，通过mysql+api的方式处理数据，mysql下支持外键和事务处理的引擎
'''

'''
mysql的优化方法：
1。字段选择：尽量使用char 并切尽量缩小字段长度。不常用的字段使用varchar
2。查询方法：尽量使用join链表少使用复合查询 因为复合查询复杂度高，而且在查询过程中需要在内存中建立临时表来完成多步骤逻辑操作
3。如果我们需要根据一个name字段来查询多个表中相关联的数据的时候使用unino联合查询，少使用多个select

'''