# Título: testing_AHP.py
# Autor: Estpehania Calvo

# Import statements
import os
import pandas as pd
import sys
from test_var_AHP import t1_CC, t1_C3, t1_C1, t2_C2, vp_t1_CC, vp_t1_C1, vp_t2_C2, CR_t1_C1, CR_t2_C2, vp_alt_3, vp_crit_3, vp_t1_C3, l_bCR_3, l_alternativas_3, l_criterios_3,l_alternativas_ord_3, vp_alt_ord_3, v_resultado_3, vp_alt_2, vp_crit_2, l_bCR_2, l_alternativas_2, l_criterios_2, vp_alt_ord_2, v_resultado_2


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
    
    1. Caso 1: Criterios y alternativas con numerales.
    2. Caso 2: Crtierios y alternativas con texto.
---------------------------------------------------------------------------------------------------
    """)

    # Definir entradas
    lr=[fun("test_1.txt"), fun("test_2.txt")]

    # Comprobar las salidas esperadas
    s_1=(['1', '2', '3', '4'], ['A', 'B', 'C'], ['t1_CC.txt', 't1_C1.txt', 't1_C2.txt', 't1_C3.txt', 't1_C4.txt'])
    s_2=(['Precio', 'Calidad', 'Distancia'], ['Alphabet', 'Bit', 'Care'], ['t2_CC.txt', 't1_C1.txt', 't2_C2.txt', 't1_C3.txt'])
        
    ls=[s_1, s_2]
    
    # Realizar el test
    resultado=test(lr,ls)
    
    return resultado

def test_lectura_matrices(fun):
    "Prueba la función lectura_matrices"
    
    print("""
---------------------------------------------------------------------------------------------------
    test_lectura_matrices
    
    Casos:
    
    1. Caso 1: Matriz 4 x 4.
    2. Caso 2: Matriz 3 x 3.
---------------------------------------------------------------------------------------------------
    """)
    
    # Definir entradas
    lr=[fun("t1_CC.txt"), fun("t1_C3.txt")]
    
    # Comprobar las salidas esperadas
    s_1=t1_CC
    s_2=t1_C3
    
    ls=[s_1, s_2]
    
    # Realizar el test
    resultado=test(lr,ls)
    
    return resultado
        
def test_vector_pesos(fun):
    "Prueba la función vector_pesos"
    
    print("""
---------------------------------------------------------------------------------------------------
    test_vector_pesos
    
    Casos:
    
    1. Caso 1: Matriz 4 x 4.
    2. Caso 2: Matriz 3 x 3.
---------------------------------------------------------------------------------------------------
    """)
    
    # Definir entradas
    lr=[fun(t1_CC), fun(t1_C3)]
    
    # Comprobar las salidas esperadas
    s_1=vp_t1_CC
    s_2=vp_t1_C3
    
    ls=[s_1, s_2]
    
    # Realizar el test
    resultado=test(lr,ls)
    
    return resultado

def test_razon(fun):
    "Prueba la función razon"
    
    print("""
---------------------------------------------------------------------------------------------------
    test_razon
    
    Casos:
    
    1. Caso 1: Razón de consistencia válida.
    2. Caso 2: Razón de consistencia inválida.
---------------------------------------------------------------------------------------------------
    """)
    
    # Definir entradas
    lr=[fun(t1_C1, vp_t1_C1), fun(t2_C2, vp_t2_C2)]
    
    # Comprobar las salidas esperadas
    s_1=CR_t1_C1
    s_2=CR_t2_C2
    
    ls=[s_1, s_2]
    
    # Realizar el test
    resultado=test(lr,ls)
    
    return resultado

def test_vector_resultado(fun):
    "Prueba la función vector_resultado"

    print("""
---------------------------------------------------------------------------------------------------
    test_vector_resultado
    
    Casos:
    
    1. Caso 1: Todas las matrices son consistentes.
    2. Caso 2: Hay una matriz inconsistente.
