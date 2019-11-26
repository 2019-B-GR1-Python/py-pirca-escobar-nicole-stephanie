# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 07:59:15 2019

@author: USRBET
"""

import numpy as np
import pandas as pd

lista_numeros =[1,2,3,4]

tupla_numeros =(1,2,3,4)

np_numeros =np.array((1,2,3,4))

serie_a=pd.Series(lista_numeros)


serie_b=pd.Series(tupla_numeros)

serie_c=pd.Series(np_numeros)

serie_d=pd.Series([
        True,
        False,
        12,
        12.12,
        "Nicole",
        None,
        (),
        [],
        {"nombre": "Nicole"}])

serie_d[3]

lista_cuidades = ["Ambato", "Loja", "Quito","Cuenca"]

series_cuiadades =pd.Series(lista_cuidades,
                            index =[
                                    "A",
                                    "L",
                                    "Q",
                                    "C",
                                    ])

series_cuiadades["Q"]

series_cuiadades[2]


valores_cuidad = {
        "Ibarra": 9500,
        "Guayaqui": 10000,
        "Cuenca": 7000,
        "Quito": 80000,
        "Loja": 3000,
        }

serie_valor_cuidad =pd.Series(
        valores_cuidad)

serie_valor_cuidad[0]

serie_valor_cuidad["Ibarra"]

cuidades_menor_a_5000 =serie_valor_cuidad <5000

serie_valor_cuidad =serie_valor_cuidad *1.1

serie_valor_cuidad["Quito"] = serie_valor_cuidad["Quito"] - 50
        
print ("Lima" in serie_valor_cuidad)

print ("Loja" in serie_valor_cuidad)


respuesta= np.square(serie_valor_cuidad)

respuestaCos= np.cos(serie_valor_cuidad)


cuidades_uno =pd.Series({
        "Montañita": 300,
        "Guayaqui": 10000,
        "Quito": 2000
        })
cuidades_dos =pd.Series({
        "Loja": 300,
        "Guayaqui": 10000,
        
        })

cuidades_uno ["Loja"] = 0
cuidades_dos ["Quito"] = 0

cuidades_uno ["Montañita"] = 0
print(cuidades_uno + cuidades_dos)

cui_add= cuidades_uno.add(cuidades_dos)

cui_concatenadas =pd.concat([
        cuidades_uno,
        cuidades_dos])

cui_concatenadas_v =pd.concat([
        cuidades_uno,
        cuidades_dos], verify_integrity= True
)


cui_append =cuidades_uno.append(cuidades_dos, verify_integrity= True)

cuidades_uno.max()
pd.Series.max(cuidades_uno)


cuidades_uno.min()
pd.Series.min(cuidades_uno)

np.min (cuidades_uno)

#Funciones estadisticas 

cuidades_uno.mean()
cuidades_uno.median()
np.average(cuidades_uno)

cuidades_uno.head(2)

cuidades_uno.tail(2)

#funciones para ordenar 

cuidades_uno.sort_values(ascending= False).head(2)

cuidades_uno.sort_values().tail(2)






