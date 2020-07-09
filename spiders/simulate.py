# -*- coding: utf-8 -*-
"""
@author: xiaoke
@file: simulate.py
@time:2020-04-23 17:58
@file_desc: 
"""


# class Cluster(object):
#     def __init__(self, retain=0.15, x=):
#         self.retain =

import math
import matplotlib.pyplot as plt


def calc(day=1):
    return math.pow(day, -0.469) * 0.15

if __name__ == '__main__':
    res = []
    for i in range(50):
        res.append(calc(i+1))
    plt.plot(res)
    plt.show()
    print(res[2])
    # f = -0.1
