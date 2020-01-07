# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 00:15:15 2020

@author: NICOLE
"""

import pandas as pd
import numpy as np
import math


path_guardado_bin =  'C://Users//NICOLE//Documents//GitHub//py-pirca-escobar-nicole-stephanie//03-pandas//Data//artwork_data_completo.pickle'
df = pd.read_pickle(path_guardado_bin)

seccion_df = df.iloc[49980:50019,:].copy()

#agrupar
#se escoge la columna que vamos agrupar.

df_agrupado = seccion_df.groupby('artist')

#tipo

type(df_agrupado)


#for para ver que tiene el dataframe
#solo llegan dos cosas, que son esas cosas y que tipo de datos son ?

for columna_agrupada,df_completo in df_agrupado:
    print(type(columna_agrupada)) # str
    print( type(df_completo)) #dataframe
    
#contar todos los valores de la columna.    
a = seccion_df['units'].value_counts()
a.empty #comprobar si toda la columna tiene valoes vacios.


def llenar_vacios_vacion(series,tipo):
    
    lista_valores = series.value_counts()
    if(lista_valores.empty == True):
        return series
    
    else:
        if(tipo == 'promedio'):
            suma = 0
            numero_valores = 0    
            for valor_serie in series:        
                if(isinstance(valor_serie,str)):
                    valor = int(valor_serie)
                    numero_valores += 1
                    suma += valor
                else:
                    pass
            promedio = suma/numero_valores
            
            #busca los Nan y pone ese valor
            serie_valores_llenos = series.fillna(promedio)
            
        if(tipo == 'value_counts'):    
            for valor_serie in series:        
                if(isinstance(valor_serie,str)):
                    valor = valor_serie            
                else:
                    pass    
            #busca los Nan y pone ese valor
            serie_valores_llenos = series.fillna(valor)   
            
        return serie_valores_llenos
 
        
def transformar_df(df):
    df_artist = df.groupby('artist')
    lista_df = []
    
    for artista,df in df_artist:
        copia = df.copy()
        
        serie_w = copia['width']
        serie_h = copia['height']
        serie_u = copia['units']
        serie_i = copia['inscription']
        
        copia.loc[:,'width'] = llenar_vacios_vacion(serie_w,'promedio')
        copia.loc[:,'height'] = llenar_vacios_vacion(serie_h,'promedio')
        copia.loc[:,'units'] = llenar_vacios_vacion(serie_u,'value_counts')
        copia.loc[:,'inscription'] = llenar_vacios_vacion(serie_i,'value_counts')
        
        lista_df.append(copia)
        
    df_completo_con_valores = pd.concat(lista_df)
    return df_completo_con_valores
    
                
        
df_completo_con_valores = transformar_df(seccion_df)