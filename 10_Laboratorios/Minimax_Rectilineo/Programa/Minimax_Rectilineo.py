# Título: Minimax Rectilíneo
# Autor: Estephania Calvo Carvajal

# -2. Importar módulos
import numpy as np
import pandas as pd
import json
import os

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

from Modulos.Mapa_Iwate import cities_geojson, pref_geojson, coord_cap, df_ciudades, df_pueblos, capital

# -1. Funciones auxiliares 

## a. Leer y almacenar datos de entrada.
def lectura_datos(archivo):
    "Lee y almacena las coordenas del archivo indicado"

    c_y,c_x=[],[]

    file=open(archivo)
    
    for i in file:
        c_x.append(float(i.split()[0]))
        c_y.append(float(i.split()[1]))
    
    # Calcular el número de decimales

    coord=c_y.copy()
    coord.extend(c_x)
    n_enteros_x=[1 for i in coord if i.is_integer()] # Contar los números enteros
    
    if sum(n_enteros_x)==len(c_x)*2:# Si todos los números son enteros
        nd=1 # El número de decimales de las clases es 1
    else: # Si no, enontar la cantidad decimales de cada dato y escoger el mayor.
        decimales=[(len(str(j))-str(j).index(".")) for j in coord]
        nd=max(decimales)

    return c_x,c_y,nd


## b. Calcular segmento óptimo.
def optimo(c_x,c_y,nd):
    """
    Calcula el punto óptimo o el segmento óptimo donde ubicar la instalación, y el valor de la función objetivo
    a partir de la lista de coordenadas de los objetivos.
    """
    l_suma=[c_x[i]+c_y[i] for i in range(len(c_x))]
    l_resta=[c_y[i]-c_x[i] for i in range(len(c_x))]
    c1,c2,c3,c4=min(l_suma),max(l_suma),min(l_resta),max(l_resta)
    c5=max (c2-c1,c4-c3)
    z=c5/2
    opt_1=(round(0.5*(c1-c3),nd),round(0.5*(c1+c3+c5),nd))
    opt_2=(round(0.5*(c2-c4),nd),round(0.5*(c2+c4-c5),nd))
    
    if opt_1==opt_2:
        opt=(opt_1,z)
    else:
        opt=([opt_1,opt_2],z)
        
    return opt

## c. Generar matriz Z
def gen_z(c_x,c_y,nd):
    """
    Generar una malla 100 * 100 con los vectores 'x', 'y' a partir de las coordenadas, y calcula la matríz z.
    """

    # Crear vectores
    v_x=[round(i,nd) for i in list(np.linspace(min(c_x),max(c_x),num=100))]
    v_y=[round(i,nd) for i in list(np.linspace(min(c_y),max(c_y),num=100))]

    # Crear matríz z
    m_z=[]

    for i in v_x:
        l_z=[]
        for j in v_y:
            z=0
            for k in range(len(c_x)):
                distancia=abs(i-c_x[k])+abs(j-c_y[k])
                if z<distancia: 
                    z=round(distancia,nd)
            l_z.append(z)
        m_z.append(l_z)
    return (v_x,v_y,m_z)

