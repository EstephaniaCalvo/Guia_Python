# Título: testing_MR.py
# Autor: Estpehania Calvo Carvajal

# Import statements
import os
import pandas as pd
import sys
from test_var_MsR import vx4, vy4, mz4, vx5, vy5, mz5

# Caso a1: Un punto tiene mas de la mitad del peso total.
cx_1,cy_1,w_1,nd_1,w_total_1=([0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 4.0], [7.0, 8.0, 10.0, 10.0, 10.0, 11.0, 12.0], [20, 2, 3, 1, 5, 1, 1], 1, 33)

# Caso a2: Solo hay un punto óptimo.
cx_2,cy_2,w_2,nd_2,w_total_2=([0.0, 0.0, 0.0, 1.0, 2.0, 3.0, 4.0], [7.0, 8.0, 10.0, 10.0, 10.0, 11.0,12.0], [1,2,3,4,5,6,7], 1, 28)

# Caso b1: Hay dos coordenadas 'x' óptimos, por lo tanto hay dos puntos óptimos.
cx_3,cy_3,w_3,nd_3,w_total_3=([0.0, 1.2, 2.1, 3.8, 4.3, 5.9, 6.5, 7.0, 8.1, 10.0], [4.0, 1.1, 2.2, 1.0, 7.5, 3.0, 9.0, 8.7, 11.0, 5.6],[1,2,3,4,5,1,2,3,4,5], 2, 30)

# Caso b2: Hay dos coordenadas 'y' óptimos, por lo tanto hay dos puntos óptimos.
cx_4,cy_4,w_4,nd_4,w_total_4=([3.22, 1.1, 2.2, 1.0, 7.5, 3.0, 9.0, 8.7, 11.0, 5.6], [1.0, 1.72, 2.01, 3.8, 4.3, 5.9, 6.5, 7.0, 8.91, 10.0], [1,2,3,4,5,1,2,3,4,5], 3, 30)

#Caso c: Tanto la coordenada 'x' y 'y' tienen dos óptimos, por lo tanto hay cuatro puntos óptimos.
cx_5,cy_5,w_5,nd_5,w_total_5=([-0.0, -0.0, -0.0, -1.0, -2.0, -3.0, -4.0, -5.0, -6.0, -7.0, -8.0, -10.0, -10.0, -10.0], [0.0, 1.0, 2.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 10.0, 10.0, 10.0, 11.0], [1,2,3,4,5,6,7,1,2,3,4,5,6,7], 1, 56)

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
    
def test_lectura_datos(fun):
    "Prueba la función lectura_datos"
    
    print("""
---------------------------------------------------------------------------------------------------
    test_lectura_datos
    
    Casos:
    
    1. Caso 1: Entradas de números enteros.
    2. Caso 2: Entradas con la misma cantidad de decimales.
    3. Caso 3: Entrada con diferente cantidad de decimales.
    4. Caso 4: Entrada con números negativos.
---------------------------------------------------------------------------------------------------
    """)

    # Definir entradas
    lr=[fun("test_1.txt"), fun("test_3.txt"), fun("test_4.txt"), fun("test_5.txt")]

    # Comprobar las salidas esperadas
    s_1=(cx_1,cy_1,w_1,nd_1)
    s_2=(cx_3,cy_3,w_3,nd_3)
    s_3=(cx_4,cy_4,w_4,nd_4)
    s_4=(cx_5,cy_5,w_5,nd_5)
    ls=[s_1,s_2,s_3,s_4]
    
    # Realizar el test
    resultado=test(lr,ls)
    
    return resultado

def test_coord_opt(fun):
    "Prueba la función coord_opt"
    
    print("""
---------------------------------------------------------------------------------------------------
    test_coord_opt
    
    Casos:
    
    1. Caso 1: Solo hay una coordenada óptima.
    2. Caso 2: Hay dos coordenadas óptimas.
---------------------------------------------------------------------------------------------------
    """)

    # Definir entradas
    lr=[fun(cx_2,w_2,w_total_2), fun(cx_5,w_5,w_total_5)]

    # Comprobar las salidas esperadas
    s_1=[2.0]
    s_2=[-5.0, -4.0]
    ls=[s_1,s_2]
    
    # Realizar el test
    resultado=test(lr,ls)
    
    return resultado

def test_optimo(fun):
    "Prueba la función optimo"

    print("""
---------------------------------------------------------------------------------------------------
    test_optimo
    
    Casos:
    
    1. Caso 1: Un punto tiene mas de la mitad del peso total.
    2. Caso 2: Solo hay un punto óptimo.
    3. Caso 3: Hay dos coordenadas 'x' óptimas, por lo tanto hay dos puntos óptimos.
    4. Caso 4: Hay dos coordenadas 'y' óptimas, por lo tanto hay dos puntos óptimos.
    5. Caso 5: Tanto la coordenada 'x' y 'y' tienen dos óptimos, por lo tanto hay cuatro puntos óptimos.
---------------------------------------------------------------------------------------------------
    """)
    
    # Definir entradas
    lr=[fun(cx_1,cy_1,w_1,nd_1), fun(cx_2,cy_2,w_2,nd_2), fun(cx_3,cy_3,w_3,nd_3), fun(cx_4,cy_4,w_4,nd_4), fun(cx_5,cy_5,w_5,nd_5)]
    
    # Comprobar las salidas esperadas
    s_1=([0.0, 7.0], 'a', 56.0) 
    s_2=([2.0, 10.0], 'a', 63.0)
    s_3=(([4.3, 5.6], [5.9, 5.6]), 'b', 165.9)
    s_4=(([5.6, 4.3], [5.6, 5.9]), 'b', 168.15)
    s_5=(([-5.0, 5.0], [-5.0, 6.0], [-4.0, 5.0], [-4.0, 6.0]), 'c', 371.0) 
    ls=[s_1,s_2,s_3,s_4,s_5]
    
    resultado=test(lr,ls)
    
    return resultado

