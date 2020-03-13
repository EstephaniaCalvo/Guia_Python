# Título: testing_MR.py
# Autor: Estpehania Calvo Carvajal

# Import statements
import os
import pandas as pd
import sys
from test_var_MR import mz1,vx1,vy1,mz2,vx2,vy2,mz3,vx3,vy3

# Caso 1: Segmento óptimo.
cx_1,cy_1,nd_1=([2.1, 1.2, 3.8, 5.9, 6.5, 10.0, 8.1, 4.3, 0.0, 7.0], [4.0, 1.1, 2.2, 1.0, 7.5, 3.0, 9.0, 8.7, 11.0, 5.6], 2)

# Caso 2: Punto optimo.
cx_2,cy_2,nd_2=([2.0, 1.0, 3.0, 5.0, 6.0, 10.0, 8.0, 4.0, 0.0, 7.0, 0.0, 0.0, 10.0, 10.0], [4.0, 1.0, 2.0, 0.0, 7.0, 3.0, 6.0, 8.0, 10.0, 5.0, 10.0, 0.0, 10.0, 0.0], 1)

# Caso 3: Datos negativos, y con diferente cantidad decimales.
cx_3,cy_3,nd_3=([-10.42, -2.42, -1.32, -18.47, -6.72, -17.79, -5.4, -10.95, -20.98, -3.87, -11.13, -9.26, -16.22, -14.99, -9.67, -3.1, -20.79, -17.34, -5.66, -1.09, -9.99, -9.08, -3.46, -0.78, -0.16, -10.85, -19.89, -4.53, -11.52, -20.57], [-18.63, -15.25, -2.63, -1.76, -14.27, -14.49, -1.94, -17.75, -22.06, -18.17, -22.47, -14.38, -16.76, -19.9, -17.39, -15.98, -0.49, -10.94, -18.53, -8.57, -6.23, -9.62, -13.52, -10.71, -3.36, -15.35, -23.97, -18.89, -15.95, -1.72], 3)
    
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
    
    1. Caso 1: Entradas con la misma cantidad de decimales.
    2. Caso 2: Entradas con números enteros.
    3. Caso 3: Entrada con números negativos y diferente cantidad de decimales.
---------------------------------------------------------------------------------------------------
    """)

    # Definir entradas
    lr=[fun("test_1.txt"), fun("test_2.txt"), fun("test_3.txt")]

    # Comprobar las salidas esperadas
    s_1=(cx_1,cy_1,nd_1)
    s_2=(cx_2,cy_2,nd_2)
    s_3=(cx_3,cy_3,nd_3)
    
    ls=[s_1, s_2, s_3]
    
    # Realizar el test
    resultado=test(lr,ls)
    
    return resultado

def test_optimo(fun):
    "Prueba la función optimo"

    print("""
---------------------------------------------------------------------------------------------------
    test_optimo
    
    Casos:
    
    1. Caso 1: Un segmento óptimo.
    2. Caso 2: Un punto óptimo.
---------------------------------------------------------------------------------------------------
    """)
    
    # Definir entradas
    lr=[fun(cx_1,cy_1,nd_1), fun(cx_2,cy_2,nd_2)]
    
    # Comprobar las salidas esperadas
    s_1=([(4.65, 6.65), (3.05, 5.05)], 9.0) 
    s_2=((5.0, 5.0), 10.0)
    
    ls=[s_1,s_2]
    
    resultado=test(lr,ls)
    
    return resultado

def test_gen_z(fun):
    "Prueba la función gen_z"
    
    print("""
---------------------------------------------------------------------------------------------------
    test_gen_z
    
    Casos:
    
    1. Caso 1: Datos con números positivos.
    2. Caso 2: Datos con números negativos.
