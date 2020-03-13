# Título: Gen_data_tf
# Autor: Estephania Calvo

# Módulo - Generación de datos aleatorios
"""
Genera un archivo con números aleatorios normales o a partir de frecuencias de ocurrencia, 
según los parámetros indicados por el usuario.
"""

# Importar Módulos

import random
import os
import numpy as np

# Creación del archivo.txt
def escritura(l_datos,n_decimales,nombre):
    "Escribe en un archivo una lista de datos numéricos con los decimales indicados."
    
    i_d="{:."+str(n_decimales)+"f}"
    archivo=open(nombre,"w")
    for i in range(len(l_datos)):
        if i==len(l_datos)-1:
            archivo.write(i_d.format(l_datos[i]))
        else:
            archivo.write(i_d.format(l_datos[i])+"\n")
    archivo.close()
    return None

# Generador por distribución normal
def G_normal(nombre):
    """
    Genera datos aleatorios normales a partir de la media, la desviación estándar, 
    el número de dato y el número de decimales indicados.
    """
    
    n= int(input("Por favo ingrese el número de datos: "))
    n_decimales=int(input("Por favor ingrese el número de decimales que deben tener los datos: "))
    mu = float(input("Por favor ingrese el valor de la media: "))
    sigma= float(input("Por favor ingrese el valor de la desviación estándar: "))
    datos = np.random.normal(mu, sigma, n) #creando muestra de datos
    escritura(datos,n_decimales,nombre)
    return None
    
# Generador por frecuencia 
def G_frecuencia(nombre):
    """
    Genera datos aleatorios a partir de un valor máximo y mínimo, las frecuencias, 
    y el número de decimales indicado.
    """
    
    # Ingresar datos
    d_menor=float(input("Por favor ingrese el dato menor: "))
    d_mayor=float(input("Por favor ingrese el dato mayor: "))
    n_decimales=int(input("\nIngrese el número de decimales que deben tener los datos: "))

    rango=d_mayor-d_menor


    # Ingresar frecuencias
    frecuencias=[]
    f_max=int(rango) # número máximo de frecuencias

    ingreso=1
    c=1

    while ingreso==1 and c<=f_max:
        mensaje_1="\nPor favor ingrese la frecuencia de la clase No."+str(ingreso)+"\nSi no desea ingresar más frecuencias oprima Enter\n"
        mensaje_2="Puede ingresar "+str(f_max-c)+" frecuencias más"
        
        if c==f_max:
            mensaje_1="\nEsta es la útima frecuencia que puede ingresar:\nSi no desea ingresar más frecuencias oprima Enter\n"
            mensaje_2="Hemos terminado, gracias.\n"
            
        fr=input(mensaje_1)
        c+=1
        if fr.isnumeric():
            fr=int(fr)
            frecuencias.append(fr)
            print(mensaje_2)
        else:
            ingreso=0
        

    # Generar intervalos.
    k=len(frecuencias) # número de frecuencias
    decimales=10**(n_decimales+1) # número de decimales operacionales.
    ventana=ventana=1/(decimales)
    tamaño=(rango+(ventana*2))/k
    l_inferior=d_menor-ventana
    intervalos=[]

    c=0
    while c<k:
            l_superior=l_inferior+tamaño
            intervalos.append((int(l_inferior*decimales), int(l_superior*decimales)))
            l_inferior=l_superior
            c+=1
                
    # Generar datos
    data=[]

    for i in range(k):
        for j in range(frecuencias[i]):
            if i==0 and j==0:
                data.append(round(d_menor,n_decimales))
            elif i==k-1 and j==(frecuencias[i]-1):
                data.append(round(d_mayor,n_decimales))
            else:
                dato=random.choice(range(intervalos[i][0],intervalos[i][1]))
                data.append(dato/(decimales))

    i_d="{:."+str(n_decimales)+"f}"
    archivo=open(nombre,"w")
    for i in range(len(data)):
        if i==len(data)-1:
            archivo.write(i_d.format(data[i]))
        else:
            archivo.write(i_d.format(data[i])+"\n")
    archivo.close()
    
    return None