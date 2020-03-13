# Título: Minsum Rectilíneo
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

from Modulos.Mapa_Colombia import departments_geojson, coord_cap, df_departamentos, df_zfrancas, capital

# -1. Funciones auxiliares 

## a. Leer y almacenar datos de entrada.
def lectura_datos(archivo):
    "Lee y almacena las coordenas y pesos del archivo indicado"

    c_y,c_x,w=[],[],[]

    file=open(archivo)
    
    for i in file:
        c_x.append(float(i.split()[0]))
        c_y.append(float(i.split()[1]))
        w.append(float(i.split()[2]))
    
    # Calcular el número de decimales

    coord=c_y.copy()
    coord.extend(c_x)
    n_enteros_x=[1 for i in coord if i.is_integer()] # Contar los números enteros
    
    if sum(n_enteros_x)==len(c_x)*2:# Si todos los números son enteros
        nd=1 # El número de decimales de las clases es 1
    else: # Si no, enontar la cantidad decimales de cada dato y escoger el mayor.
        decimales=[(len(str(j))-str(j).index(".")) for j in coord]
        nd=max(decimales)

    return c_x,c_y,w,nd

## b. Calcular la o las coordenadas óptimas.
def coord_opt(coord, w, w_total):
    """
    Calcular la coordenada óptima, apartir de la lista de la coordenada, la de los pesos y el peso total
    """
    
    #Crear lista con las parejas coordenada - peso
    parejas=[[coord[i],w[i]] for i in range(len(coord))]
    parejas.sort() # Ordenar de menor a mayor
    
    ## Sumar los pesos hata llegar o sobrepasar la mitad del peso total
    c, sw=(0,0)
    while sw<w_total/2:
        sw+=parejas[c][1]
        c+=1

    copt_1=parejas[c-1][0] # Recuperar la coordenada óptima 1.

    # Si la suma de los pesos es exactamente igual a la mitad del peso total:
    if sw==w_total/2:
        # La coordenada óptima 2 es la siguiente a la coordenada 1.
        copt_2=parejas[c][0]
        c_opt=[copt_1, copt_2]
    else: 
        c_opt=[copt_1]    

    return c_opt

## c. Calcular y organizar el o los puntos óptimos.
def optimo(c_x, c_y, w,nd):
    """
    Calcula y organiza el o los puntos óptimos para ubicar la instalación y el valor de la función objetivo
    a partir de la lista de coordenadas de los puntos objetivos.
    """
    w_total=sum(w)
    w_max=max(w)

    # Calcular el o los puntos óptimos
    if w_max>=w_total/2:
        i=w.index(w_max)
        cx_opt=[c_x[i]]
        cy_opt=[c_y[i]]
    else:
        cx_opt=coord_opt(c_x,w,w_total)
        cy_opt=coord_opt(c_y,w,w_total)

    # Organizar el o los puntos óptimos
    if len(cx_opt)+len(cy_opt)==2:
        opt=([cx_opt[0],cy_opt[0]])
        tipo="a"
    elif len(cx_opt)==2 and len(cy_opt)==1:
        opt=([cx_opt[0],cy_opt[0]],[cx_opt[1],cy_opt[0]])
        tipo="b"
    elif len(cx_opt)==1 and len(cy_opt)==2:
        opt=([cx_opt[0],cy_opt[0]],[cx_opt[0],cy_opt[1]])
        tipo="b"
    else:
        opt=([cx_opt[0],cy_opt[0]],[cx_opt[0],cy_opt[1]],[cx_opt[1],cy_opt[0]],[cx_opt[1],cy_opt[1]])
        tipo="c"
    
    # Calcular función objetivo:
    l_costo=[]
    for i in range(len(w)):
        distancia=abs(cx_opt[0]-c_x[i])+abs(cy_opt[0]-c_y[i])
        costo=w[i]*distancia
        l_costo.append(costo)
    z=round(sum(l_costo),nd)

    return opt,tipo,z

## d. Generar matriz Z
def gen_z(c_x,c_y,w,nd):
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
            costo=0
            
            for k in range(len(c_x)):
                costo+=w[k]*(abs(i-c_x[k])+abs(j-c_y[k]))
            
            z=round(costo,nd)
            l_z.append(z)

        m_z.append(l_z)

    return (v_x,v_y,m_z)

