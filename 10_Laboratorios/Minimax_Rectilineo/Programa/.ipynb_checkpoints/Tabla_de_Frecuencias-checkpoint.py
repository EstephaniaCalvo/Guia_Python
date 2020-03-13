# Título: Tabla de Frecuencias
# Autor: Estephania Calvo Carvajal

# -2. Importar módulos
import os 
import statistics
import pandas as pd
import matplotlib.pyplot as plt
import random

# -1. Funciones auxiliares 

## a. Leer y almacenar datos de entrada.
def lectura_entradas (archivo_entradas): #Crear la función lectura_entradas con parámetros de entrada: nombre del archivo.txt con la información de las entradas.
    
    # Definir listas de almacenamiento
    l_archivos=[] # Crear lista vacía para los nombres de los archivos de datos.
    l_k=[] # Crear una lista vacía para el número de clases de cada set de datos.
    l_colores=[] # Crear una lista vacía para los colores de los gráficos.

    # Definir la lista de colores para elegir aleatoriamente.
    colores=['aquamarine', 'bisque', 'blue', 'blueviolet', 'brown', 'burlywood', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'crimson', 'cyan', 'green', 'lightblue', 'lightcoral', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightslategrey', 'lime', 'limegreen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'moccasin', 'navajowhite', 'navy', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'peachpuff', 'peru', 'pink', 'plum', 'purple', 'rebeccapurple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'sienna', 'skyblue', 'slateblue', 'slategrey', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'yellow', 'yellowgreen']

    # Leer el archivo de entradas
    ruta_entradas=archivo_entradas # Extraer la ruta del archivo de entradas.txt ingresado.
    with open(ruta_entradas) as file: # Abrir el archivo.
        for i in file: # Por cada elemento del archivo:
            entradas=i.split(";") # convertir cada línea en un lista y guardarla en la variable entradas
            l_archivos.append(entradas[0]) # Agregar el nombre del archivo de datos a la lista de archivos de datos.
            l_k.append(int(entradas[1])) # Convertir y agregar el número de clase a lista de números de clase
            color=entradas[2]
            if "\n" in color:
                color=entradas[2][:-1]
            if color=="a": # Si el colores es 'a':
                color=random.choice(colores) # Escoja un color de la lista colores aleatoriamente
            l_colores.append(color) # Agregar el color a lista de colores a usar.
    file.close() # Cerrar archivo.
    entradas=(l_archivos,l_k,l_colores)
    return (entradas) # Devolver tupla con la lista de archivos, la lista de números de clase y colores.

## b. Lectura y almacenamiento de datos.
def lectura_datos (archivo_datos, l_datos): #Crear la función lectura_datos con parámetros de entrada: nombre del archivo.txt con los datos.
    data=[] # Crear lista vacía para almacenar los datos.

    with open(archivo_datos) as file: # Abrir el archivo.
        for i in file: # Por cada elemento del archivo:
            data.append(float(i)) # Convertir el elemento a flotante y agregarlo a lista data.
    file.close() # Cerrar archivo.
    l_datos.append(data) # Almacenar el conjunto de datos actuales en la lista de datos
    return (data) # Devolver lista de datos

## c. Calcular las medidas de centramiento y dispersión:  
def medidas (data): # Crear la función medidas con parámetros de entrada: lista de datos.
    # Medidas de centramiento
    r_media= statistics.mean(data) # Calcular la media
    r_mediana= statistics.median(data) # Calcular la mediana
    
    # Calculara la moda
    valores=list(set(data)) # Extraer valores de los datos y guardarlos en una lista.
    l_fr = [[data.count(x)] for x in set(valores)] # contar cuantas veces esta cada valor en la lista de datos y guardar en una lista de frecuencias
    fr_max=max(l_fr) # Guardar la frecuencia de la moda
    n_modas=l_fr.count(fr_max) # Contar cuantas veces se repite la frecuencia de la moda
    if n_modas>1: # Si hay mas de una moda
        r_moda=[] # Crear una lista para guardar los valores de moda.
        for i in range(len(l_fr)): # Para cada elemento en la lista de frecuencias
            if l_fr[i]== fr_max: # Si la frecuencia actual es igual a la frecuencia de la moda
                r_moda.append(valores[i]) # Agregue el valor con esa frecuencia a lista de la moda.
                r_moda.sort()
    else:
        r_moda= statistics.mode(data) # Calcular la moda
    
    # Medidas de dispersión
    r_desviacion= statistics.stdev(data) # Calcular la desviación estándar
    r_rango= max(data)-min(data) # Calcular el rango
    r_varianza=statistics.variance(data) # Calcular la varianza

    r_medidas=(r_media, r_mediana, r_moda, r_desviacion, r_rango, r_varianza) # Guardar resultados en una tupla
    return(r_medidas) # Devolver la tupla con los resultados.

## d. Definir las clases
def clases (data, k): # Crear la función medidas con parámetros de entrada: lista de datos.
    
    c=list(plt.hist(data,k)[1]) # Extraer del gráfico la lista de clases.
    plt.close()# Cerrar el gráfico
    
    i_clases=[] # Crear lista vacía para almacenar las clases.
    
    n_enteros=[1 for x in data if x.is_integer()] # Contar los números enteros
    
    if sum(n_enteros)==len(data):# Si todos los números son enteros
        nd=1 # El número de decimales de las clases es 1
    else: # Si no, enontar la cantidad decimales de cada dato y escoger el mayor.
        decimales=[(len(str(x))-str(x).index(".")) for x in data]
        nd=max(decimales)
        
    # Crear intervalos de clase
        
    for i in range(len(c)-1): # Por cada clase haga
        inferior=round(c[i],nd) # Límite inferior
        superior=round(c[i+1],nd) # Límite superior
        i_clases.append([inferior,superior]) # Añadir Límites a la lista de intervalos de clase.

    return i_clases # Devolver la lista de intervalos de clase.

## e. Calcular frecuencias
def frecuencias (data,k): # Crear la función frecuencias con parámetros de entrada: lista de datos y números de clases.
       
    n=len(data) # Calcular el número de datos.
      
    fa=list(plt.hist(data,k)[0]) # Extraer del gráfico la lista de frecuencias
    plt.close()
    fr=[x/n for x in fa] # Calcular las frecuencias relativas
    
    # Calcular las frecuencias absolutas acumuladas
    faa=[fa[0]]
    for i in fa[1:]:
        faa.append(faa[-1]+i)
        
    fra=[x/n for x in faa] # Calcular las frecuencias relativas acumuladas
    
    tabla=(fa,fr,faa,fra) # Crear una tupla que contenga las listas de frecuencias.
    return tabla # Devolver la tupla de listas.

## f. Guardar archivo de resultados.xlsx
def resultados (r_clases,tabla,r_medidas,archivo): # Crear la función frecuencias con parámetros de entrada: lista de clases, lista de datos y archivo de datos.
    fa, fr, faa, fra=tabla # Abrir la tupla tabla y sacar las listas frecuencias.
    media, mediana, moda, desviacion, rango, varianza=r_medidas # Abrir la tupla r_medidas  y sacar los resultados de las medidas.
    
    # Ubicarse en la ruta de Resultados
    if os.path.exists("Resultados")==False: # Si la carpeta "Resultados" no existe:
        os.mkdir("Resultados") # Crear la carpeta de resultados
        
    # Crear los DataFrames
    df_frecuencias = pd.DataFrame({"Clases":r_clases, "FA":fa, "FR":fr, "FAA":faa, "FRA":fra})
    df_medidas=pd.DataFrame({"Medidas":["Media","Mediana","Moda","Desviación estándar","Rango","Varianza"],"":[media, mediana, moda, desviacion,rango,varianza]})
    
    # Crear el documento
    doc=pd.ExcelWriter('Resultados/Resultados_'+archivo[:-4]+'.xlsx', engine='xlsxwriter')
    
    ## Escribir resultados
    df_medidas.to_excel(doc, sheet_name='Medidas',index=False, startrow=2, header=False)
    df_frecuencias.to_excel(doc, sheet_name='Tabla de frecuencias', index=False, startrow=2)

    libro=doc.book # Abrir libro
    hoja_1=doc.sheets['Medidas'] # Abrir la hoja 1
    hoja_2=doc.sheets['Tabla de frecuencias'] # Abrir la hoja 2

    # Formato de los números
    formato_numeros=libro.add_format({'num_format': '#,##0.00'})
    ancho=len(str(r_clases[0]))
    
    hoja_1.set_column('B:B', None, formato_numeros) # Aplicar formato de números a la columna B de la hoja 1.
    hoja_1.set_column('A:A', 18)# Aplicar ancho de columna a la columna A de la hoja 2.

    hoja_2.set_column('A:A', ancho) # Definir el tamaño de la columna A de la hoja 2.
    # Ancho de la columna= tamaño de la cadena una tupla de las clases.
    hoja_2.set_column('C:C', None, formato_numeros) # Aplicar formato de números a la columna C de la hoja 2.
    hoja_2.set_column('E:E', None, formato_numeros) # Aplicar formato de números a la columna E de la hoja 2.

    # Formato de títulos
    formato_titulo=libro.add_format({'bold': True, 'font_size': 16}) 
    
    ## Escribir los títulos
    hoja_1.write(0, 0, 'Medidas de centramiento y dispersión'.title(), formato_titulo)
    hoja_2.write(0, 0, 'Tabla de frecuencias'.title(), formato_titulo)
    
    doc.save() ## Guardar documento.
    
## g. Hacer el histograma
def histograma (data,r_clases,k,fa,archivo,color): # Crear la función frecuencias con parámetros de entrada: lista de clases, lista de datos, archivo de datos y color del gráfico.

    ## Títulos de los ejes y del gráfico
    plt.xlabel('Datos')
    plt.ylabel('Frecuencia absoluta')
    plt.title('Histograma de '+archivo[:-4])

    ## Definir mallas.
    plt.grid(b=True, which='major', axis='y', color='#999999', linestyle=':') # Crear malla principal.
    #   Malla principal para el eje y, con color gris claro, y estilo de línea punteada.
    plt.minorticks_on() # Habilitar la malla secundaria.
    plt.grid(b=True, which='minor', axis='y', color='#999999', linestyle=':', alpha=0.2) # Crear malla secundaria.
    #   Malla secundaria para el eje y, con color gris claro, y estilo de línea punteada.

    ## Crear histograma.
    plt.hist(data,k,facecolor=color, alpha=0.5, linewidth=2, edgecolor=color)

    # Crear etiquetas
    etiquetas_x=[] # Crear listas de etiquetas del eje x.
    for i in r_clases: # Por cada clase haga:
        etiquetas_x.append(i[0]) # Agregar a la lista de etiquetas del eje x el límite inferior de la clase.
    etiquetas_x.append(r_clases[-1][1]) # Agregar a lista de etiquetas del eje x el límite superior de la última clase.
    plt.xticks(etiquetas_x) # Poner las etiquetas.

    plt.savefig('Resultados/Histograma_de_'+archivo[:-4]+'.png') # Guardar el gráfico.
    plt.show(block=False) # Mostrar el grafico, sin interrumpir el programa
    plt.close() # Cerrar el gráfico
    return None # No devolver nada

## h. Hacer el histograma combinado
def hist_comparativo (l_data,l_k,l_colores,l_archivos,nombre): # Crear la función frecuencias con parámetros de entrada: lista de clases, lista de datos, archivo de datos, color del gráfico y nombre del archivo de entradas.

    ## Títulos de los ejes y del gráfico
    plt.xlabel('Datos')
    plt.ylabel('Frecuencia absoluta')
    plt.title('Histograma_Comparativo'+nombre)

    ## Definir mallas.
    plt.grid(b=True, which='major', axis='y', color='#999999', linestyle=':') # Crear malla principal.
    #   Malla principal para el eje “y” con color gris claro, y estilo de línea punteada.
    plt.minorticks_on() # Habilitar la malla secundaria.
    plt.grid(b=True, which='minor', axis='y', color='#999999', linestyle=':', alpha=0.2) # Crear malla secundaria.
    #   Malla secundaria para el eje y, con color gris claro, y estilo de línea punteada.

    ## Crear histograma.
    # Por cada archivo de datos haga:
    for i in range(len(l_archivos)):
        # Crear un histograma
        plt.hist(l_data[i],l_k[i],facecolor=l_colores[i], alpha=0.5, linewidth=2, edgecolor=l_colores[i],label=l_archivos[i][:-4])
    plt.legend(loc='best', frameon=True) # Mostrar la leyenda en el mejor lugar, en un recuadro.

    plt.savefig('Resultados/Histograma_Comparativo_de_'+nombre+'.png') # Guardar el gráfico.
    plt.show(block=False) # Mostrar el grafico, sin interrumpir el programa
    plt.close() # Cerrar el gráfico

    return None # No devolver nada

# 0. Programa principal
def main():
    """
    Al ingresar uno o varios archivos de datos, asociados a un numero de clase, y a un color, este programa calcula y guarda para cada paquete de datos, las medidas de centramiento y dispersión, la tabla de frecuencias, y su histograma.
    """

    "0. Pedir y leer archivo de entradas"
    # Ingresar archivo de entrada.
    a_entradas=input("Por favor ingrese el archivo que contiene las entradas, por ejemplo, 'Entradas.txt':\n")
    l_entradas=lectura_entradas(a_entradas) # Leer el archivo de entradas
    l_archivos,l_k,l_colores=l_entradas # Extraer lista de archivos, lista de números de clase, y colores.
    l_datos=[] # Crear una lista vacía para almacenar las listas de datos.
    
    "Realizar el algoritmo de tabla de frecuencias e histograma"
    # Por cada archivo de entradas haga:
    for i in range(len(l_archivos)):
        # Crear variable para almacenar el nombre del archivo actual.
        n_archivo=l_archivos[i] # Hacer n_archivo igual al nombre del archivo actual
        # Crear variable para almacenar el número de clase actual.
        n_k=l_k[i] # Hacer n_k igual al número de clase actual
        
        "1. Leer y almacenar los datos."
        datos=lectura_datos(n_archivo, l_datos) # Leer y almacenar datos.
        
        "2. Calcular las medidas de centramiento y dispersión"
        m_centramiento= medidas (datos) # Calcular y almacenar los resultados de las medidas.
        rango=m_centramiento[4] # Extraer el rango
        
        "3. Crear la tabla de frecuencias" 
        "3.1. Definir las clases"
        intervalos=clases(datos,n_k) # Calcular y almacenar las clases.
        "3.2. Calcular las frecuencias"
        t_frecuencias=frecuencias (datos,n_k) # Calcular y almacenar las frecuencias.
        f_absoluta=t_frecuencias[0] # Extraer la frecuencia absoluta 

        "4. Crear y guardar el archivo.xlsx con los resultados"
        resultados(intervalos,t_frecuencias,m_centramiento,n_archivo) # Crear y guardar el archivo de Resultados_Archivo.xlsx.
        
        "5. Crear y guardar el histograma"
        histograma(datos,intervalos,n_k,f_absoluta,n_archivo,l_colores[i]) # Crear, mostrar y guardar la imagen Histograma de Archivo.png.
    
    "6. Crear y guardar histograma comparativo"
    if len(l_archivos)>1: # Si hay más de un archivo de datos
        hist_comparativo(l_datos,l_k,l_colores,l_archivos,a_entradas[:-4])# Crear, mostrar y guardar histograma comparativo.
        
if __name__=='__main__':
    main()