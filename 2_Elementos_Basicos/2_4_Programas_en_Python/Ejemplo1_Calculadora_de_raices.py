# Ejemplo-1_Calculadora-de-raices.py

# By Leonardo Rivera

## Análisis del problema
"""
Problema: Crear un programa para calcular la raíz cuadrada de varios números,
el usuario indica las veces que quiere hacer la operación y los números a operar,
y una vez terminado se despide. 

Entradas:
    1. Cantidad de cálculos= veces.
    2. Número a operar= num.

Salidas:
    1. Mensaje 1: "CÁLCULO DE RAÍCES CUADRADAS"
    2. Mensaje 2: "La raíz cuadrada de num es raíz"
    3. Mensaje 3: "Hemos terminado. Adiós"

Pseudocódigo:

-2. Importar math.
-1. Crear función para calcular raíz= raiz_cuadrada
0. Definir programa principal. 
    1. Imprimir: Mensaje 1.
    2.Ingresar veces.
    3. Convertir veces a integer= times
    4. Ingresar num y calcular raíz.
    Por cada vez en times haga:
        4.1 Ingresar num.
        4.2 Convertir num a float= numero.
        4.3 Calcular raíz= raiz_cuadrada(numero)
        4.4 Imprimir: Mensaje 2.
    5. Imprimir: Mensaje 3. 
6. Ejecutar programa principal.
"""

## -2. IMPORT STATEMENTS

import math

## -1. HELPER FUNCTIONS.

def raiz_cuadrada(n):
    raiz=math.sqrt(n)

    return raiz

## 0. MAIN PROGRAM

def main():
    print("CÁLCULO DE RAÍCES CUADRADAS") # 1
    veces= input("Cuántas raíces cuadradas va a calcular: ") # 2
    times= int(veces) # 3
    
    #4
    for j in range (times):
        num=input("Dígame el número: ")# 4.1
        numero= float(num)# 4.2
        raiz= raiz_cuadrada(numero) #4.3
        print("La raíz cuadrada de ",numero," es:",raiz) #4.1¿4
        
    print("Hemos terminado. Adiós") #5

## 6. EJECUTAR.

if __name__=='__main__':
    main() 