---------------------------------------------------------------------------------------------------
    """)

    # Definir entradas
    lr=[fun(cx_1,cy_1,nd_1), fun(cx_3,cy_3,nd_3)]
    
    # Comprobar las salidas esperadas
    s_1=(vx1, vy1, mz1)
    s_2=(vx3, vy3, mz3)
    ls=[s_1, s_2]
    
    resultado=test(lr, ls)
    
    return resultado

def evaluacion():
    """
    Evalua automáticamente las funciones del programa Minimax_Rectilineo lectura_datos, optimo, y gen_z, y manualmente la generación de los gráficos, el archivo de resultados y el mapa. Finalmente almacena los resultados en un diccinario.
    """
    dir_test=os.getcwd()
    
    os.chdir("Proyectos")
    dir_proyectos=os.getcwd()
    proyectos=os.listdir()
    
    proyecto, lp1, lp2, lp3, lp4, lp5, lp6, lpb, notas=[],[],[],[],[],[],[],[],[]
    
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
            from Minimax_Rectilineo import lectura_datos, optimo, gen_z,main
            os.chdir("../../")
            
            # Evaluación automática --> Funciones principales
            try:
                lp1.append(test_lectura_datos(lectura_datos)*5)
            except(Exception):
                print("!ERROR! ---> La función no es correcta")
                lp1.append(0)

            try:
                lp2.append(test_optimo(optimo)*5)
            except(Exception):
                print("!ERROR! ---> La función no es correcta")
                lp2.append(0)
            try:
                lp3.append(test_gen_z(gen_z)*5)
            except(Exception):
                print("!ERROR! ---> La función no es correcta")
                lp3.append(0)
        
            try:
                os.chdir("Proyectos/"+i)  
                archivos=os.listdir()
                assert("Modulos" in archivos)
                if n_prac=="0":
                    main(1,1)
                elif n_prac=="1":
                    main("p1",1)
                elif n_prac=="2":
                    main("p2")

            except(Exception):
                print("""
    ---> La función principal no es correcta.
                        """)

            sys.modules.pop('Minimax_Rectilineo')

    # Evaluación Manual --> Presentación de resultados

            print("\nEvaluación Manual de Presentación de Resultados\n")

            print("Repondas la siguientes preguntas de acuerdo a una escala de 0 a 5, donde:\n")
            print("""
            0 = El archivo no fue creado.
            1= Fue creado pero está en blanco.
            2= Fue creado pero presenta un contenido erroneo.
            3= Tiene el contenido correcto pero no tiene aplicado nada del formato de presentación.
            4= Tiene el contenido correcto y el formato aplicado cumple con la mayoría de requisitos pero no todos.
            5= Tanto el contenido como todos los requisitos están aplicados correctamente.
                """)
            lp4.append(float(input("¿El gráfico de costos fue creado, mostrado y guardado correctamente?: ")))
            lp5.append(float(input("¿El gráfico de ubicaciones fue creado, mostrado y guardado correctamente?:" )))
            lp6.append(float(input("¿El archivo en excel fue creado, mostrado y guardado correctamente?: ")))

                # Evalaución de Bónus

            lpb.append(float(input("Con la escala anterior calfique si el mapa de la prefactura de Iwate,\ny los puntos óptimos para úbicar la el hospital, o el correspondiente a la práctica evaluada fue creada correctamente: ")))

            notas.append(((lp1[-1] + lp2[-1] + lp3[-1] + lp4[-1] + lp5[-1] + lp6[-1])/6) + lpb[-1]/5)

            os.chdir("../")
            
        except (Exception):
            print("Hay un error general en todo el proyecto, puede faltarle el archivo principal del programa")
            pruebas=[lp1, lp2, lp3, lp4, lp5, lp6, lpb]
            for i in pruebas:
                i.append(0)
            notas.append("Revisar a mano")
            
    os.chdir(dir_test)
    
    bd_calif={"Proyectos":proyectos,"Criterio 1":lp1,"Criterio 2":lp2,"Criterio 3":lp3,"Criterio 4":lp4,"Criterio 5":lp5,"Criterio 6":lp6, "Bonus":lpb,"Notas":notas}
    
    return bd_calif


def resultados(diccionario):
    """
    Crear y guardar el archivo.xls con los calificaciones del algoritmo Minisum Rectilineo.
    """
    
    ## DataFrame de la matríz.
    df_calificaciones=pd.DataFrame(diccionario)
    
    # Crear el documento
    doc=pd.ExcelWriter('Calficaciones_Minimax_Rectilineo.xlsx', engine='xlsxwriter')
    
    ## Escribir resultados
    df_calificaciones.to_excel(doc, sheet_name='Calificaciones',index=False, startrow=2)

    # Abrir libro y hojas del documento
    libro=doc.book
    hoja_1=doc.sheets['Calificaciones']

    # Títulos
    formato_titulo=libro.add_format({'bold': True, 'font_size': 16})
    hoja_1.write(0, 0, "Calificaciones Minimax_Rectilineo", formato_titulo)

    ## Guardar documento.
    doc.save() 
    doc.close()

    return None