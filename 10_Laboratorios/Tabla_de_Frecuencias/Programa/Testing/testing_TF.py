# Título: testing_TF.py
# Autor: Estpehania Calvo

# Import statements
import os
import pandas as pd
import sys
from test_var_TF import c, data_1, data_2, medidas_1, medidas_2, clases_1, clases_2, tabla_1, tabla_2

def test(r,s):
    try:
        for i in range(len(r)): 
            assert(r[i]==s[i])
            
            print("Caso",i+1,"Correcto\n")
            
        print("---> La función es correcta")
        return (1)  
    
    except(AssertionError):
        print("Revisar el caso",i+1)
        print("Los resultados esperados son:\n",s[i])
        print("Pero los resultados obtenidos son",r[i])
        return(0)
    except(Exception):
        print("!ERROR! ---> La función no es correcta")
        return(0)


def test_lectura_entradas(fun):
    "Prueba la función lectura_entradas"
    
    print("""
---------------------------------------------------------------------------------------------------
    test_lectura_entradas
    
    Casos:
    
    1. Caso 1: Una entrada.
    2. Caso 2: Dos entradas y color aleatorio
---------------------------------------------------------------------------------------------------
    """)

    # Definir entradas
    lr=[fun("test_1.txt"), fun("test_2.txt")]

    # Comprobar las salidas esperadas
    s_1=(['test_d1.txt'],[5],['salmon'])
    a=lr[1][2][0]
    if a in c:
        s_2=(['test_d2.txt','test_d1.txt'],[7,5],[a,'dodgerblue'])
    else:
        s_2=(['test_d2.txt','test_d1.txt'],[7,5],['a','dodgerblue'])
        print("El valor aleatorio no es válido, recuerde que tiene que ser alguno de esta lista:\n",c,"\n")
        
    ls=[s_1, s_2]
    
    # Realizar el test
    resultado=test(lr,ls)
    
    return resultado
        
def test_lectura_datos(fun):
    "Prueba la función lectura_datos"
    
    print("""
---------------------------------------------------------------------------------------------------
    test_lectura_datos
    
    Casos:
    
    1. Caso 1: Datos enteros positivos.
    2. Caso 2: Datos con decimales negativos.
---------------------------------------------------------------------------------------------------
    """)
    
    # Definir entradas
    ld=[]
    lr=[fun("test_d1.txt",ld), fun("test_d2.txt",ld)]
    
    # Comprobar las salidas esperadas
    s_1=data_1
    
    s_2=data_2
    
    if ld!=[s_1,s_2]:
        print("No se están acumulándo las listas de datos en la lista l_datos correctamente\n")
        print("l_datos esperado =",[s_1,s_2])
        print("l_datos obtenidos =",ld,"\n")
        ls=ld
    else:
        ls=[s_1, s_2]
    
    # Realizar el test
    resultado=test(lr,ls)
    
    return resultado

        
def test_medidas(fun):
    "Prueba la función medidas"
    
    print("""
---------------------------------------------------------------------------------------------------
    test_medidas
    
    Casos:
    
    1. Caso 1: Moda múltiple.
    2. Caso 2: Moda única.
---------------------------------------------------------------------------------------------------
    """)
    
    # Definir entradas
    lr=[fun(data_1), fun(data_2)]
    
    # Comprobar las salidas esperadas
    s_1=medidas_1
    
    s_2=medidas_2
    
    ls=[s_1, s_2]
    
    # Realizar el test
    resultado=test(lr,ls)
    
    return resultado
        
def test_clases(fun):
    "Prueba la función clases"
    
    print("""
---------------------------------------------------------------------------------------------------
    test_clases
    
    Casos:
    
    1. Caso 1: Datos con decimales.
    2. Caso 2: Datos enteros.
---------------------------------------------------------------------------------------------------
    """)
    
    # Definir entradas
    lr=[fun(data_1,5), fun(data_2,7)]
    
    # Comprobar las salidas esperadas
    s_1=clases_1
    
    s_2=clases_2
    
    ls=[s_1, s_2]
    
    # Realizar el test
    resultado=test(lr,ls)
    
    return resultado
        
def test_frecuencias(fun):
    "Prueba la función frecuencias"

    print("""
---------------------------------------------------------------------------------------------------
    test_frecuencias
    
    Casos:
    
    1. Caso 1: Datos con decimales.
    2. Caso 2: Datos enteros.
---------------------------------------------------------------------------------------------------
    """)
    
    # Definir entradas
    lr=[fun(data_1,5), fun(data_2,7)]
    
    # Comprobar las salidas esperadas
    s_1=tabla_1
    
    s_2=tabla_2
    
    ls=[s_1, s_2]
    
    # Realizar el test
    resultado=test(lr,ls)
    
    return resultado

