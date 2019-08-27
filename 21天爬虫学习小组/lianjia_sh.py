#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-08-27 22:16:58
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-08-27 23:08:14
# @Email: julywaltz77@hotmail.com

import requests
from bs4 import BeautifulSoup
import os
import csv


def main():
    print('开始获取信息')
    house_infos = []
    for page in range(10):
        url = 'https://sh.lianjia.com/zufang/pg{}/#contentList'.format(page)
        ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        headers = {'User-Agent': ua}
        res = requests.get(url, headers=headers)
        html = res.text
        soup = BeautifulSoup(html, 'lxml')
        info_list = soup.find_all('div', class_='content__list--item--main')
        for info in info_list:
            title = info.find('a', target='_blank').get_text().strip().replace(
                ' ', ',')
            info_1 = info.find(
                'p', class_='content__list--item--des').get_text().split('/')
            address = info_1[0].strip()
            area = info_1[1].strip()
            house_type = info_1[3].strip()
            house_link = info.find('a', target='_blank').get('href')
            house_link = 'https://sh.lianjia.com' + house_link
            price = info.find('span',
                              class_='content__list--item-price').get_text()
            house_info = [title, address, area, house_type, house_link, price]
            house_infos.append(house_info)
    os.makedirs('./lianjia/', exist_ok=True)
    head_row = ['标题', '地址', '面积', '户型', '链接', '价格']
    print('信息获取完成，开始写入')
    with open('./lianjia/lianjia.csv', 'w', encoding='gbk',
              newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(head_row)
        for row in house_infos:
            print(row)
            writer.writerow(row)
    print('写入完成')


if __name__ == "__main__":
    main()
