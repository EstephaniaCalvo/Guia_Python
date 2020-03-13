# Título: Módulo Mapa_Colombia.py
# Autor: Estephania Calvo Carvajal

import numpy as np
import pandas as pd
import json
import os

# Constantes 

# Capital
capital="Cundinamarca - Bogotá"
coord_cap=[4.598889, -74.080833] 

# Ciudades 

departamentos=["Antioquia - Medellín", "Boyacá - Tunja", "Caldas - Manizales", "Caquetá - Florencia", "Cauca - Popayán", "Cesar - Valledupar", "Chocó - Quibdó", "Huila - Neiva", "Nariño - Pasto", "Norte de Santander - Cúcuta", "Putumayo - Mocoa", "Quindío - Armenia", "Risaralda - Pereira", "Santander - Bucaramanga", "Tolima - Ibagué", "Valle del Cauca - Cali"]

## Coordenadas ciudades
c_x= [-75.574828, -73.361389, -75.484722, -75.611667, -76.600278, -73.259722, -76.658192, -75.2875, -77.274722, -72.504722, -76.646389, -75.6725, -75.694558, -73.116111, -75.200556, -76.519722]

c_y=[6.244747, 5.540278, 5.066111, 1.614167, 2.459167, 10.460278, 5.692277, 2.9275, 1.21, 7.9075, 1.149167, 4.538889, 4.814278, 7.118611, 4.437778, 3.44]

## DataFrame ciudades
df_departamentos=pd.DataFrame({"LAT":c_y,"LOG":c_x,"C":departamentos})

# Zonas Francas

## Coordenadas pueblos y villas

z_francas=["Z.F:Neiva", "Z.F:Yumbo", "Z.F:Pereira", "Z.F:Funza", "Z.F:Fontibon"]

zf_x=[-75.329079, -76.491929, -75.872766, -74.163103, -74.153823]

zf_y=[2.906665, 3.546749, 4.882888, 4.747874, 4.676238]

## DataFrame pueblos
df_zfrancas=pd.DataFrame({"LATI":zf_y,"LOGI":zf_x,"P":z_francas})

# Croquis

## Croquis ciudades y pueblos
departments_path = os.path.join(os.getcwd(),'Modulos\\','Colombia.geojson') 
departments_geojson = json.load(open(departments_path, encoding="utf8"))