## d. Guardar archivo de resultados.xlsx
def resultados (archivo,opt,v_x,v_y,m_z): # Crear la función frecuencias con parámetros de entrada: lista de clases, lista de datos y archivo de datos.
    """
    Crear y guardar el archivo.xls con los resultados del pograma en la carpeta Resultados.
    """
    
    # Extraer los puntos óptimos y el costo minimo.
    p_opt,z=opt

    # Ubicarse en la ruta de Resultados
    if os.path.exists("Resultados")==False: # Si la carpeta "Resultados" no existe:
        os.mkdir("Resultados") # Crear la carpeta de resultados
        
    # Crear los DataFrames

    ## DataFrame del Segmento óptimo.
    if type(p_opt)==list: # Si es un segmento óptimo
        title_opt="Segemento Óptimo"
        p_opt.sort()
        df_optimo=pd.DataFrame({"Segmento":["Desde","Hasta"],"Coord_x":[p_opt[0][0],p_opt[1][0]],"Coord_y":[p_opt[0][1],p_opt[1][1]]})
        
    else:
        coord_x=str(p_opt[0])
        coord_y=str(p_opt[1])
        title_opt="Punto Óptimo"
        df_optimo=pd.DataFrame({"Coordenada x":[coord_x,""],"Coordenada y":[coord_y,""]})

    ### Crear diccionario del DataFrame de la matríz.
    dic_m_z={"Cy / Cx":v_y}
    claves=tuple([str(i) for i in v_x])
    valores=m_z

    diccionario=dict(zip(claves,valores))
    dic_m_z.update(diccionario)
    
    ## DataFrame de la matríz.
    df_m_z=pd.DataFrame(dic_m_z)
    
    # Crear el documento
    doc=pd.ExcelWriter('Resultados/Resultados_'+archivo[:-4]+'.xlsx', engine='xlsxwriter')
    
    ## Escribir resultados
    df_optimo.to_excel(doc, sheet_name='Óptimos',index=False, startrow=2)
    df_m_z.to_excel(doc, sheet_name='Matríz', index=False, startrow=2)

    # Abrir libro y hojas del documento
    libro=doc.book
    hoja_1=doc.sheets['Óptimos']
    hoja_2=doc.sheets['Matríz'] 

    # Títulos
    formato_titulo=libro.add_format({'bold': True, 'font_size': 16})
    negrita=libro.add_format({'bold':True})
    hoja_1.write(0, 0, title_opt, formato_titulo)
    hoja_2.write(0, 0, "Matríz de costos Z", formato_titulo)
    hoja_2.set_column('A:A', None,negrita)

    # Formato condicional
    hoja_2.conditional_format('B4:CW103', {'type': '3_color_scale'})
    
    # Escribir costos
    hoja_1.write(7,0,"Costo minimo z:",negrita)
    hoja_1.write(7,1,str(z))

    ## Guardar documento.
    doc.save() 
    doc.close()

    return None

## e. Hacer los gráficos

def graficos (archivo,opt,v_x,v_y,m_z,c_x,c_y):
    "Crea el gráficos de costos y el gráfico de ubicaciones"

    # Extarer punto o segamento óptimo:
    p_opt,z=opt
    
    # Crear gráfico de costos

    ## Crear arrays.
    X=np.array(v_x)
    Y=np.array(v_y)
    X, Y = np.meshgrid(X, Y)
    Z=np.transpose(np.array(m_z))

    ## Crear figura 3d
    fig = plt.figure(figsize=[7,6])
    ax = fig.gca(projection='3d')

    ## Dibujar la superficie
    ax.plot_surface(X, Y, Z, cmap=cm.jet, rstride=1, cstride=1)

    ## Títulos
    plt.title("Gráfica de costos de "+archivo[:-4]+"\n")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    ax.set_zlabel("Costo")

    ## Modificar eje z.
    ax.set_zlim(z-0.5) # Inciar el costo optimo menos 0.5
    ax.zaxis.set_major_locator(LinearLocator(10)) # Cantidad de marcadores 10
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.01f')) # Decimales de los marcadores 1

    ## Mostrar y guardar gráficos.
    plt.savefig("Resultados/Grafico_de_Costos_de_"+archivo[:-4]+".png")
    plt.show(block=False)
    plt.close()

    # Crear gráfico de ubicaciones
    
    ## Crear figura.
    plt.figure()

    ## Crear mapa de densidad
    plt.pcolormesh(X, Y, Z, cmap=cm.jet)

    ## Dibujar los puntos de las ubicaciones objetivos
    plt.plot(c_x,c_y,label="Objetivos",linestyle="",marker="o",markersize=4,markerfacecolor="black",markeredgecolor="white")

    ## Dibujar los puntos de las ubicaciones óptimas
    if type(p_opt)==tuple:
        plt.plot(p_opt[0],p_opt[1],label="Óptimo",marker="o",markersize=7,markerfacecolor="red",markeredgecolor="white")
    else:
        plt.plot([p_opt[0][0],p_opt[1][0]],[p_opt[0][1],p_opt[1][1]],label="Óptimos",linestyle=":",color="white",marker="o",markersize=7,markerfacecolor="red",markeredgecolor="white")
    ## Ejes
    r_1=(max(c_x)-min(c_x))*0.01
    r_2=(max(c_y)-min(c_y))*0.01
    plt.axis([min(c_x)-r_1,max(c_x)+r_1,min(c_y)-r_2,max(c_y)+r_2])
    
    ## Títulos
    plt.title("Gráfico de Ubicaciones de "+archivo[:-4]+"\n")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.legend()

    ## Activar cuadrícula
    plt.grid(linestyle=":")
    
    ## Mostrar y guardar gráficos.
    plt.savefig("Resultados/Ubicaciones_de_"+archivo[:-4]+".png")
    plt.show(block=False)
    plt.close()
    
    return None

