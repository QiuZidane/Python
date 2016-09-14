from utils import *
import matplotlib.pyplot as plt

"""
1、输入要素:
    投资年数
    年投资利率
    投资开始前流动资金: amt1
    在投资金:amt2
    卖金碧房收入:amt3
2、方式A:买楼后,每年拿出amt4供楼
3、方式B:不买楼
"""

firstpay = 200
years = 15
lifecost = 5
data1 = calAB(years, firstpay, lifecost)
fundA200 = data1[0]
fundB = data1[1]
yearlist = data1[2]
print('方式A资金池:' + str(fundA200))
print('方式B资金池:' + str(fundB))
# print(yearlist)

fundA250 = calAB(years, 250, lifecost)[0]
fundA300 = calAB(years, 300, lifecost)[0]
fundA400 = calAB(years, 400, lifecost)[0]
fundA500 = calAB(years, 500, lifecost)[0]

plt.plot(yearlist, fundA200, c='blue', linewidth=2)
plt.plot(yearlist, fundA250, c='purple', linewidth=2)
plt.plot(yearlist, fundA300, c='green', linewidth=2)
plt.plot(yearlist, fundA400, c='yellow', linewidth=2)
plt.plot(yearlist, fundA500, c='black', linewidth=2)
plt.plot(yearlist, fundB, c='red', linewidth=4)
title = '''
年利率10%
蓝色:首付 200万
紫色:首付 250万
绿色:首付 300万
黄色:首付 400万
黑色:首付 500万
红色:不买房的方案
'''
plt.title(title, fontsize=13)
plt.xlabel('年份', fontsize=13)
plt.ylabel('资金总量(单位:万)', fontsize=13)
plt.show()
