# -*- coding: utf-8 -*-


# print("hello")
# print(100 + 100)
# print('hi', 'i', 'am tom cat', 100)
# print('hi  i am tom cat', '1')
# # name = input('请输入名字:')
# # # print(name)
# # if name == "zidane":
# #     print("没错")
# # else:
# #     print("错了")
# print('''1
# line1
# line2
# line3
# 2''')
#
# s4 = r'''Hello,,,,
# World,,,!'''
# print(s4)
# print(2**100)
# print('hello %s %f' %('zidane',100))
#
# *****************************
# ******** list和tuple ********
# *****************************
#
# classmates = ['AA','BB']
# print(classmates[-2])
# print(len(classmates))
# classmates.append('CC')
# classmates.insert(1,'YY')
# print(classmates)
# p = ['asp', 'php']
# s = ['python', 'java', p, 'scheme']
# print(s[2][0])
# tuple1 = ('A', 'B', ['AA', 'BB'])
# tuple1[2].append('CC')
# print(tuple1)
#
#
#
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(L[0][0])
# print(L[1][1])
# print(L[2][-1])
#
# i=list(range(10))
# print(i)
#
# i=100
# if i > 100 :
#     print('123')
# elif i <50 :
#     print('222')
# else:
#     print('333')
#
# ss = '110'
# a = int(ss)
# if a == 100:
#     print('=100')
# else:
#     print("not = 100")
#
#
# *****************************
#              循环
# *****************************
#
# names = ['zidane',
#          'even',
#          'qxy',
#          'ljj'
#          ]
# for name in names:
#     print(name)
#
# sum = 0
# for x in list(range(3)):
#     sum += x
# print("x =",x)
# print("sum =",sum)
#
# L = ['Bart', 'Lisa', 'Adam']
# for name in L:
#     print("HELLO,", name, "!")
#     print("HELLO, %s !"%name)
#
# *****************************
#          字典  dictionary
#          集合  set
# *****************************
# dict1 = {"zidane":34 ,"even":30}
# if "zidane1" in dict1:
#     print(dict1["zidane"])  #34
# else:
#     print("key not find!")
#
# value1 = dict1.get("zidane1",-1)#没有自定义返回值则返回None
# value2 = dict1.get("zidane",-2) #自定义返回值
# print(value1) #-1
# print(value2) #34
# dict1.pop("zidane") #删除键值对
# print(dict1)
# dict1["zidane"] = 33 #增加键值对
# print(dict1)
#
# set1 = set([1,2,"zidane"])
# print(set1)
# set1.add(3)
# print(set1)
# set1.remove("zidane")
# print(set1)
#
# str = "zidanezidanezidane"
# str2 = str.replace("z","Z",2)
# print(str2)
#
# t1 = (1,2,3)
# t2 = (1,2,[1,2])
# dict2 = {"key":t1}
# dict2 = {t1:"value"}
# # dict2 = {t1}
# set2 = set(t1)
# # dict2 = {t2} #错误:key要为不可变元素[1,2]list是可变的
# # set2 = set(t2) #错误:key要为不可变元素[1,2]list是可变的
# print(dict2[t1])

# *****************************
#           函数
# *****************************
# n1 = 255
# n2 = 1000
# n3 = hex(n1)
# print(str(n3))
# print(hex(n2),str(n3))
#
# def my_abs(x):
#     if x >= 0:
#         return x*x
#     else:
#         return -x*-x
#
# print(my_abs(-9))
#
# import math
# def quadratic(a, b, c):
#     delta = b*b - 4*a*c
#     __delta = math.sqrt(delta)
#     x1 = (-b + __delta) / 2*a
#     x2 = (-b - __delta) / 2*a
#     print("x1 = ",str(x1));
#     print("x2 = ",str(x2));
# quadratic(2,3,1)
# quadratic(1,3,1)
#
# list1 = [1,2,[1,2],'A',True]
# print(list1)
#
# 字符串
# name = "zidane"
# print(name[1:-1])

##可变参数
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return print(sum)
# nums = (1,2,3)
# calc(*nums)

# list1 = ['a', 'b', 'c']
# list2 = sorted(list1, reverse=True)
# print(list2)
# names = [1, 2, 3, 4]
# list2 = sorted(names)


'''

模块的用法

'''
# import module1
import module1 as m1
# from module1 import func2
from module1 import func2 as f2
from module1 import *

# module1.func1();
m1.func1()
# func2();
f2()
func1()

'''

可以访问条件语句中的值

'''
value = '123'
if True:
    value = 1
else:
    value = 2
print(value)