def test_gen_z(fun):
    "Prueba la función gen_z"
    
    print("""
---------------------------------------------------------------------------------------------------
    test_gen_z
    
    Casos:
    
    1. Caso 1: Datos con mas de un decimal.
    2. Caso 2: Datos con números negativos.
---------------------------------------------------------------------------------------------------
    """)

    # Definir entradas
    lr=[fun(cx_4,cy_4,w_4,nd_4), fun(cx_5,cy_5,w_5,nd_5)]
    
    # Comprobar las salidas esperadas
    s_1=(vx4, vy4, mz4)
    s_2=(vx5, vy5, mz5)
    ls=[s_1, s_2]
    
    resultado=test(lr, ls)
    
    return resultado

def evaluacion():
    """
    Evalua automáticamente las funciones del programa Minisum_Rectilineo lectura_datos, coord_opt, optimo, y gen_z, y manualmente la generación de los gráficos, el archivo de resultados y el mapa. Finalmente almacena los resultados en un diccinario.
    """
    
    os.chdir("Proyectos")
    dir_proyectos=os.getcwd()
    proyectos=os.listdir()
    
    proyecto, lp1, lp2, lp3, lp4, lp5, lp6, lp7, lpb, notas=[],[],[],[],[],[],[],[],[],[]
    
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
            from Minisum_Rectilineo import lectura_datos, coord_opt, optimo, gen_z,main
            os.chdir("../../")
            
            # Evaluación automática --> Funciones principales
            try:
                lp1.append(test_lectura_datos(lectura_datos)*5)
            except(Exception):
                print("!ERROR! ---> La función no es correcta")
                lp1.append(0)

            try:
                lp2.append(test_coord_opt(coord_opt)*5)
            except(Exception):
                print("!ERROR! ---> La función no es correcta")
                lp2.append(0)

            try:
                lp3.append(test_optimo(optimo)*5)
            except(Exception):
                print("!ERROR! ---> La función no es correcta")
                lp3.append(0)
            try:
                lp4.append(test_gen_z(gen_z)*5)
            except(Exception):
                print("!ERROR! ---> La función no es correcta")
                lp4.append(0)
        
            try:
                os.chdir("Proyectos/"+i)  
                archivos=os.listdir()
                assert("Modulos" in archivos)
                if n_prac=="0":
                    main(1,1)
                elif n_prac=="1":
                    main("p1",1)

            except(Exception):
                print("""
    ---> La función principal no es correcta.
                        """)

            sys.modules.pop('Minisum_Rectilineo')

    # Evaluación Manual --> Presentación de resultados

            print("\nEvaluación Manual de Presentación de Resultados\n")

            print("Repondas la siguientes preguntas de acuerdo a una escala de 0 a 5, donde:\n")
            print("""
            0 = El archivo no fué creados
            1= Fue creado pero está en blanco.
            2= Fue creado pero presenta un contenido erroneo.
            3= Tiene el contenido correcto pero no tiene aplicado nada del formato de presentación.
                4= Tiene el contenido correcto y el formato aplicado cumple con la mayoría de requisitos pero no todos.
                5= Tanto el contenido como todos los requisitos están aplicados correctamente.
                """)
            lp5.append(float(input("¿El gráfico de costos fue creado, mostrado y guardado correctamente?: ")))
            lp6.append(float(input("¿El gráfico de ubicaciones fue creado, mostrado y guardado correctamente?:" )))
            lp7.append(float(input("¿El archivo en excel fue creado, mostrado y guardado correctamente?: ")))

                # Evalaución de Bónus

            lpb.append(float(input("Con la escala anterior calfique si el mapa de los departamentos de Colombia,\ny los puntos óptimos para úbicar la maquila fueron creados correctamente: ")))

            notas.append(((lp1[-1] + lp2[-1] + lp3[-1] + lp4[-1] + lp5[-1] + lp6[-1] + lp7[-1])/7) + lpb[-1]/5)

            os.chdir("../")
            
        except (Exception):
            print("Hay un error general en todo el proyecto, puede faltarle el archivo principal del programa")
            pruebas=[lp1, lp2, lp3, lp4, lp5, lp6, lp7, lpb]
            for i in pruebas:
                i.append(0)
            notas.append("Revisar a mano")
            
    os.chdir("../../")
    
    bd_calif={"Proyectos":proyectos,"Criterio 1":lp1,"Criterio 2":lp2,"Criterio 3":lp3,"Criterio 4":lp4,"Criterio 5":lp5,"Criterio 6":lp6,"Criterio 7":lp7, "Bonus":lpb,"Notas":notas}
    
    return bd_calif


def resultados(diccionario):
    """
    Crear y guardar el archivo.xls con los calificaciones del algoritmo Minisum Rectilineo.
    """
    
    ## DataFrame de la matríz.
    df_calificaciones=pd.DataFrame(diccionario)
    
    # Crear el documento
    doc=pd.ExcelWriter('Calficaciones_Minisum_Rectilineo.xlsx', engine='xlsxwriter')
    
    ## Escribir resultados
    df_calificaciones.to_excel(doc, sheet_name='Calificaciones',index=False, startrow=2)

    # Abrir libro y hojas del documento
    libro=doc.book
    hoja_1=doc.sheets['Calificaciones']

    # Títulos
    formato_titulo=libro.add_format({'bold': True, 'font_size': 16})
    hoja_1.write(0, 0, "Calificaciones Minisum_Rectilineo", formato_titulo)

    ## Guardar documento.
    doc.save() 
    doc.close()

    return None