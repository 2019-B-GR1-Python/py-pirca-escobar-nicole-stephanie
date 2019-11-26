# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 07:44:14 2019

@author: USRBET
"""
import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)

np_numeros = np.array((1,2))
df1 = pd.DataFrame(arr_pand)

s1= df1[0]

s2= df1[1]

s3= df1[2]

s4 = df1[serie_a]

serie_a = pd.Series(
        np_numeros)
