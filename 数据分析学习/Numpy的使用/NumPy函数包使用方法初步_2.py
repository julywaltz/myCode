#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-07-12 21:45:09
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-07-13 20:39:55
# @Email: julywaltz77@hotmail.com

import numpy as np
"""
3.简单运算
"""
"""
维度转换

"""
a = np.arange(24).reshape(6, 4)  #生成一个4*6的二维数组

print(a)
"""
将二维数组展平（转换为一个4*6项的一维数组）
"""

print(a.flatten())
"""
将6*4的二维数组转换为3*8的二维数组
"""
a.resize((3, 8))  # resize()方法改变原数组
print(a)
"""
转置
"""
print(a)
print(a.transpose())  # transpose()生成新数组
"""
数组的组合
"""
"""
水平组合
"""
a = np.arange(6).reshape((2, 3))
b = a * 2
print(np.hstack((a, b)))
"""
垂直组合
"""
print(np.vstack((a, b)))
"""

"""
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr * arr)
print(arr - arr)

print(1 / arr)
print(arr**0.5)
arr2 = np.array([[0, 4, 2], [7, 2, 10]])
print(arr2 > arr)
