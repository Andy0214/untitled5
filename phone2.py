# -*- coding:utf-8 -*-
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# author = "Andy"
# Date: 2018/7/23

from phone import Phone
import xlrd
import xlwt


def Get_Excel_data():
    file = './Tel.xlsx'   #电话号码存储的excle表
    re1 = xlrd.open_workbook(file)

    outwb = xlwt.Workbook() #创建工作簿
    # print(type(outwb))
    outws = outwb.add_sheet("new")  #在工作簿中新建一个工作表new
    # print(type(outws))

    # 读取第一个sheet
    ws = re1.sheet_by_index(0)
    rows = ws.nrows
    # print(rows)
    outws.write(0, 0, u'电话号')  #给新表的第一行添加对应的标签
    outws.write(0, 1, u'省份')
    outws.write(0, 2, u'城市')
    outws.write(0, 3, u'区号')
    outws.write(0, 4, u'运营商')

    for i in range(0, rows):
        Telvalue = int(ws.cell_value(i, 0))
        # print(Telvalue)
        data = Phone().find(Telvalue)
        print(data)
        outws.write(i + 1, 0, Telvalue)  #给新表的个列添加对应的数据
        try:
            outws.write(i + 1, 1, data['province'])
            outws.write(i + 1, 2, data['city'])
            outws.write(i + 1, 3, data['area_code'])
            outws.write(i + 1, 4, data['phone_type'])

            outwb.save(r'New_Tel.xls')
        except:
            print("none")

Get_Excel_data()