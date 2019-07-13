#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-07-13 20:47:20
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-07-13 22:11:51
# @Email: julywaltz77@hotmail.com

import numpy as np
arr = np.arange(10)
print(arr)
print(arr[5])
print(arr[1:2])
temp = arr[2:3]
temp[0] = 0
print(temp)
print(arr)
temp = arr[:].copy()
print(temp)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[0][2])
print(arr2d[0, 2])

print(arr2d[:2])
print(arr2d[:2, 1:])
"""
布尔索引
"""
names = np.array(['cheng', 'tang', 'zeng', 'cheng', 'zhang'])
data = np.random.randn(5, 3)
print(names)
print(data)
print(names == 'cheng')
print(data[names == 'cheng'])
"""
神奇索引
"""
arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i

print(arr)
print(arr[[4, 3, 0, 6]])
print(arr[[-5, -2, -7]])
print(arr[[1,5,3],[1,2,3]])
