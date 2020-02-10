# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 16:12:34 2019

@author: Ale
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os



path_csv = "C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\data\\world_marathon_majors2.csv"
##C:\Users\Ale\Documents\GitHub\py-macas-cevallos-alexandra-vanessa\Proyecto_1_Bimestre\data
data_frame_test = pd.read_csv(path_csv,  encoding = 'unicode_escape',sep = ";",parse_dates=[2],infer_datetime_format=True)
data_frame_test.head()
data_frame_test.dtypes
temp = pd.DatetimeIndex(data_frame_test['time'])
data_frame_test['Date'] = temp.date
data_frame_test['Time'] = temp.time
del data_frame_test['time']

genero = data_frame_test['gender'].value_counts()
tipo_genero = ['Male','Female']

plt.figure(figsize=(5,6))
plt.title('Segregación de ganadores por genero')
plt.bar(tipo_genero, genero, color = 'orangered')
for a,b in zip(tipo_genero, genero):
    plt.text(a,b,str(b),  horizontalalignment='center', fontsize=15, family = 'fantasy',fontweight = 'bold')
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\data\\Segregación de ganadores por genero.jpg")
plt.show()

"""
segundo
"""
plt.title('Top 10 de los ganadores de los maratones')
ganadores_count = data_frame_test['winner'].value_counts()[:10].sort_values().plot(kind='barh')
count_ganadores = data_frame_test['winner'].value_counts()[:10]
print(count_ganadores)
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\data\\Top 10 de los ganadores de los maratones.jpg")
plt.show()

"""
"""

print ("Han existido un total de: ",data_frame_test["winner"].size," ganadores de los seis Grandes Maratones Mundiales de la historia")
print (data_frame_test["winner"])


"""
"""
#fig = plt.figure(figsize=(8,18))

edades_hombres = data_frame_test.age[data_frame_test.gender=='Male'].value_counts()[:10]

edades_mujeres = data_frame_test.age[data_frame_test.gender=='Female'].value_counts()[:10]

#Mostramos la grafica con el metodo show()
plt.show()
#print(edades_hombres)
#data_frame_test.age[data_frame_test.gender=='Male'].value_counts().plot(kind='barh',alpha=1)
#plt.show()

#Obtenemos la posicion de cada etiqueta en el eje de X
	
ganadores = data_frame_test['age'].value_counts().groupby(data_frame_test['gender']).mean().plot(kind='bar')
print(ganadores)
plt.show()


"""
"""
plt.pie(generoC, labels=letra_genero, autopct='%1.1f%%',
        shadow=True, startangle=90)
plt.axis('equal')
plt.show()
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\data\\Segregación de ganadores por genero.jpg")


plt.title('Particiaciones por edad de mujeres')
plt.pie(edades_mujeres, labels=edades_mujeres,autopct="%0.1f %%")
plt.axis("equal")
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\data\\Participación por edad en mujeres.jpg")
plt.show()

plt.title('Particiaciones por edad de hombres')
plt.pie(edades_hombres, labels=edades_hombres,autopct="%0.1f %%")
plt.axis("equal")
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\data\\Participación por edad en hombres.jpg")
plt.show()




plt.figure(figsize=(30,5))
plt.title("Total de Participantes por año")
ganadores_anio = data_frame_test['year'].value_counts()[:40].sort_values().plot(kind='bar')
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\data\\Total de Participantes por año.jpg")

plt.show()

data_frame_test['year'].value_counts()[:40]

edad = data_frame_test['age'].value_counts()

edadNum = [int(x) for x in edad]
#edadNum.sort()
a = 0 
b = 0 
c = 0
d = 0 
e = 0 
f = 0
for i in edadNum:
    if(i<=25):
        a = a+1
    elif(i<=35 and i>25):
        b = b+1
    elif(i<=45 and i>35):
        c = c+1
    elif(i<=55 and i>45):
        d = d+1
    elif(i<=65 and i>55):
        e = e+1
    else:
        f = f+1

edades = [a,b,c,d,e,f]
edadesCat = ['De 18 a 25 años', 'De 26 a 35 años', 'De 36 a 45 años', 
             'De 46 a 55 años', 'De 56 a 65 años', 'De 65 años en adelante']

plt.title("Porcetanjes de participantes por rango de edad")
plt.pie(edades, labels=edadesCat, autopct='%1.1f%%',
        shadow=True, startangle=90, radius = 1800)
plt.axis('equal')
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\data\\Porcetanjes de participantes por rango de edad.jpg")
plt.show()


edad = data_frame_test['age'].value_counts()
genero2 = data_frame_test['gender']


