# -*- coding: utf-8 -*-
"""
Created on Tue Feb 06 09:50:29 2018

@author: to72078
"""
import numpy as np
xx, yy = np.meshgrid(np.arange(0, 1, 0.1), np.arange(10, 11, 0.2))

print xx
print xx.ravel()

print np.c_[xx.ravel(), yy.ravel()]