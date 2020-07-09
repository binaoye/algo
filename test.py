# -*- coding: utf-8 -*-
"""
@author: xiaoke
@file: test.py
@time:2020-03-09 15:05
@file_desc: 
"""
import logging as log
import sys
import hashlib

log.basicConfig(level=log.DEBUG)
_logger = log.getLogger(__name__)

def myhash(instr):
    md5 = hashlib.md5()  # 应用MD5算法计算哈希
    md5.update(str(instr).encode('utf-8'))
    return md5.hexdigest()


if __name__ == '__main__':
    xy = "116.256586,39.986913"
    xz = "116.256586,39.986913"
    print(myhash(xy))
    print(myhash(xz))