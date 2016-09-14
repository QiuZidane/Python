from utils import *
import matplotlib.pyplot as plt
# import csv
# from jdcal import *
# from et_xmlfile import *
# from openpyxl import *
import xlrd

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

firstpay = 150
years = 25
lifecost = 6
data1 = calAB2(years, firstpay, lifecost)
fundA150 = data1[0]
fundB = data1[1]
yearlist = data1[2]
print('方式A资金池:' + str(fundA150))
# print('方式B资金池:' + str(fundB))
# print(yearlist)

fundA200 = calAB2(years, 200, lifecost)[0]
fundA250 = calAB2(years, 250, lifecost)[0]
fundA300 = calAB2(years, 300, lifecost)[0]

plt.plot(yearlist, fundA150, c='blue', linewidth=2)
# plt.plot(yearlist, fundA200, c='purple', linewidth=2)
# plt.plot(yearlist, fundA250, c='green', linewidth=2)
# plt.plot(yearlist, fundA300, c='green', linewidth=2)
# plt.plot(yearlist, fundB, c='red', linewidth=4)
title = '''
年利率10%
蓝色:首付 150万
紫色:首付 200万
绿色:首付 250万
黄色:首付 300万
红色:不买房的方案
'''
plt.title(title, fontsize=13)
plt.xlabel('年份', fontsize=13)
plt.ylabel('资金总量(单位:万)', fontsize=13)
# plt.show()

exceldata = xlrd.open_workbook('home1.xlsx')
table = exceldata.sheet_by_index(0)
cell_A1 = table.cell(0, 0).value
print(cell_A1)
