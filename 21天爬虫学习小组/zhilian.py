#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-08-28 21:58:49
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-08-29 00:20:49
# @Email: julywaltz77@hotmail.com

import requests
from bs4 import BeautifulSoup
import csv
import os
from time import sleep

os.makedirs('./zhilian/', exist_ok=True)
if 'zhilian.csv' in os.listdir('./zhilian/'):
    os.remove('./zhilian/zhilian.csv')
head_row = [
    '岗位名称', '招聘公司', '公司类型', '公司规模', '工作地点', '岗位类型', '经验要求', '学历要求', '是否全职',
    '薪资待遇', '岗位链接', '岗位描述'
]
with open('./zhilian/zhilian.csv', 'a', encoding='utf8',
          newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(head_row)
url = 'https://fe-api.zhaopin.com/c/i/sou'
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
headers = {'User-Agent': ua}
for i in range(1, 13):
    params = {
        'pageSize': 90 * i,
        'cityId': 801,
        'salary': '0,0',
        'workExperience': -1,
        'education': -1,
        'companyType': -1,
        'employmentType': -1,
        'jobWelfareTag': -1,
        'kw': 'python',
        'kt': 3,
        '': 0,
        '_v': 0.68042711,
        'x-zp-page-request-id':
        '8c426580c1234349aced9df0dab80ea5-1567001204159-7609',
        'x-zp-client-id': '6899ebf4-0904-4db9-90e2-37bec1312fac'
    }
    res = requests.get(url, headers=headers, params=params)
    results = res.json()['data']['results']
    print(params['pageSize'])
    rows = []
    print(rows)
    for r in results:
        job_name = r['jobName']
        company = r['company']
        company_name = company['name']
        company_type = company['type']['name']
        company_size = company['size']['name']
        city = r['city']['items'][0]['name']
        job_type = r['jobType']['items'][0]['name']
        work_exp = r['workingExp']['name']
        edu_level = r['eduLevel']
        emp_type = r['emplType']
        salary = r['salary']
        pos_url = r['positionURL']
        row = [
            job_name, company_name, company_type, company_size, city, job_type,
            work_exp, edu_level, emp_type, salary, pos_url
        ]
        rows.append(row)
    print(rows)
    for row in rows:
        pos_url = row[-1]
        print(pos_url)
        sleep(5)
        pos_res = requests.get(pos_url, headers=headers)
        pos_html = pos_res.text
        soup = BeautifulSoup(pos_html, 'lxml')
        des_jobs = soup.find_all(attrs={"class": "describtion"})
        for des_job in des_jobs:
            des_text = des_job.text
            row.append(des_text)
        print(row)
    print('开始写入')
    with open('./zhilian/zhilian.csv', 'a', encoding='utf8',
              newline='') as csvfile:
        writer = csv.writer(csvfile)
        for row in rows:
            writer.writerow(row)
    print('写入完成')
print('全部写入完成')