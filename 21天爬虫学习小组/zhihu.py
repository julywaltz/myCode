#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-08-26 21:47:41
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-08-26 23:46:56
# @Email: julywaltz77@hotmail.com

import requests
import os
import csv
print('开始获取数据')
url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend'
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
cookie = '_zap=032582cd-a6fb-400f-aa69-3c4f75bc3b42; _xsrf=JKTjLiqCYJI7m83ZB9LoF38pgemDF2aC; d_c0="AKBpR4r5gA-PTrJ7tUCkgAWY9Xy1cAy-FJY=|1559133387"; q_c1=c61eb70eaa3f449c9c7462740e54ec70|1559139366000|1559139366000; z_c0="2|1:0|10:1560693748|4:z_c0|92:Mi4xRkx3RUFBQUFBQUFBb0dsSGl2bUFEeVlBQUFCZ0FsVk45Sm56WFFBOGs0Yk5vU05rS0VLcnQzUWZqcUdsVy1kR1pB|962d5c99be04b3a8f49a44d1ab3d2ec75dd402bf6e6e703a954a02fbc47e468a"; __gads=ID=72c0781bc46d60ab:T=1561381048:S=ALNI_MawNgXPTSvpZuPk0_i-6NqmE-hOsw; tgw_l7_route=060f637cd101836814f6c53316f73463; tst=r'
headers = {'User-Agent': ua, 'cookie': cookie}
page_number = 2
after_id = 5
rows = []
for i in range(100):
    params = {
        'session_token': '1862c36c5a6f845560b9de85195ca70d',
        'desktop': 'true',
        'page_number': page_number,
        'limit': 6,
        'action': 'down',
        'after_id': after_id
    }
    session = requests.Session()
    with session:
        res = session.get(url, headers=headers, params=params)
        data = res.json()['data']
        head_row = list(data[0].keys())
        for i in range(len(data)):
            row = []
            for key in head_row:
                row.append(data[i][key])
            rows.append(row)
    print(page_number)
    page_number = page_number + 1
    after_id = after_id + 6
print('数据获取完成，写入csv文件中')
os.makedirs('./zhihu/', exist_ok=True)
with open('./zhihu/zhihu.csv', 'w', encoding='gbk', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(head_row)
    for i in range(len(rows)):
        try:
            writer.writerow(rows[i])
        except:
            pass
print('写入完成')