edadNum = [int(x) for x in edad]
aM = 0
aF = 0
bM = 0 
bF = 0 
cM = 0
cF = 0
dM = 0 
dF = 0 
eM = 0
eF = 0
fM = 0
fF = 0

for i,j in zip(edadNum,genero2):
    if(i<=25 and j== 'Male'):
        aM = aM+1
    elif(i<=25 and j=='Female'):
        aF = aF+1
    elif(i<=35 and i>25 and j=='Male'):
        bM = bM+1
    elif(i<=35 and i>25 and j=='Female'):
        bF = bF+1
    elif(i<=45 and i>35 and j=='Male'):
        cM = cM+1
    elif(i<=45 and i>35 and j=='Female'):
        cF = cF+1
    elif(i<=55 and i>45 and j=='Male'):
        dM = dM+1
    elif(i<=55 and i>45 and j=='Female'):
        dF = dF+1
    elif(i<=65 and i>55 and j=='Male'):
        eM = eM+1
    elif(i<=65 and i>55 and j=='Female'):
        eF = eF+1
    elif(i>65 and j=='Male'):
        fM = fM+1
    else:
        fF = fF+1
        
edadesM = [aM,bM,cM,dM,eM,fM]
edadesF = [aF,bF,cF,dF,eF,fF]
edadesCat = ['De 18 a 25 años', 'De 26 a 35 años', 'De 36 a 45 años', 
             'De 46 a 55 años', 'De 56 a 65 años', 'De 65 años en adelante']
N = 6
ind = np.arange(N)
width = 0.35 
fig, ax = plt.subplots(figsize=(15,8))
bar1 = ax.bar(ind, edadesM, width, color = 'blue')
for a,b in zip(ind, edadesM):
    ax.text(a,b,str(b), ha='center',fontweight = 'bold')
bar2 = ax.bar(ind + width, edadesF, width, color = 'red')
for a,b in zip(ind + width, edadesF):
    ax.text(a,b,str(b), ha='center',fontweight = 'bold')

ax.set_title('Participacion por Genero y por Edad')
ax.set_xticks(ind + width / 2)
ax.set_xticklabels(('De 18 a 25 años', 'De 26 a 35 años', 'De 36 a 45 años', 
             'De 46 a 55 años', 'De 56 a 65 años', 'De 65 años en adelante'))
ax.legend((bar1[0], bar2[0]), ('Masculino', 'Femenino'))
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\data\\Participantes por genero y por edad.jpg")

plt.show()


tiempo = data_frame_test['Time'].value_counts()[:10]
tiemposM = ['< 2h05m', '< 2h10m', '< 2h20m', '< 2h30m', '< 2h40m', 
           '< 2h50m', '< 3h00m', '< 3h10m', '< 3h20m', '< 3h30m']
y_tiempo = np.arange(len(tiemposM))
plt.figure(figsize=(10,8))
plt.title('Tiempos por cantidad de Participantes')
plt.barh(y_tiempo, tiempo)
for i, v in enumerate(tiempo):
    plt.text(v + 3, i + .25, str(v), va='center', color='blue', fontweight='bold')
plt.yticks(y_tiempo, tiemposM)
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\data\\Tiempos por cantidad de Participantes.jpg")

plt.show()

plt.figure(figsize=(10,8))
plt.title('Pais con mayor numero de participantes')
data_frame_test['country'].value_counts().plot(kind='bar')
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\data\\Pais con mayor numero de participantes.jpg")

plt.title('Participantes en marathon')
data_frame_test['marathon'].value_counts().plot(kind='bar')
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\data\\participantes en marathon.jpg")


plt.title('ciudades que participan en Boston')
data_frame_test.country[data_frame_test.marathon=='Boston'].value_counts().plot(kind='bar')
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\data\\ciudades que participan en Boston.jpg")

plt.figure(figsize=(30,8))
plt.title('Participantes de EEUU')

data_frame_test.winner[data_frame_test.country=='United States'].value_counts().plot(kind='bar')
plt.savefig("C:\\Users\\Ale\\Documents\\GitHub\\py-macas-cevallos-alexandra-vanessa\\Proyecto_1_Bimestre\\data\\Participantes de EEUU.jpg")








##grouped = data_frame_test.groupby([times.hour, times.minute])
##print(grouped)

#plt.title("Homicidios/Asesinatos por provincia")
#data_frame_test['Ground'].value_counts().plot(kind='bar')
#plt.show()
data_frame_test['Ground'].value_counts()[:20]
data_frame_test['Ground'].unique()[:10].plot(kind='bar')  ##top 10
data_frame_test.shape  ##tamaño (x, y)