## e. Guardar archivo de resultados.xlsx
def resultados (archivo,opt,v_x,v_y,m_z):
    """
    Crear y guardar el archivo.xls con los resultados del pograma en la carpeta Resultados.
    """
    
    # Extraer los puntos óptimos y el costo minimo.
    p_opt,tipo, z=opt

    # Ubicarse en la ruta de Resultados
    if os.path.exists("Resultados")==False: # Si la carpeta "Resultados" no existe:
        os.mkdir("Resultados") # Crear la carpeta de resultados
        
    # Crear los DataFrames

    ## DataFrame de el o los puntos óptimos.
    if tipo=="a": # Si es un punto óptimo
        coord_x=p_opt[0]
        coord_y=p_opt[1]
        title_opt="Punto Óptimo"
        df_optimo=pd.DataFrame({"Coordenada x":[coord_x,""],"Coordenada y":[coord_y,""]})
    elif tipo=="b": # Si hay dos puntos 
        coord_x=[p_opt[0][0],p_opt[1][0]]
        coord_y=[p_opt[0][1],p_opt[1][1]]
        title_opt="Puntos Óptimos"
        df_optimo=pd.DataFrame({"Punto":["a","b"],"Coord_x":coord_x,"Coord_y":coord_y})
    else:
        coord_x=[p_opt[0][0],p_opt[1][0],p_opt[2][0],p_opt[3][0]]
        coord_y=[p_opt[0][1],p_opt[1][1],p_opt[2][1],p_opt[3][1]]
        title_opt="Puntos Óptimos"
        df_optimo=pd.DataFrame({"Punto":["a","b","c","d"],"Coord_x":coord_x,"Coord_y":coord_y})

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
    hoja_1.write(7,0,"Costo mínimo z:",negrita)
    hoja_1.write(7,1,str(z))
    hoja_1.set_column('A:A', len("Costo mínimo z:"))
    hoja_1.set_column('B:B', len("Coordenada Y"))

    ## Guardar documento.
    doc.save() 
    doc.close()

    return None

## e. Hacer los gráficos

def graficos (archivo,opt,v_x,v_y,m_z,c_x,c_y):
    "Crea el gráficos de costos y el gráfico de ubicaciones"

    # Extarer punto o segamento óptimo:
    p_opt,tipo,z=opt
    
    # Crear gráfico de costos

    ## Crear arrays.
    X=np.array(v_x)
    Y=np.array(v_y)
    X, Y = np.meshgrid(X, Y)
    Z=np.transpose(np.array(m_z))

    ## Crear figura 3d
    fig = plt.figure(figsize=[11,11],dpi=60)
    ax = fig.gca(projection='3d')

    ## Dibujar la superficie
    ax.plot_surface(X, Y, Z, cmap=cm.jet, rstride=1, cstride=1)

    ## Títulos
    plt.title("Gráfica de costos de "+archivo[:-4]+"\n")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    ax.set_zlabel("Costo",labelpad=25)

    ## Modificar eje z.
    ax.set_zlim(z-0.5) # Inciar el costo optimo menos 0.5
    ax.zaxis.set_major_locator(LinearLocator(10)) # Cantidad de marcadores 10
    ax.zaxis.set_major_formatter(FormatStrFormatter('       %0.2E')) # Decimales de los marcadores 1

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
    if tipo=="a": # Si es un punto óptimo
        coord_x=p_opt[0]
        coord_y=p_opt[1]     
    elif tipo=="b": # Si hay dos puntos 
        coord_x=[p_opt[0][0],p_opt[1][0]]
        coord_y=[p_opt[0][1],p_opt[1][1]]
    else:
        coord_x=[p_opt[0][0],p_opt[1][0],p_opt[2][0],p_opt[3][0]]
        coord_y=[p_opt[0][1],p_opt[1][1],p_opt[2][1],p_opt[3][1]]
    
    plt.plot(coord_x,coord_y,"ro", label="Óptimo",markersize=7,markeredgecolor="white")  
    
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

