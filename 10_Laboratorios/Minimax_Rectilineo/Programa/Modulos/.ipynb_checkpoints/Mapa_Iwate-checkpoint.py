# Título: Módulo Mapa_Iwate.py
# Autor: Estephania Calvo Carvajal

import numpy as np
import pandas as pd
import json
import os

# Constantes 

# Capital
capital="Cápital: Morioka"
coord_cap=[39.683333, 141.15]

# Ciudades (Sin cabpital)

ciudades=["Hachimantai", "Hanamaki", "Ichinoseki", "Kamaishi", "Kitakami", "Kuji", "Miyako", "Ninohe", "Ōfunato", "Ōshū", "Rikuzentakata", "Takizawa", "Tōno"]

## Coordenadas ciudades
c_x= [141.095278, 141.116667, 141.126583, 141.885556, 141.113056, 141.775278, 141.957222, 141.304722, 141.708333, 141.138889, 141.629444, 141.076944, 141.533611]

c_y=[39.926389, 39.388611, 38.934722, 39.275833, 39.286667, 40.190278, 39.641389, 40.271111, 39.082222, 39.144444, 39.015278, 39.734722, 39.3275]

## DataFrame ciudades
df_ciudades=pd.DataFrame({"LAT":c_y,"LOG":c_x,"C":ciudades})

# Pueblos y villas
pueblos=["Kanegasaki", "Kuzumaki", "Shizukuishi", "Ōtsuchi", "Sumita", "Hirono", "Karumai", "Kunohe", "Noda", "Ichinohe", "Hiraizumi", "Fudai", "Iwaizumi", "Tanohata", "Yamada", "Shiwa", "Yahaba", "Nishiwaga"]

## Coordenadas pueblos y villas
pv_x= [141.116111, 141.436389, 140.975556, 141.906389, 141.575833, 141.718056, 141.460556, 141.418889, 141.818056, 141.295278, 141.114167, 141.886111, 141.796667, 141.888889, 141.948889, 141.167778, 141.143056, 140.779167]
pv_y=[39.195556, 40.039722, 39.696111, 39.359722, 39.141944, 40.408611, 40.326667, 40.211389, 40.11, 40.213056, 38.986667, 40.005278, 39.843056, 39.930278, 39.4675, 39.554722, 39.605833, 39.317778]

## DataFrame pueblos
df_pueblos=pd.DataFrame({"LATI":pv_y,"LOGI":pv_x,"P":pueblos})