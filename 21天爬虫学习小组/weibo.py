#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-08-25 20:38:14
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-08-25 20:48:56
# @Email: julywaltz77@hotmail.com

import requests

url = 'https://weibo.com/a/hot/realtime'

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
cookie = 'SINAGLOBAL=8083744408594.012.1559574507326; UOR=www.mobiletrain.org,widget.weibo.com,www.oldding.net; Ugrow-G0=d52660735d1ea4ed313e0beb68c05fc5; login_sid_t=3ffb08ebf16ad298c1733f3d3e2acf7b; cross_origin_proto=SSL; YF-V5-G0=125128c5d7f9f51f96971f11468b5a3f; WBStorage=f54cf4e4362237da|undefined; _s_tentry=-; Apache=2886603592052.4526.1566736315049; ULV=1566736315936:3:1:1:2886603592052.4526.1566736315049:1559649502759; SUB=_2AkMqPg-Ff8NxqwJRmPAQy2nhboRwyAvEieKcYv5eJRMxHRl-yT83qmgytRB6Ab4haqiR4k8_70iUQJzNQyrVE6OFIGkF; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9W5i4TQFfaRxCeTx_ZbXpgCg'
headers = {'User-Agent': ua, 'cookie': cookie}
res = requests.get(url, headers=headers)
with open('weibo1.html', 'w', encoding='UTF8') as f:
    f.write(res.text)