---------------------------------------------------------------------------------------------------
    """)
    
    # Definir entradas
    lr=[fun(vp_alt_3, vp_crit_3, l_bCR_3, l_alternativas_3, l_criterios_3), fun(vp_alt_2, vp_crit_2, l_bCR_2, l_alternativas_2, l_criterios_2)]
    
    # Comprobar las salidas esperadas
    s_1=(l_alternativas_ord_3, vp_alt_ord_3, v_resultado_3)
    
    s_2=(l_alternativas_2, vp_alt_ord_2, v_resultado_2)
    
    ls=[s_1, s_2]
    
    # Realizar el test
    resultado=test(lr,ls)
    
    return resultado

def evaluacion():
    """
    Evalua automáticamente las funciones del programa AHP lectura_entradas, lectura_matrices, vector_pesos, razon y vector_resultado
 y manualmente la generación del archivo de resultados. Finalmente almacena los resultados en un diccinario.
    """
    dir_test=os.getcwd()
    
    os.chdir("Proyectos")
    dir_proyectos=os.getcwd()
    proyectos=os.listdir()
    
    proyecto, lp1, lp2, lp3, lp4, lp5, lp6, notas=[],[],[],[],[],[],[],[]
    
    n_prac=input("Ingrese el número de la práctica que quiere revisar, si desea ingresar a mano el archivo de entradas ingrese 0: ")

    for i in proyectos:
        
        proyecto.append(i)

        print("""
        ________________________________________________________________
        
        Test del proyecto """+str(i)+"""
        ________________________________________________________________
        """)
        
        try:
            os.chdir(i)
            from AHP import lectura_entradas, lectura_matrices, vector_pesos, razon, vector_resultado, main
            os.chdir("../../")
            
            # Evaluación automática --> Funciones principales
            try:
                lp1.append(test_lectura_entradas(lectura_entradas)*5)
            except(Exception):
                print("!ERROR! ---> La función no es correcta")
                lp1.append(0)
                
            try:
                lp2.append(test_lectura_matrices(lectura_matrices)*5)
            except(Exception):
                print("!ERROR! ---> La función no es correcta")
                lp2.append(0)

            try:
                lp3.append(test_vector_pesos(vector_pesos)*5)
            except(Exception):
                print("!ERROR! ---> La función no es correcta")
                lp3.append(0)
                
            try:
                lp4.append(test_razon(razon)*5)
            except(Exception):
                print("!ERROR! ---> La función no es correcta")
                lp4.append(0)
                
            try:
                lp5.append(test_vector_resultado(vector_resultado)*5)
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
                    
            except(Exception):
                print("""
    ---> La función principal no es correcta.
                        """)

            sys.modules.pop('AHP')

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
            
            lp6.append(float(input("¿El archivo en excel fue creado, mostrado y guardado correctamente?: ")))

            notas.append((lp1[-1] + lp2[-1] + lp3[-1] + lp4[-1] + lp5[-1] + lp6[-1])/6)

            os.chdir("../")
            
        except (Exception):
            print("Hay un error general en todo el proyecto, puede faltarle el archivo principal del programa")
            pruebas=[lp1, lp2, lp3, lp4, lp5, lp6]
            for i in pruebas:
                i.append(0)
            notas.append("Revisar a mano")
            
    os.chdir(dir_test)
    
    bd_calif={"Proyectos":proyectos,"Criterio 1":lp1,"Criterio 2":lp2,"Criterio 3":lp3,"Criterio 4":lp4,"Criterio 5":lp5,"Criterio 6":lp6,"Notas":notas}
    
    return bd_calif


def resultados(diccionario):
    """
    Crear y guardar el archivo.xls con los calificaciones del algoritmo AHP.
    """
    
    ## DataFrame de la matríz.
    df_calificaciones=pd.DataFrame(diccionario)
    
    # Crear el documento
    doc=pd.ExcelWriter('Calficaciones_AHP.xlsx', engine='xlsxwriter')
    
    ## Escribir resultados
    df_calificaciones.to_excel(doc, sheet_name='Calificaciones',index=False, startrow=2)

    # Abrir libro y hojas del documento
    libro=doc.book
    hoja_1=doc.sheets['Calificaciones']

    # Títulos
    formato_titulo=libro.add_format({'bold': True, 'font_size': 16})
    hoja_1.write(0, 0, "Calificaciones AHP", formato_titulo)

    ## Guardar documento.
    doc.save() 
    doc.close()

    return None