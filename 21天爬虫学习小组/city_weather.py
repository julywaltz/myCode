#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-08-23 19:56:26
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-08-24 21:05:51
# @Email: julywaltz77@hotmail.com

import requests

f = True

while f:
  url = 'http://wthrcdn.etouch.cn/weather_mini?city='
  city = input('请输入城市，回车退出：')
  if len(city) != 0:
    url = url + city
    res = requests.get(url)
    if res.json()['status'] == 1000:
      info = res.json()['data']['forecast'][0]
      print(city)
      print(info['date'])
      print(info['high'])
      print(info['low'])
      print(info['type'])
    else:
      print(city)
      print('未获得')
  else:
    f = False
