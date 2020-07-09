# -*- coding: utf-8 -*-
"""
@author: xiaoke
@file: img_sim.py
@time:2020-04-22 15:46
@file_desc: 
"""
import logging as log
import sys

log.basicConfig(level=log.DEBUG)
_logger = log.getLogger(__name__)

from skimage.measure import compare_ssim
import cv2
import os

import voc
import numpy as np
