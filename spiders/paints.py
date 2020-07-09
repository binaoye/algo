# -*- coding: utf-8 -*-
"""
@author: xiaoke
@file: paints.py
@time:2020-05-29 15:28
@file_desc: 
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import scipy.optimize as optimization

data_day = [1,2,3,4,5,6,7,8] #x坐标值|x coord
data_ltv = [0.2,0.35,0.45,0.52,0.57,0.6,0.62,0.63] #y坐标值|y coord

xdata = np.array(data_day)
ydata = np.array(data_ltv)

#定义使用的公式|customize equation
def lnFunction(x, A, B):
    return A*np.log(x)+B

if __name__ == '__main__':
    guess = [1, 1]  # 定义初始A、B|initialize a and b
    try:
        params, params_covariance = optimization.curve_fit(lnFunction, xdata, ydata,
                                                           guess)  # 拟合，A、B结果存入params|curve fitting and store a, b values to params
        print(params)
        result = ''  # 输出结果|to store result
        for i in range(1, 15):
            result += str(round(lnFunction(i, params[0], params[1]),
                                2))  # 将i带入公式中的x，使用拟合出的A、B值计算y值，并保留两位小数|calculate result for each i as x using the a, b values, and round the result to 2 points
            if i != 14:
                result += ','  # 每个结果用逗号隔开，并省略最后一个逗号|separate each result with comma, and omit the last comma
        print(result)
    except:
        print("except")

