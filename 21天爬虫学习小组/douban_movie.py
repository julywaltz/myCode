#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-08-24 21:14:35
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-08-31 19:42:05
# @Email: julywaltz77@hotmail.com

import requests
import os
import csv
from time import sleep


def main_program():
    """创建文件夹"""
    all_movies = []
    dir_path = os.path.split(os.path.realpath(__file__))[0] + '/douban'
    if os.path.exists(dir_path):
        pass
    else:
        os.mkdir(dir_path)
    """下载电影信息、图片"""
    for i in range(0, 250, 20):
        url = 'https://api.douban.com/v2/movie/top250?start={}&apikey=0df993c66c0c636e29ecbb5344252a4a'.format(
            i)
        res = requests.get(url)
        for movie_info in res.json()["subjects"]:
            """id"""
            movie_id = movie_info['id']
            """电影名"""
            title = movie_info['title']
            """主演"""
            casts = []
            for key in movie_info['casts']:
                casts.append(key['name'])
            casts = ','.join(casts)
            """上映年份"""
            year = movie_info['year']
            """评分"""
            rating = movie_info['rating']['average']
            """海报地址"""
            image_url = movie_info['images']['large']
            """下载海报图片"""
            image_name = dir_path + '/' + title + '.jpg'
            if os.path.exists(image_name):
                print(title + '图片已存在')
            else:
                print('下载' + title + '海报ing')
                res = requests.get(image_url)
                with open(image_name, 'wb') as f:
                    f.write(res.content)
                print('下载完成')
            line = [movie_id, title, casts, year, rating, image_url]
            all_movies.append(line)
            sleep(0.2)
    """根据评分排序"""
    all_movies.sort(key=lambda x: x[4])
    all_movies.reverse()
    """写入csv"""
    print('写入csv文件')
    file_path = os.path.split(
        os.path.realpath(__file__))[0] + '/douban/douban_movie.csv'
    if os.path.exists(file_path):
        os.remove(file_path)
    with open(file_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['id', '电影名', '主演', '上映年份', '豆瓣评分', '海报下载地址'])
        for line in all_movies:
            writer.writerow(line)
    print('写入结束')


if __name__ == 'main':
    main_program()
