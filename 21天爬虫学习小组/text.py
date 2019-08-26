#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-08-26 22:47:20
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-08-26 22:48:12
# @Email: julywaltz77@hotmail.com
import requests

url = 'https://www.zhihu.com/api/v3/feed/topstory/recommend'
headers = {
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    'Cookie':
    '_zap=032582cd-a6fb-400f-aa69-3c4f75bc3b42; _xsrf=JKTjLiqCYJI7m83ZB9LoF38pgemDF2aC; d_c0="AKBpR4r5gA-PTrJ7tUCkgAWY9Xy1cAy-FJY=|1559133387"; q_c1=c61eb70eaa3f449c9c7462740e54ec70|1559139366000|1559139366000; z_c0="2|1:0|10:1560693748|4:z_c0|92:Mi4xRkx3RUFBQUFBQUFBb0dsSGl2bUFEeVlBQUFCZ0FsVk45Sm56WFFBOGs0Yk5vU05rS0VLcnQzUWZqcUdsVy1kR1pB|962d5c99be04b3a8f49a44d1ab3d2ec75dd402bf6e6e703a954a02fbc47e468a"; __gads=ID=72c0781bc46d60ab:T=1561381048:S=ALNI_MawNgXPTSvpZuPk0_i-6NqmE-hOsw; tgw_l7_route=060f637cd101836814f6c53316f73463; tst=r'
}

params = {
    'session_token': '1862c36c5a6f845560b9de85195ca70d',
    'desktop': 'true',
    'page_number': 2,
    'limit': 6,
    'action': 'down',
    'after_id': 5
}

req = requests.session()
r = req.get(url, headers=headers, params=params)
if r.status_code == 200:
    data = r.json()
    if data:
        for i in data.get('data'):
            try:
                print(i)
            except Exception as e:
                print('error', e)