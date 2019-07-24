#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 24 00:39:55 2019

@author: augustocbx
"""

import numpy as np

def sigmoid(soma):
    return 1 / (1 + np.exp(-soma))

a = sigmoid(1.5)
b = np.exp(0)