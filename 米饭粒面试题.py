# -*- coding: utf-8 -*-
# __author__ = "maple"

# 1、下面代码的输出结果是什么，请解释。

def extend_list(val, list=[]):
    list.append(val)
    return list


list1 = extend_list(10)
list2 = extend_list(123, [])
list3 = extend_list('a')

print(list1)
print(list2)
print(list3)

print(list1 is list3)

"""
依次输出：
[10, ‘a’]
[123]
[10, ‘a’]
True
因为list1和list3调用函数extend_list时，没有传入list关键字参数，使用了函数初始化的list。
返回给list1和list3的都是初始化list的地址，所以值相同。

注：打印位置不同结果不同
调用一次函数，打印一次结果的话：
依次输出
[10]
[123]
[10, ‘a’]

"""


# 2、类的继承
# 下面代码的输出结果是什么，请解释。
class Parent(object):
    x = 1


class Child1(Parent):
    pass


class Child2(Parent):
    pass


print(Parent.x, Child1.x, Child2.x)
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)

'''
依次输出：
1 1 1
1 2 1
3 2 3
因为，Child1、Child2都继承Parent类。
第一次都输出Parent的x值，为1。
第二次，Child1拥有自己的属性x=2,他的输出变为2。
第三次，Parent的属性x被赋值为3。不改变Child1自己的属性x。'''


# 3、冒泡排序

# 1. 冒泡排序
#   原理：从索引为0的位置开始，比较索引0和1的值的大小，索引0的值大，则互换位置。再比较索引1和2的值，一趟下来，最大值换到末尾，再从头比较。
#   i: 趟
#   j: 指针位置
#   时间复杂度：O（n2）


def bubble_sort(li):
    for i in range(len(li) - 1):
        for j in range(len(li) - 1 - i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


# li = [12, 3, 4, 5, 3, 6, 7]
# bubble_sort(li)
# print(li)


# 冒泡优化
# 执行一趟没有交换，则说明列表有序，结束排序

def bubble_sort_op(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - 1 - i):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            return


# 4、打印文件夹中文件的路径以及包含文件夹中文件的路径（不让使用os.walk）

# 标准答案
def print_directory_contents(sPath):
    import os

    for sChild in os.listdir(sPath):
        sChildPath = os.path.join(sPath, sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)


# 使用os.walk
def print_directory_contents(sPath):
    import os
    for root, _, filenames in os.walk(sPath):
        for filename in filenames:
            print(os.path.abspath(os.path.join(root, filename)))


# 5、有n个台阶，可以一次走上1个阶台，2个台阶，3个台阶。请问n个台阶，有几种走法。

def func(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 3
    return func(n - 1) + func(n - 2) + func(n - 3)


print(func(4))
