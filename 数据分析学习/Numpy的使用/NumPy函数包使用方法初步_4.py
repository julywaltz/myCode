#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-07-14 20:48:45
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-08-08 21:36:06
# @Email: julywaltz77@hotmail.com
import numpy as np
"""通用函数"""
"""在nadarray数据中逐元素操作的函数"""
arr = np.arange(10)
print(arr)

print(np.sqrt(arr))
print(np.exp(arr))
x = np.random.randn(8)
y = np.random.randn(8)
print(x)
print(y)
print(np.maximum(x, y))  #maximum逐元素将下，y最大值计算出来

remainder, whole_part = np.modf(x)  #modf 返回浮点数组的整数部分和小数部分
print(remainder)
print(whole_part)
