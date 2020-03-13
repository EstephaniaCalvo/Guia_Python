#Módulo Mapa_Iwate.py

import numpy as np
import pandas as pd
import json
import os

# Importar folium
def imp_folium ():
    "Valida si el módulo folium está instalado, si es así lo carga y si no muestra un mensaje con las indicaciones para instalarlo"
    try:
        import folium
    except(Exception):
        print("""Usted no tiene instalado el módulo 'folium', para hacerlo ejecute la celda siguiente celda con el comando
        'pip install folium', espere hasta termine el proceso, resustare el kernel del notebook y vuelva a correr este programa.""")
    
    return None

# Constantes 

# Capital
capital="Cápital: Morioka"
coord_cap=[39.683333, 141.15]

# Ciudades 

ciudades["Hachimantai","Hanamaki","Ichinoseki","Kamaishi","Kitakami","Kuji","Miyako","Ninohe","Ōfunato","Ōshū","Rikuzentakata","Takizawa","Tōno"]
## Coordenadas ciudades
c_x= [141.095278, 141.116667, 141.126583, 141.885556, 141.113056, 141.775278, 141.957222, 141.304722, 141.708333, 141.138889, 141.629444, 141.076944, 141.533611]

c_y=[39.926389, 39.388611, 38.934722, 39.275833, 39.286667, 40.190278, 39.641389, 40.271111, 39.082222, 39.144444, 39.015278, 39.734722, 39.3275]

## DataFrame ciudades
df_ciudades=pd.DataFrame({"LAT":c_y,"LOG":c_x,"C":ciudades})

# Pueblos y villas
pueblos["Kanegasaki","Kuzumaki","Shizukuishi","Ōtsuchi","Sumita","Hirono","Karumai","Kunohe","Noda","Ichinohe","Hiraizumi","Fudai","Iwaizumi","Tanohata","Yamada","Shiwa","Yahaba","Nishiwaga"]

## Coordenadas pueblos y villas
pv_x= [141.116111, 141.436389, 140.975556, 141.906389, 141.575833, 141.718056, 141.460556, 141.418889, 141.818056, 141.295278, 141.114167, 141.886111, 141.796667, 141.888889, 141.948889, 141.167778, 141.143056, 140.779167]
pv_y=[39.195556, 40.039722, 39.696111, 39.359722, 39.141944, 40.408611, 40.326667, 40.211389, 40.11, 40.213056, 38.986667, 40.005278, 39.843056, 39.930278, 39.4675, 39.554722, 39.605833, 39.317778]

## DataFrame pueblos
df_pueblos=pd.DataFrame({"LATI":pv_y,"LOGI":pv_x,"P":pueblos})

# Croquis

## Croquis ciudades y pueblos
cities_path = os.path.join(os.getcwd(),'jp_cities1.geojson') 
cities_geojson = json.load(open(cities_path, encoding="utf8"))

## Croquis prefactura
pref_path = os.path.join(os.getcwd(),'jp_prefs1.geojson') 
pref_geojson = json.load(open(pref_path, encoding="utf8"))
    
    
def c_mapa(p_opt, ruta, nombre):
    """
    Genera un mapa de la prefactura de Iwate Japón, con sus cidudades y pueblos, y señala un punto o segmento índicado.
    Además guarda el mapa el un archivo .html con la ruta y el nombre indicado, este debe tener la extensión ".html".
    """
    
    # Importar folium
    imp_folium()
    
    # Crear mapa
    mapa=folium.Map(location=[39.683333, 141.15],zoom_start=8, control_scale=True)
    
    # Cargar croquis ciudades y pueblos
    folium.GeoJson(cities_geojson,name='ciudades',style_function=lambda feature: {'fillColor': "yellowgreen",'fillOpacity': 0.5,'weight': 1,'color': 'darkgreen'}).add_to(mapa)

    # Cargar croquis prefactura
    folium.GeoJson(pref_geojson,name='Prefactura',style_function=lambda feature: {'fillColor': "yellowgreen",'fillOpacity': 0.2,'weight': 3,'color': 'darkgreen'}).add_to(mapa)
    
    # Activar el controlador de capas
    folium.LayerControl().add_to(mapa)
    
    # Poner marcador a la cápital
    folium.Marker(coord_cap, tooltip=capital,icon=folium.Icon(color='red')).add_to(mapa)
    
    # Poner marcador a las ciudades principales
    for row in df_ciudades.itertuples():
    mapa.add_child(folium.Marker(location=[row.LAT,row.LOG],tooltip=row.C,icon=folium.Icon(color='orange')))
    
    # Poner marcador a los pueblos
    for row in df_pueblos.itertuples():
    mapa.add_child(folium.Marker(location=[row.LATI,row.LOGI],tooltip=row.P,icon=folium.Icon(color='gray')))

    # Poner marcador al punto o segmento óptimo:
    
    if type(p_opt[1])==list: # Si es un segmento óptimo

        opt_x1=p_opt[0][0]
        opt_y1=p_opt[0][1]
        opt_x2=p_opt[1][0]
        opt_y2=p_opt[1][1]
        
        # Generar puntos intermedios
        
        ## Calcular la pendiente
        pendiente=(opt_y2-opt_y1)/(opt_x2-opt_x1,)
        
        ## Crear valores x
        c_opt_x=list(np.linspace(opt_x2,opt_x1,100))
        
        ## Calcular valores de y
        c_opt_y=[(pendiente*(i-opt_x1))+opt_y1 for i in c_opt_x]
        
        # Generar etiquetas de puntos intermedios
        etiq=["Óptimo" for i in c_opt_x]
        
        # Generar DataFrame seg_opt
        df_seg_opt=pd.DataFrame({"LA":c_opt_y,"LO":c_opt_x,"E":etiq})
        
        # Generar marcadores del segmento óptimo
        for row in df_seg_opt.itertuples():
            mapa.add_child(folium.CircleMarker(location=[row.LA,row.LO], tooltip=row.E, radius=1,color='crimson', fill=True, fill_color='crimson', fill_opacity=0.5)
        
    else:
        opt_x=p_opt[0]
        opt_y=p_opt[1]
        
        # Poner marcador punto óptimo
        folium.CircleMarker(location=[opt_y,Opt_x], tooltip="Óptimo", radius=10,color='crimson', fill=True, fill_color='crimson', fill_opacity=0.5)

    mapa.save(ruta+nombre)
    return mapa