def c_mapa(p_opt, ruta, nombre):
    """
    Genera un mapa de la prefactura de Iwate Japón, con sus cidudades y pueblos, y señala un punto o segmento índicado.
    Además guarda el mapa el un archivo .html con la ruta y el nombre indicado, este debe tener la extensión ".html".
    """
    
    # Importar folium

    try:
        import folium
        
    except(Exception):
        
        print("""Usted no tiene instalado el módulo 'folium', para hacerlo ejecute la celda siguiente celda con el comando
            'pip install folium', espere hasta termine el proceso, resustare el kernel del notebook y vuelva a correr este programa.""")
        
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
    
    # Si es un segmento óptimo
    if type(p_opt)==list: 

        opt_x1=p_opt[0][0]
        opt_y1=p_opt[0][1]
        opt_x2=p_opt[1][0]
        opt_y2=p_opt[1][1]
        
        # Generar puntos intermedios
        
        ## Calcular la pendiente
        pendiente=(opt_y2-opt_y1)/(opt_x2-opt_x1)
        
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
            mapa.add_child(folium.CircleMarker(location=[row.LA,row.LO], tooltip=row.E, radius=2,color='crimson', fill=True, fill_color='crimson', fill_opacity=0.5))
        
    else:
        opt_x=p_opt[0]
        opt_y=p_opt[1]
        # Poner marcador punto óptimo
        folium.CircleMarker(location=[opt_y,opt_x], tooltip="Óptimo", radius=10,color='crimson', fill=True, fill_color='crimson')

    mapa.save(ruta+nombre)
    return mapa

# 0. Programa principal
def main(ingreso=1,cm=0):
    """
    Al ingresar un archivo con las coordenadas (x,y) de puntos objetivos, calcula el punto o segmentos óptimo para ubicar una instlación manejando un modelo de distancia rectilíneo, genera una matriza de costos y devuelve un archivo de excel con los resultados anteriores y guarda los gráricos de costos y ubicaciones.
    """

    "1. Leer archivo de coordenadas"

    # Ingresar archivo de coordenadas.
    if ingreso==1:
        a_coord=input("Por favor ingrese el archivo que contiene las coordenadas de los puntos objetivos,\npor ejemplo, 'Municipios.txt':\n")
    elif ingreso=="e":
        a_coord="Ej_MR.txt"
    elif ingreso=="p1":
        a_coord="Iwate.txt"
    elif ingreso=="p2":
        a_coord="Focos_suroeste.txt"
        
    # Leer el archivo de coordenadas.
    x,y,d=lectura_datos(a_coord) 
    
    "2. Calcular el punto o el segmento óptimo."
    opt=optimo(x,y,d)

    "3. Calcular matríz de costos z"
    vx,vy,mz=gen_z(x,y,d)   
    
    "4. Crear el archivo de resultados"
    resultados(a_coord,opt,vx,vy,mz)
    
    "5. Crear gráficos"
    graficos(a_coord,opt,vx,vy,mz,x,y)
    
    "BONUS ---> 6. Crear mapa" 
    try: 
        if cm==1:
            m_ubicaciones= c_mapa(opt[0], "Resultados/", "Mapa_Hospital_Iwate.html")

            return m_ubicaciones
        else:
            return None
    except(Exception):
        return None

if __name__=="__main__":
    main()