def evaluacion():
    """
    Evalua automáticamente las funciones del programa Tabla_de_Frecuencias lectura_entradas, lectura_datos, medidas, clases y frecuencias, y manualmente la generación de los histogramas, y el archivo de resultados. Finalmente almacena los resultados en un diccinario.
    """
    dir_test=os.getcwd()
    
    os.chdir("Proyectos")
    dir_proyectos=os.getcwd()
    proyectos=os.listdir()
    
    proyecto, lp1, lp2, lp3, lp4, lp5, lp6, lp7, lp8, notas=[],[],[],[],[],[],[],[],[],[]
    
    n_prac=input("Ingrese el número de la práctica que quiere revisar, si desea ingresar a mano el archivo de datos ingrese 0: ")

    for i in proyectos:
        
        proyecto.append(i)

        print("""
        ________________________________________________________________
        
        Test del proyecto """+str(i)+"""
        ________________________________________________________________
        """)
        
        try:
            os.chdir(i)
            from Tabla_de_Frecuencias import lectura_entradas, lectura_datos, medidas, clases, frecuencias, main
            os.chdir("../../")
            
            # Evaluación automática --> Funciones principales
            try:
                lp1.append(test_lectura_entradas(lectura_entradas)*5)
            except(Exception):
                print("!ERROR! ---> La función no es correcta")
                lp1.append(0)
                
            try:
                lp2.append(test_lectura_datos(lectura_datos)*5)
            except(Exception):
                print("!ERROR! ---> La función no es correcta")
                lp2.append(0)

            try:
                lp3.append(test_medidas(medidas)*5)
            except(Exception):
                print("!ERROR! ---> La función no es correcta")
                lp3.append(0)
                
            try:
                lp4.append(test_clases(clases)*5)
            except(Exception):
                print("!ERROR! ---> La función no es correcta")
                lp4.append(0)
                
            try:
                lp5.append(test_frecuencias(frecuencias)*5)
            except(Exception):
                print("!ERROR! ---> La función no es correcta")
                lp5.append(0)
        
            try:
                os.chdir("Proyectos/"+i)  
                archivos=os.listdir()
                if n_prac=="0":
                    main(1)
                elif n_prac=="1":
                    main("p1")
                elif n_prac=="2":
                    main("T1")
                    main("T2")
                    main("T3")
                    
            except(Exception):
                print("""
    ---> La función principal no es correcta.
                        """)

            sys.modules.pop('Tabla_de_Frecuencias')

    # Evaluación Manual --> Presentación de resultados

            print("\nEvaluación Manual de Presentación de Resultados\n")

            print("Repondas la siguientes preguntas de acuerdo a una escala de 0 a 5, donde:\n")
            print("""
            0 = El o los archivos no fueron creados.
            1= Fue creado pero está en blanco.
            2= Fue creado pero presenta un contenido erroneo.
            3= Tiene el contenido correcto pero no tiene aplicado nada del formato de presentación.
            4= Tiene el contenido correcto y el formato aplicado cumple con la mayoría de requisitos pero no todos.
            5= Tanto el contenido como todos los requisitos están aplicados correctamente.
                """)
            lp6.append(float(input("¿Los histogramas de los sets de datos fueron creados, mostrados y guardados correctamente?: ")))
            lp7.append(float(input("¿El histograma comparativo fue creado, mostrado y guardado correctamente?:" )))
            lp8.append(float(input("¿Los archivos en excel fueron creados, mostrados y guardados correctamente?: ")))

            notas.append((lp1[-1] + lp2[-1] + lp3[-1] + lp4[-1] + lp5[-1] + lp6[-1] + lp7[-1] + lp8[-1])/8)

            os.chdir("../")
            
        except (Exception):
            print("Hay un error general en todo el proyecto, puede faltarle el archivo principal del programa")
            pruebas=[lp1, lp2, lp3, lp4, lp5, lp6, lp7, lp8]
            for i in pruebas:
                i.append(0)
            notas.append("Revisar a mano")
            
    os.chdir(dir_test)
    
    bd_calif={"Proyectos":proyectos,"Criterio 1":lp1,"Criterio 2":lp2,"Criterio 3":lp3,"Criterio 4":lp4,"Criterio 5":lp5,"Criterio 6":lp6, "Criterio 7":lp7,"Criterio 8":lp8,"Notas":notas}
    
    return bd_calif


def resultados(diccionario):
    """
    Crear y guardar el archivo.xls con los calificaciones del algoritmo Minisum Rectilineo.
    """
    
    ## DataFrame de la matríz.
    df_calificaciones=pd.DataFrame(diccionario)
    
    # Crear el documento
    doc=pd.ExcelWriter('Calficaciones_Tabla_de_Frecuencias.xlsx', engine='xlsxwriter')
    
    ## Escribir resultados
    df_calificaciones.to_excel(doc, sheet_name='Calificaciones',index=False, startrow=2)

    # Abrir libro y hojas del documento
    libro=doc.book
    hoja_1=doc.sheets['Calificaciones']

    # Títulos
    formato_titulo=libro.add_format({'bold': True, 'font_size': 16})
    hoja_1.write(0, 0, "Calificaciones Tabla_de_Frecuencias", formato_titulo)

    ## Guardar documento.
    doc.save() 
    doc.close()

    return None