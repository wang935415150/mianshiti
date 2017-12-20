#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "YGZBxia"
# Date: 2017/12/19
#1.请列举 python2 与 python3 的区别，请将下面的 python2 代码转换成python3。
# from operator import attrgetter
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return '({}, {})'.format(self.x, self.y)
# points = [Point(9, 2), Point(1, 5), Point(2, 7), Point(3, 8), Point(2, 5)]
# c=sorted(points,key=attrgetter('x','y'))
# print(', '.join(map(str, c)))

#2请用 python 写一个正则表达式实现电话号码的 取功能，下面是需要满足条 件:
'''
a. 匹配(123)-456-7890和123-456-7890
b. 不匹配(123-456-7890和123)-456-7890
'''
# \(\d{3}\)|\d{3}-\d{3}-\d{4}

#3改成能够使用多个cpu的
'''
import os
import sys
from concurrent.futures import ProcessPoolExecutor
pool=ProcessPoolExecutor(max_workers=4)
def dump_file(input_dir):
    if not os.path.exists(input_dir):
        return print('dir {} not exists'.format(input_dir))
    path_list = [os.path.join(input_dir, f).strip('\n') for f in os.listdir(input_dir)]
    file_path_list = filter(lambda file_path: os.path.isfile(file_path),path_list)
    return file_path_list
def print_info(file_path):
    print('{}:{} size:{}'.format(os.getpid(), file_path, os.path.getsize(file_path)))
    return
if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_path_list=dump_file(sys.argv[1])
    else:
        file_path_list=dump_file(os.getcwd())
    for file_path in file_path_list:
        a=pool.submit(print_info,file_path)
        a.result()
'''
##找出当前目录下 2 天内新创建的所有 json 文件。

# find -name '*.zip' -ctime -48

#如何查看(监控)CPU 使用情况，硬盘读写情况以及网络读写情况?
'''top查看监视器
ps查看某一个
'''