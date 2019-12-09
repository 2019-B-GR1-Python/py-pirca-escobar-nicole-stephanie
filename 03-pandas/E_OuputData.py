# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 08:00:08 2019

@author: USRBET
"""

import pandas as pd
import numpy as np
import os
import sqlite3


path_guardado_bin = "C://Users//USRBET//Documents//GitHub//py-pirca-escobar-nicole-stephanie//03-pandas//Data//artwork_data_completo.pickle"

df5 = pd.read_pickle(path_guardado_bin)
df= df5.iloc[49980:50019, :].copy()
 ##tipos de archivos
 #JSON
 #EXCEL
 #SQL
 ####   EXCEL 
 
df.to_excel('mi_df_completo.xlsx')
## copiar los indices 
df.to_excel(path_guardado_bin)
df.to_excel(path_guardado_bin, index =False)
columnas =['artist', 'title','year']
df.to_excel (path_guardado_bin, columns= columnas)

## CREAR VARIAS HOJAS DE TRABAJO 
# 1) SE DEFINE EL PATH

path_multiple = "C://Users//USRBET//Documents//GitHub//py-pirca-escobar-nicole-stephanie//03-pandas//Data//artwork_data.pickle"
write = pd.ExcelWriter(path_multiple,
                       engine = 'xlswriter')

df.to_excel(writer, sheet_name= 'Primera')

df.to_excel(writer, sheet_name= 'Segunda', index =False)


df.to_excel(writer, sheet_name= 'Tercera', columns = columns)

writer.save()


num_artistas = df['artist'].value_counts() ## agruar por artista 

path_colores = "C://Users//USRBET//Documents//GitHub//py-pirca-escobar-nicole-stephanie//03-pandas//Data//mi_df_colores.xlsx"
df.to_excel('mi_df_completo_colores.xlsx')
writer = pd.ExcelWriter(path_colores,
                       engine = 'xlsxwriter')
num_artistas.to_excel (writer, sheet_name = 'Artistas')


hoja_artistas= writer.sheets['Artistas']

rango_celdas = 'B2: B{}'.format(len(num_artistas.index) + 1) ## esto pone un 3 +1 que da 4 xd


## cear un diccionario
formato_artistas ={
        "type": "2_color_scale",
        "min_value": "10",
        "min_type":"percentile",
        "max_value": "99",
        "max_type": "percentile"
        }
## se crea de que rango a que rago el se define el formato a usar 

hoja_artistas.conditional_format(rango_celdas, formato_artistas)

writer.save()






path_grafico="C://Users//USRBET//Documents//GitHub//py-pirca-escobar-nicole-stephanie//03-pandas//Data//mi_df_grafico.xlsx
writer = pd.ExcelWriter(path_grafico,
                       engine = 'xlsxwriter')


chart_series ={
    'values': '=Sheet1!$A$1:$A$6',
    'marker': {
        'type': 'square',
        'size': 8,
        'border': {'color': 'black'},
        'fill':   {'color': 'red'},
    },
}


chart_series.conditional_format(chart_series)

writer.save()
## el lunes y marte recepcion de proyectos 
