def c_mapa(p_opt, tipo, ruta, nombre):
    """
    Genera un mapa de la prefactura de Colombia, con sus departamentos y señala los puntos indicados.
    Además guarda el mapa el un archivo .html con la ruta y el nombre indicado, este debe tener la extensión ".html".
    """
    
    # Importar folium

    try:
        import folium
        
    except(Exception):
        
        print("""Usted no tiene instalado el módulo 'folium', para hacerlo ejecute la celda siguiente celda con el comando
            'pip install folium', espere hasta termine el proceso, resustare el kernel del notebook y vuelva a correr este programa.""")
        
    # Crear mapa
    mapa=folium.Map(location=[4.598889, -74.080833],zoom_start=6, control_scale=True)
    
    # Cargar croquis departamentos
    folium.GeoJson(departments_geojson,name='departamentos',style_function=lambda feature: {'fillColor': "yellowgreen",'fillOpacity': 0.5,'weight': 1,'color': 'darkgreen'}).add_to(mapa)
    
    # Poner marcador a la cápital
    folium.Marker(coord_cap, tooltip=capital,icon=folium.Icon(color='red')).add_to(mapa)
    
    # Poner marcador a los departamentos
    for row in df_departamentos.itertuples():
        mapa.add_child(folium.Marker(location=[row.LAT,row.LOG],tooltip=row.C,icon=folium.Icon(color='gray')))
    
    # Poner marcador a las zonas francas
    for row in df_zfrancas.itertuples():
        mapa.add_child(folium.Marker(location=[row.LATI,row.LOGI],tooltip=row.P,icon=folium.Icon(color='orange')))

    # Poner marcador al punto o los puntos óptimos:
        
        ## Dibujar los puntos de las ubicaciones óptimas
    if tipo=="a": # Si es un punto óptimo
        coord_x=p_opt[0]
        coord_y=p_opt[1]
        folium.CircleMarker(location=[coord_y,coord_x], tooltip="Óptimo", radius=10,color='crimson', fill=True, fill_color='crimson').add_to(mapa)
        
    elif tipo=="b": # Si hay dos puntos 
        coord_x=[p_opt[0][0],p_opt[1][0]]
        coord_y=[p_opt[0][1],p_opt[1][1]]
        
        folium.CircleMarker(location=[coord_y[0],coord_x[0]], tooltip="Óptimo", radius=10,color='crimson', fill=True, fill_color='crimson').add_to(mapa)
        folium.CircleMarker(location=[coord_y[1],coord_x[1]], tooltip="Óptimo", radius=10,color='crimson', fill=True, fill_color='crimson').add_to(mapa)
    else:
        coord_x=[p_opt[0][0],p_opt[1][0],p_opt[2][0],p_opt[3][0]]
        coord_y=[p_opt[0][1],p_opt[1][1],p_opt[2][1],p_opt[3][1]]
        folium.CircleMarker(location=[coord_y[0],coord_x[0]], tooltip="Óptimo", radius=10,color='crimson', fill=True, fill_color='crimson').add_to(mapa)
        folium.CircleMarker(location=[coord_y[1],coord_x[1]], tooltip="Óptimo", radius=10,color='crimson', fill=True, fill_color='crimson').add_to(mapa)
        folium.CircleMarker(location=[coord_y[2],coord_x[2]], tooltip="Óptimo", radius=10,color='crimson', fill=True, fill_color='crimson').add_to(mapa)
        folium.CircleMarker(location=[coord_y[3],coord_x[3]], tooltip="Óptimo", radius=10,color='crimson', fill=True, fill_color='crimson').add_to(mapa)
        
    mapa.save(ruta+nombre)
    return mapa

def main(ingreso=1,cm=0):
    """
    Al ingresar un archivo con las coordenadas (x,y) y con sus peso 'w' asociados a cada punto objetivo, 
    encuentra el punto o los puntos óptimos para ubicar la instalación manejando un modelo de 
    distancia rectilíneo, genera una matriz de costos, devuelve un archivo de excel con los 
    resultados anteriores y guarda los gráficos de costos y ubicaciones.
    """

    "1. Leer archivo de coordenadas"

    # Ingresar archivo de coordenadas.
    if ingreso==1:
        a_coord=input("Por favor ingrese el archivo que contiene las coordenadas de los puntos objetivos,\npor ejemplo, 'Municipios.txt':\n")
    elif ingreso=="e":
        a_coord="Ej_MsR.txt"
    elif ingreso=="p1":
        a_coord="Region_Andina.txt"
        
    # Leer el archivo de coordenadas.
    x,y,w,d=lectura_datos(a_coord)
    "2. Calcular el punto o el segmento óptimo."
    opt=optimo(x,y,w,d)

    "3. Calcular matríz de costos z"
    vx,vy,mz=gen_z(x,y,w,d)  
    
    "4. Crear el archivo de resultados"
    resultados(a_coord,opt,vx,vy,mz)
    
    "5. Crear gráficos"
    graficos(a_coord,opt,vx,vy,mz,x,y)
    
    "BONUS ---> 6. Crear mapa" 
    try:
        if cm==1:
            m_ubicaciones=c_mapa(opt[0], opt[1], "Resultados/", "Mapa_Maquila_JKshoes.html")

            return m_ubicaciones
        else:
            return None
    except(Exception):
        return None

if __name__=="__main__":
    main()