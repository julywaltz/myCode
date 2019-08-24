#!/usr/bin/env python
# -*- coding=utf-8 -*-

# @Author: Cheng Yili
# @Date: 2019-08-08 21:39:12
# @LastEditors: Cheng Yili
# @LastEditTime: 2019-08-08 21:47:26
# @Email: julywaltz77@hotmail.com
import numpy as np

points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)
print(xs, ys)
