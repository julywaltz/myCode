#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-07-12 20:54:26
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-07-12 21:58:28
# @Email: julywaltz77@hotmail.com
"""
1.ndarray对象创建
"""
"""
ndarry：大数据集容器
ndarry是一个通用的多维同类数据容器，它包含的每一个元素均为同类型
用list创建一维ndarray对象
"""
import numpy as np

data = [1, 2, 11, 4, 59]
arr = np.array(data)  # 生成数组
print(arr)
print(type(arr))
"""
向量到list类型转换
"""
arr = np.arange(8)
L = arr.tolist()
print(type(L))
print(L)
"""
嵌套列表构建ndarry多维数组
同等长度的列表将会自动转换为多维数组
"""
data = [[1, 2, 3, 4], [5, 6, 7, 8.2]]
arr = np.array(data)
print(arr)
print(arr.ndim)  # 数组的维度
print(arr.shape)  # 每一维度的数量
print(arr.dtype)  # 数组的数据类型
print(type(arr))
"""
zeros创建给定长度及形状的全0数组
zeros_like 根据所给数组生成一个形状一样的全0数组
ones创作全1数组
ones_like根据所给数组生成一个形状一样的全1数组
empty可以创建一个没用初始化数值的数组
empty_like同上
full 根据给定的形状和数据生成指定数值的数组
full_like同上
想要创建高维数组，需要未shape传递一个元组
"""
arr0 = np.zeros(10)
print(arr0)
arr1 = np.ones(10)
print(arr1)
arr1_2 = np.ones((10, 2))
print(arr1_2)
arr_empty = np.empty((2, 3, 2))
print(arr_empty)
"""
arrange 是range的数组版

"""
"""
生成网格数据
"""
arr = np.linspace(0, 80, 5)  #指定起始点和终止点（包含），以及网格点的个数
print(arr)
