#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "yiguozhubuxia"
# Date: 2017/11/14
'''
python的堆栈一般是指栈，
栈又分成栈和队列

1.栈是一只能通过访问其一端来实现数据储存与检索的线性数据结构，具有后进先出的特征
    英文名称（last in first out ，LIFO）
2.队列（queue）是一种具有先进后出的特征的线性数据结构，元素的增加只能在一端进行，元素的删除只能在另一端进行
    能够增加元素的队列一端称为队尾，可以删除元素的队列一端则称为队首。
     http://docs.python.org/2/tutorial/datastructures.html#more-on-lists

    下面是官方的一端代码
'''

'''

#关于栈
stack = [3,4,5]
stack.append(6)
stack.append(7)
print(stack)#[3, 4, 5, 6, 7]
print(stack.pop())#7
print(stack.pop())#6
print(stack.pop())#5

#关于队列
from collections import deque
queue=deque(['one','two','three'])
print(queue)#deque(['one', 'two', 'three'])

queue.append('four')
queue.append('five')
print(queue.popleft())#one
print(queue.popleft())#two
print(queue)#deque(['three', 'four', 'five'])

'''
maze = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,1,0,0,0,1,0,1],
    [1,0,0,0,0,1,1,0,0,1],
    [1,0,1,1,1,0,0,0,0,1],
    [1,0,0,0,1,0,0,0,0,1],
    [1,0,1,0,0,0,1,0,0,1],
    [1,0,1,1,1,0,1,1,0,1],
    [1,1,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1]
]
#通过栈的方式实现迷宫
#1。在一个节点通过左右下上的四个方向进行探查，
#2。从一个节点开始，任意找下一个能走都的点，如果走不了就退回来
#3。创建一个空的栈，先将入口的位置进站，寻找一下可走的相邻方块，如果都走不通就回溯
dirs = [lambda x,y:(x+1,y),lambda x,y:(x-1,y),lambda x,y:(x,y-1),lambda x,y:(x,y+1)]

def mgpath(x1,y1,x2,y2):
    stack=[]
    stack.append((x1,y1))
    while len(stack)>0:
        curNode = stack[-1]
        if curNode[0] == x2 and curNode[1]:
            for p in stack:
                print(p)
            break
        for dir in dirs:
            nextNode = dir(*curNode)
            if maze[nextNode[0]][nextNode[1]]==0 :
                stack.append(nextNode)
                maze[nextNode[0]][nextNode[1]]=-1
                break
            else:
                maze[curNode[0]][curNode[1]]=-1
                stack.pop()
    return False

mgpath(1,1,8,8)