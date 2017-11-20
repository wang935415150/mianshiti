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
3。如果我们需要根据一个name字段来查询多个表中相关联的数据的时候使用unino联合查询，少使用select多次查询
4。事物：当我做最简单的一个表a加一同时表b减一的动作时候，表a没有加一而表b
    减少了 这样做，会造成数据不安全，而且需要进行两次select，耗资源，事物可以在第一个动作去引导第二个动作进行
5。使用外键：添加关联性，确保相关联的表每条记录都有对应
6。使用索引：对于常用的表中的某一个或多个字段我们可以建立为索引，就可以更快速的索引特定行
7。规避查询的语句：少用含有字段的计算，可以计算完成后在做对比，少用like和通配符，
8。减少mysql进行的字符转换

http://www.jb51.net/article/18934.htm
'''

#2web开发中session和cookie的作用和区别：
'''
cookie可以保存4kb以下的数据信息，保存在浏览器中，通过key，value的方式进行保存，主要用来做身份认证的信息的保存工作
session可以保存4kb以上的数据信息，保存在服务器端，和浏览器当中的cookie做对应使用，也是通过key，value的方式使用。

他们都是用来存储用户的登陆认证信息：通常情况下：cookie会存储一个键值对其中的值对应着服务器上session的key，而session上的值是用户的更多的一部分信息，但是现在都会存储更多的信息，在cookie上只存session的key
'''

#3web开发过程有哪些结束手段防止sql注入

'''

http://www.jb51.net/article/106744.htm
原因：



'''
import pymysql
class Database():
    host='localhost'
    user='root'
    pwd='pwd'
    db='db'
    charset='utf8'
    def __init__(self):
        self.conn=pymysql.connect(host=self.host,username=self.user,passwd=self.pwd,db=self.db,charset=self.charset)
        self.cursor=self.conn.cursor()
    def insert(self,query):
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()


