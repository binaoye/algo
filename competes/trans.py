# -*- coding: utf-8 -*-
"""
@author: xiaoke
@file: trans.py
@time:2020-05-14 14:09
@file_desc: 
"""
import logging as log


import gensim
import numpy as np

if __name__ == '__main__':
    model_path = "/Users/hortor/Downloads/temp_model.bin"
    model = gensim.models.KeyedVectors.load_word2vec_format(model_path, binary=True)
    print(model.get_vector('1491049'))
    
