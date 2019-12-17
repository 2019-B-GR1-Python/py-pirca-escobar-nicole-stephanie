# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 07:51:39 2019

@author: USRBET
"""



import pandas as pd
import numpy as np
import os
import sqlite3

path_save2 = 'C://Users//USRBET//Documents//GitHub//py-pirca-escobar-nicole-stephanie//03-pandas//Data//artwork_data.pickle'

df5 = pd.read_pickle(path_save2)
serie_artistas_repetidos = df5["artist"]

artistas = pd.unique(serie_artistas_repetidos)

artistas.size
len(artistas)

blake = df5["artist"] == "Blake, William"
blake.values_counts()


df5["artist"].value_counts()

df5_blake = df5[blake]
