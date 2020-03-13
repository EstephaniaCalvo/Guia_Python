# Título: Minimax Rectilíneo
# Autor: Estephania Calvo Carvajal

# -2. Importar módulos
import numpy as np
import pandas as pd
import os

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

#import sys 
#sys.path.append("Testing/")
#from test_MR import test_lectura_datos, test_optimo, test_gen_z

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

# print(lectura_datos("Coordenadas.txt"))
# test_lectura_datos(lectura_datos)

## b. Calcular segmento optimo.
def optimo(c_x,c_y,nd):
    """
    Calcula el punto optimo o el segmento optimo donde ubicar la instalación,
    a partir de la lista de coordenaadas de los objetivos
    """
    l_suma=[c_x[i]+c_y[i] for i in range(len(c_x))]
    l_resta=[c_y[i]-c_x[i] for i in range(len(c_x))]
    c1,c2,c3,c4=min(l_suma),max(l_suma),min(l_resta),max(l_resta)
    c5=max (c2-c1,c4-c3)
    z=c5/2
    opt_1=(round(0.5*(c1-c3)),round(0.5*(c1+c3+c5)))
    opt_2=(round(0.5*(c2-c4)),round(0.5*(c2+c4-c5)))
    
    if opt_1==opt_2:
        return opt_1,z
    else:
        segmento=[opt_1,opt_2]
        return segmento,z

# print(optimo([0.0, 82.0713, 39.4895, 58.6312, 44.3135, 37.2939, -56.4356, 24.6152, 40.3244, 76.9998, 19.1417, 67.6609, -19.1417, 3.7108, 53.1577, 33.0883, 23.2236, 31.4802, 31.7276, 28.1096, 20.8734, -2.1956, -5.4116, 46.6637, 53.8071, 60.8577, 24.9554, 30.7071, -0.3402, 25.8212, 40.6336, 32.4389, 65.4344, 49.1376, 22.2032, 35.7477, 87.1118, 35.5931, 8.6586, 15.1835, 2.814, 50.0344], [0.0, 137.3318, 81.36, 151.0618, 143.1763, 100.0379, 48.6738, 51.6115, 85.4419, 99.605, -3.3707, 145.4956, 24.2132, 54.6729, 163.4313, 147.0418, 27.1509, 118.9941, -13.1735, 31.6658, 36.1497, -19.9457, 23.3473, 121.6844, 120.3856, 126.4776, 10.545, -2.3502, 42.489, 79.7211, 108.3873, 61.6617, 92.3379, 130.2503, 85.8749, 71.7737, 140.486, 126.4157, 28.759, 46.7874, 15.3381, 106.2226]))
# print(optimo([2.0, 1.0, 3.0, 5.0, 6.0, 10.0, 8.0, 4.0, 0.0, 7.0], [4.0, 1.0, 2.0, 1.0, 7.0, 3.0, 9.0, 8.0, 11.0, 5.0]))
# test_optimo(optimo)

## d. Generar matriz Z
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
                    z=distancia
            l_z.append(z)
        m_z.append(l_z)
    return (v_x,v_y,m_z)

# test_gen_z(gen_z)

## e. Guardar archivo de resultados.xlsx
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
    if len(p_opt)==2: # Si es un segmento óptimo
        title_opt="Segemento Óptimo"
        p_opt.sort()
        df_optimo=pd.DataFrame({"Segmento":["Desde","Hasta"],"Coord_x":p_opt[0],"Coord_y":p_opt[1]})
        
    else:
        title_opt="Punto Óptimo"
        df_optimo=pd.DataFrame({"Coordenada x":p_opt[0],"Coordenada y":p_opt[1]})

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

## f. Hacer los gráficos de costos

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
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    ## Dibujar la superficie
    ax.plot_surface(X, Y, Z, cmap=cm.jet, rstride=1, cstride=1)

    ## Títulos
    plt.title("Gráfica de costos de "+archivo[:-4])
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    ax.set_zlabel("Costo")

    ## Modificar eje z.
    ax.set_zlim(z-0.5) # Inciar el costo optimo menos 0.5
    ax.zaxis.set_major_locator(LinearLocator(10)) # Cantidad de marcadores 10
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.01f')) # Decimales de los marcadores 1

    ## Mostrar y guardar gráficos.
    plt.savefig("Resultados/Gráfico_de_Costos_de_"+archivo[:-4]+".png")
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
    if len(p_opt)<1:
        plt.plot(p_opt[0],p_opt[1],label="Óptimo",marker="o",markersize=7,markerfacecolor="red",markeredgecolor="white")
    else:
        plt.plot([p_opt[0][0],p_opt[1][0]],[p_opt[0][1],p_opt[1][1]],label="Óptimos",linestyle=":",color="white",marker="o",markersize=7,markerfacecolor="red",markeredgecolor="white")
        
    ## Ejes
    r_1=(max(c_x)-min(c_x))*0.01
    r_2=(max(c_y)-min(c_y))*0.01
    plt.axis([min(c_x)-r_1,max(c_x)+r_1,min(c_y)-r_2,max(c_y)+r_2])
    
    ## Títulos
    plt.title("Gráfico de Ubicaciones de "+archivo[:-4])
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

def main():
    """
    Al ingresar un archivo con coordenadas de puntos objetivos, calcula y guarda el punto o 
    el segmento óptimo para ubicar una instalación que garantice la cobertura de todos los objetivos, 
    la matríz de costos de 10,000 y guarda los gráficos de costos y de ubicaciones.
    """

    "1. Leer archivo de coordenadas"

    # Ingresar archivo de coordenadas.
    a_coord=input("Por favor ingrese el archivo que contiene las coordenadas de los puntos objetovos,\npor ejemplo, 'Municipios.txt':\n")
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

if __name__=="__main__":
    main()