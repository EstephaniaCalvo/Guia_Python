<a id='4_Bucles-e-Iterables'></a>
# 4. Bucles e Iterables

---
### [4.1. Iterables](#4.1_Iterables)   
>[4.1.1. Métodos Básicos](#4.1.1_Metodos-Basicos)  
[4.1.2. índices](#4.1.2_Indices)  
### [4.2. Estructuras de Repetición](#4.2_Estructuras-de-Repeticion)  
>[4.2.1. Bloque for](#4.2.1_Bloque-for)  
>>[4.2.1.1. Recorrer un Iterable](#4.2.1.1_Recorrer-un-Iterable)  
[4.2.1.2. Recorrido con Índices](#4.2.1.2_Recorrido-con-Indices)  
[4.2.1.3. Contador Condicional](#4.2.1.3_Contador-Condicional)  
[4.2.1.4. Acumulador](#4.2.1.4_Acumulador)  

>[4.2.2. Bloque while](#4.2.2_Bloque-while)  
>>[4.2.2.1. Contadores no Líneales](#4.2.2.1_Contadores-no-Lineales)  
[4.2.2.2. Ejecucion por Evento](4.2.2.2_Ejecucion-por-Evento)  
[4.2.2.3. Bucles Infinitos](4.2.2.3_Bucles-Infinitos)

>[4.2.3. Controladores de Bucles](#4.2.3_Controladores-de-Bucles)

---

## **4.1. Iterables** <a id='4.1_Iterables'></a>

Un iterable es un objeto que es capaz de retornar sus elementos uno a la vez, es un tipo de dato cuyo manejo es especialmente útil y poderoso en Python.

En general, los iterables son aquellos tipos de datos que pueden contener varios elementos, y se llaman así porque Python incorpora funciones que permiten ejecutar operaciones sobre cada uno de los sus elementos con mucha facilidad, por ejemplo, se puede retornar o modificar cada uno de sus elementos con un [cíclo for](#4.2.1_Bloque-for "Ir al apartado del bloque for") como veremos más adelante. 

Los iterables que mas se van a usar en la guía son las variables tipo [string *str*](../2_Elementos_Basicos/2_Elementos_Basicos.ipynb#Variables-de-texto), y las [listas *list*](../5_Estructura_de_Datos/5_Estructura_de_Datos.ipynb#5.1_Listas) que se verán en el siguiente capítulo.

## 4.1.1. Métodos Básicos <a id="4.1.1_Metodos-Basicos"></a>

A continuación están los métodos básicos para interactuar con cualquier iterable, [len( )](#Min-eje_Metodo-len), [count( )](#Min-eje_Metodo-count), e [index( )](#Min-eje_Metodo-index), en este caso se aplicarán a cadenas.

#### a. Método *len( )*  <a id='Min-eje_Metodo-len'></a>
Este método nos muestra la longitud del iterable, es decir, la cantidad de elementos que tiene.
~~~python
# Mini_Ejemplo: Método len()

## Ingresos de datos:
cadena=input("Por favor, ingrese cualquier cadena")

## Contar los elementos:
cantidad=len(cadena)

## Imprimir resultado:
print("La cantidad de elementos que tiene la cadena ingresada '",cadena,"' es:",cantidad)
~~~


```python
# Pase aquí el mini ejemplo anterior
```

#### b. Método *.count( )* <a id='Min-eje_Metodo-count'></a>
Este método nos muestra la frecuencia de un elemento en un iterable, es decir, la cantidad de veces que se encuentra un elemento en el iterable. 
~~~python
# Min_Ejemplo: Método count()

## Ingreso de datos:
palabra="interdisciplinariedad"
print("La palabra disponible para hacer la consulta es: '",palabra,"'.\n")
letra=input("Por favor, ingrese en minúscula la letra que a la quiera consultar su frecuencia.\n")


## Pequeña validación de datos:
if ((letra not in palabra) and (len(letra)==1)):
    import random
    letra=random.choice(palabra)
    print("Lo sentimos, no ha ingresado un valor inválido, el programa usará:",letra,"\n")

## Evaluación del índice:
veces=palabra.count(letra)

## Impresión de resultados:
print("La cantidad de veces que esta la letra '",letra,"' en la palabra '",palabra,"' es:", veces)
~~~


```python
# Pase aquí el mini ejemplo anterior
```

#### c. Método *.index( )* <a id='Min-eje_Metodo-index'></a>
Con este método se puede solicitar la posición de un elemento en un iterable, si hay elementos repetidos arrojará el índice del que se encuentra más a la izquierda. 
~~~python
# Mini_Ejemplo: Método index 

## Ingreso de datos:
palabra="centrifugados"
print("La palabra disponible para hacer la consulta es: '",palabra,"'.\n")
letra=input("Por favor, ingrese en minúscula la letra a la cual quiera consultarle su posición.\n")

## Pequeña validación de datos:
if ((letra not in palabra) and (len(letra)==1)):
    import random
    letra=random.choice(palabra)
    print("Lo sentimos, no ha ingresado un valor inválido, el programa usará:",letra,"\n")

## Evaluación del índice:
indice=palabra.index(letra)

## Impresión de resultados:
print("La posición de la letra '",letra,"' es:", indice)
~~~


```python
# Pase aquí el mini ejemplo anterior
```

## 4.1.2. Índices <a id="4.1.2_Indices"></a>

- **Retornar Valores:**
Es posible acceder a cualquier elemento de un iterable si conocemos su posición o índice, es vital recordar que la indexación en Python **empieza en cero**, esto quiere decir que el primer elemento tiene índice cero. <a id="Min-eje_Indices"></a>

~~~python
# Mini_Ejemplo: Índices

## Ingreso de datos:
palabra=input("Por favor, ingrese una palabra de más de tres letras:\n")

## Pequeña validación de datos:
if not((palabra.isalpha()) and (len(palabra)>3)):
    palabra= 'electroencefalografista'
    print("Lo sentimos, no ha ingresado una palabra válida, el programa usará:\n",palabra,"\n")
    
## Asignación de resultados:
resultado_1=palabra[0]
resultado_2=palabra[1]
resultado_3=palabra[2]

## Impresión de resultados:
print("El primer elemento del iterable es: '",resultado_1,"' y su índice es 0.\n")
print("El segundo elemento del iterable es: '",resultado_2,"' y su índice es 1.\n")
print("El tercer elemento del iterable es: '",resultado_3,"' y su índice es 2.\n") 
~~~


```python
# Pase aquí el mini ejemplo anterior
```

- **Índices negativos:** <a id="Min-eje_Indices-negativos"></a>
Las posiciones en un iterable también pueden ser representadas con número negativos, como si se cambiára de punto de referencia al último elemento y las posiciones se contáran hacia atrás, esta indexación **empieza en -1**.  

~~~python
# Mini_Ejemplo: Índices negativos

## Ingreso de datos:
palabra=input("Por favor, ingrese una palabra de más de tres letras:\n")

## Pequeña validación de datos: 
if not((palabra.isalpha()) and (len(palabra)>3)):
    palabra= 'electroencefalografísta'
    print("Lo sentimos, no ha ingresado una palabra válida, el programa usará:",palabra,"\n")
    
## Asignación de resultados:
resultado_1=palabra[-1]
resultado_2=palabra[-2]
resultado_3=palabra[-3]
    
## Impresión de resultados: 
print("El último elemento del iterable es: '",resultado_1,"' y su índice es -1.\n")
print("El penúltimo elemento del iterable es: '",resultado_2,"' y su índice es -2.\n")
print("El antepenúltimo elemento del iterable es: '",resultado_3,"' y su índice es -3.\n")
~~~


```python
# Pase aquí el mini ejemplo anterior
```

- **Secciones:** <a id="Min-eje_Secciones"></a>
También se puede acceder a través de los índices a secciones de un iterable, para esto se deben indicar la posición inicial y final+1 de la sección. 

~~~python
# Mini_Ejemplo: Secciones

## Ingreso de datos:
palabra=input("Por favor, ingrese una palabra de más de seis letras:\n")

## Pequeña validación de datos:
if not((palabra.isalpha()) and (len(palabra)>3)):
    palabra= 'electroencefalografísta'
    print("Lo sentimos, no ha ingresado una palabra válida, el programa usará:",palabra,"\n")
    
## Asignación de resultados:
resultado_1=palabra[0:4]
resultado_2=palabra[:4]
resultado_3=palabra[:-3]
resultado_4=palabra[2:5]
resultado_5=palabra[1:]
resultado_6=palabra[-5:]
    
## Impresión de resultados:
print("Los primeros cuatro elementos del iterable son: '",resultado_1,"' es decir, los elementos que están desde la posición 0 y antes de la 4.\n")

print("Lo anterior también se puede decir: Los elementos que están antes del quinto elemento son: '",resultado_2,"' es decir, los elementos que están antes de la posición 4.\n")

print("Los elementos que están antes del antepenúltimo elemento son: '",resultado_3,"' es decir, los elementos que están antes de la posición -3.\n")

print("Los elementos que están desde el tercer elemento hasta el quinto son: '", resultado_4,"' es decir, los elementos que están desde la posición 2 y antes de la posición 5.\n")

print("Los elementos que están después del segundo elemento son: '", resultado_5,"' es decir, los elementos que están desde la posición 1 en adelante.\n")

print("Los últimos 5 elementos son:'", resultado_6,"' es decir, los elementos que están desde la posición -5 en adelante.\n")
~~~


```python
# Pase aquí el mini ejemplo anterior
```

- **Error de Indexación:**<a id='Min-eje_Error-de-Indexacion'></a>
Si se intenta acceder a una posición que no existe al correr el código arrojará.

~~~python
# Mini_Ejemplo: Error de Indexación

iterable="01234567"
indice=iterable[8]

">>> IndexError: string index out of range"
~~~

## **4.2. Estructuras de Repetición** <a id='4.2_Estructuras-de-Repeticion'></a>

Las estructuras de repetición son un tipo de estructura de control, usada para repetir un conjunto de instrucciones durante una cantidad de ciclos determinada o hasta que una condición no se cumpla, normalmente son llamados bloques de repetición, bucles o ciclos.

El Bloque for y el Bloque while son las principales estructuras de repetición, y muchas veces pueden ser usadas cualquiera de las dos para crear un ciclo en específico, sin embargo, hay varias diferencias entre ellos.

###### **Ojo:** Al igual que con las estructuras de decisión, la indentación es crucial para que el código corra correctamente.

## 4.2.1. Bloque for <a id='4.2.1_Bloque-for'></a>

La ejecución de este ciclo siempre va a depender de un iterable, hay diferentes maneras en que se usa un ciclo for, a continuación, se mostrarán algunas de ellas.

### 4.2.1.1 Recorrer un Iterable <a id='4.2.1.1_Recorrer-un-Iterable'></a>
El bloque for se puede usar para para recorrer e interactuar con los elementos de un iterable, normalmente se lee: *por cada elemento en un iterable realice las siguientes instrucciones:*.<a id='Min-eje_Recorrer-un-iterable'></a>

~~~python
# Mini_Ejemplo: Recorrer un iterable
iterable="cadena"

for elemento in iterable:
    "Aquí van las instrucciones a realizar"
    print(elemento.upper())

print("Aquí ya salimos del bloque")
~~~


```python
# Pase aquí el mini ejemplo anterior
```

### 4.2.1.2 Recorrido con Índices <a id="4.2.1.2_Recorrido-con-Indices"></a>
Es muy útil cuando se necesita interactuar con dos iterables a la vez, es muy importante que estos sean del mismo tamaño, porque se puede tener un ciclo incompleto o que al correrlo arroje [index error](Min-eje_Error-de-Indexacion "Ir al apartado error de indexación").

Para esto se debe usar la función `range(k)`

- **Función range:** <a id="Min-eje_Funcion-range"></a>
Los parámetros de esta función son (start, stop, step), el tercero es opcional, por ejemplo si las entradas son (j,k,n), retornará una lista inmutable de números desde (j) hasta (k-1), saltando de (n) en (n). Si sólo se ingresa un valor la función tomará las entradas por defecto como (0,k)

~~~python
# Mini_Ejemplo Función range

print("Rango a: 1,11,2")
for i in range(1,11,2):
    print(i)

print("Rango b: 1,11")
for i in range(1,11):
    print(i)

print("Rango c: 11")
for i in range(11):
    print(i)

print("Rango d: -2,2")
for i in range (-2,2):
    print(i)
~~~


```python
# Pase aquí el mini ejemplo anterior
```

En el siguiente se verá cómo crear una cadena, fusionando dos cadenas predefinidas intercalando sus elementos.<a id="Min-eje_Recorrido-con-Indices"></a>

~~~python
# Mini_Ejemplo: Recorrido con Índices

consonantes="TYT" #Iterable 1
vocales="OOA" #Iterable 2
resultado="" # Se crea una cadena vacía para acumular resultados internos.
rango_indices=range(len(consonantes)) # Se crea el rango para los índices = 0 hasta (tamaño de consonantes)-1

for i in rango_indices:
    print("Esta es la vez No.",i+1,"en la que entramos al ciclo, el índice actual es:",i,"\n")
    resultado_interno=consonantes[i]+vocales[i] # Concatenar los elementos de mismo índice de vocales y consonante
    print("Resultado interno=",resultado_interno)
    resultado=resultado+resultado_interno # Acumular los resultados internos
    print("Resultado acumulado=",resultado,"\n\n")

print("El resultado final=",resultado)
~~~


```python
# Pase aquí el mini ejemplo anterior
```

### 4.2.1.3 Contador Condicional <a id="4.2.1.3_Contador-Condicional"></a>
Es usado cuando se necesita contar la cantidad de elementos de un iterable que cumplen con una condición.

Como el contador es una variable acumulativa, será de gran ayuda conocer los operadores de asignación.

- **Operadores de asignación: **
Estos operadores son muy útiles para abreviar operaciones sobre la misma variable.

|Operador|Descripción|Operación|Descripción|
|:--------:|:--------:|:--------:|:--------:|
|=|Igualdad|/=|c/=3(c=c/3)|
|+=|c+=1 (c=c+1)|%=|c%=4 (c=c%4)|
|-.=|c-=1 (c=c-1)|\**\=|c\*\*\=2(c=c\*\*2\)|
|*=|c\*=2 (c=c*2)|//=|c//=5 (c=c//5)|

El siguiente Mini_ejemplo cuenta cuantos números primos hay entre 1 y 100. Si desea imprimir la lista de los números identificados, como primos o no, deshabilite los comentarios. <a id="Min-eje_Contador-Condicional"></a>

~~~python
# Mini_Ejemplo: Contador Condicional (Números primos hasta el 100)

rango=range(1,101) # Se crea el rango de 1 hasta 100
contador=0

for i in rango:
    if i!=1 and ((i in (2,3,5,7))or not((i%2==0) or (i%3==0) or (i%5==0) or (i%7==0))):
#         print(i,"es primo")
        contador+=1 #contador=contador+1
#     else:
#         print(i,"no es primo")

print("\nLa cantidad de números primos que hay hasta 100 es:",contador)
~~~


```python
# Pase aquí el mini ejemplo anterior
```

### 4.2.1.4 Acumulador <a id='4.2.1.4_Acumulador'></a>
Este ciclo tambien se puede utilizar para acumular en una variable los resultados de cada cíclo, sobretodo cuando se necesita interactuar con los resultados de cíclos anteriores y se debe crear una variable que haga el papel de memoria.

En el siguiente ejemplo se va a guardar en un string la secesión de Fibonacci hasta el n-avo valor, el cual es ingresado por el usuario.<a id="Min-eje_Acumulador"></a>

La suseción de fibonacci $(x_n)$ está descrita por la siguiente formula: $x_1=1,\quad x_2=1,\quad x_n=x_{n-1}+x_{n-2}\;\;(n>2)$, es decir, $(x_n)$ es igual, a la suma de los dos $(x_n)$ anteriores, por lo tanto la lógica que siguió fue la siguiente:  

Sea:  
nuevo_fibonacci= $(x_n)$  
fibonacci_actual= $x_{n-1}$   
fibonacci anterior= $x_{n-2}$   

~~~
Crear una la lista de 1 hasta el n-avo Fibonacci.

Para cada n evaluar:

    Si n es 1:
        El fibonacci actual es 0 
        Y el anterior es 1.   
        
    Si es diferentes de 1 entonces:
        El nuevo fibonacci es el actual + el anterior
        (Después de calculado el nuevo fibonacci)
        El fibonacci actual se convierte en el anteriror. 
        Y el nuevo fibonacci se convierte en el actual. 
~~~

~~~python
# Mini_Ejemplo: Acumulador (Sucesión de Fibonacci)

#Ingresar datos
n_avo=input("Por favor ingrese el n-avo Fibonacci hasta donde quiere calcular la sucesión\n")
sucesion=""

## Peuqeña validación de datos:
if not n_avo.isnumeric():
    n_avo=100
    print("Ha ingresado un valor inválido, el programa ha defino que el n-avo Fibonacci será:",n)

## Conversión:
n_avo=int(n_avo)

## Crear rango:
rango=range(1,n_avo+1) #creamos el rango para que empiece en 1 y termine en n.

for i in rango:
    # Si es el Fibonacci no. 1 entonces:
    if i==1:
        #El fibonacci anterior es igual 0 y el actual es igual 1
        fibonacci_anterior=0
        fibonacci=1
    else: #si no
        #El nuevo fibonacci es igual alactual mas el anterior.
        nuevo_fibonacci=fibonacci+fibonacci_anterior
        fibonacci_anterior=fibonacci
        fibonacci=nuevo_fibonacci
    final=",\n" if i!=n_avo else "."
    sucesion=sucesion+"Fibonacci No."+str(i)+"= "+str(fibonacci)+final
    
print("La sucesión Fibonacci hasta el índice 100 es:")
print(sucesion)
~~~


```python
# Pase aquí el mini ejemplo anterior
```

## 4.2.2. Bloque while <a id='4.2.2_Bloque-while'></a>

Este bloque ejecuta las instrucciones que contiene mientras se cumpla la condición a la que esté sujeto, cuando esta condición deja de ser verdadera se pasa al siguiente bloque del código.

Como se verá más adelante este bloque es muy útil cuando no se tine predefino la cantidad de iteraciones a realizar, y normalmente se lee: *Mientras se cumpla la condición x haga:*

A continuación, están algunas formas de usar este bloque.

### 4.2.2.1. Contadores no Lineales. <a id='4.2.2.1_Contadores-no-Lineales'></a>

En el siguiente ejemplo, el usuario tiene 5 intentos para adivinar un número, así que puede haber hasta 5 interacciones, pero no se sabe exactamente cuántas, ya que, el usuario puede adivinar en la oportunidad 1,2,3 o 4, por lo tanto, lo más común es usar un bloque while, ya que, para hacerlo con un bloque for habría que usar el [controlador break](#4.2.3_Controladores-de-Bucles "Ir al apartado de controladores de bucles") que se explicará más adelante. <a id='Min-eje_Contadores-no-Lineales'></a>

~~~python
# Mini_Ejemplo: Contadores no lineales

## Ingreso datos:
import random
numero=str(random.randint(1,10))
intentos=1
print("Adivina el número entre 1 y 10, cuenta con 5 intentos")


while intentos<=5: 
    num_usuario=input("Ingrese un número.")
    
    if num_usuario==numero:
        print("!Has adivinado, felicitaciones!")
        intentos=5
    elif intentos==4:
        print("Fallaste, ya solo te queda una oportunidad.")
    elif intentos==5:
        print("Fallaste de nuevo, el número era",numero)
    else:
        print("El número no es",num_usuario,"vuelve a intentarlo.")
    
    intentos+=1
    
print("Terminamos de jugar, !gracias!")
~~~


```python
# Pase aquí el mini ejemplo anterior
```

### 4.2.2.2 Ejecución por Evento <a id='4.2.2.2_Ejecución-por-Evento'></a>
Cuando se necesita que se cumpla cierta condición para poder continuar, se crea un ciclo while, como muestra el siguiente mini_ejemplo no se pode seguir hasta que no se ingrese un número entero. <a id='Min-eje_Ejecución-por-Evento'></a>

~~~python
# Mini_Ejemplo: Ejecución por Evento (Pequeña validación de datos)

numero=input("Por favor, ingrese un número entero:")
         
while not(numero.isnumeric()):
    numero=input("No ha ingresado un número entero, por favor vuelva a intentarlo")
    
print("Gracias por ingresar un número válido")
~~~


```python
# Pase aquí el mini ejemplo anterior
```

### 4.2.2.3 Bucles Infinitos <a id='4.2.2.3_Bucles-Infinitos'></a>
Como se vió el ciclo while a diferencia del ciclo for no requiere tener definida la cantidad de iteraciones, y se puede repetir un bloque hasta o mientras que  se cumpla una condición como vimos en ejemplo anterior, por lo cual, es posible tener un ciclo infinito si esta condición nunca se llega a cumplir, por lo tanto, el programa nunca dejará de ejecutarse.

Por ejemplo si ejecuta el siguiente Mini_Ejemplo en una consola está no dejará de ejecutarse hasta que la reinicie con ( ctrl + L + C ) o se acabe la memoria.  

~~~python
# Mini_Ejemplo: Bucle infinito (Factorial infinito)
numero=1
factorial=1
while numero>=1:
    factorial*=numero
    print(factorial,"\n")
    numero+=1
~~~
![Fig1_Bucle_Infinito](Fig1_Bucle_Infinito.gif)

## 4.2.3. Controladores de Bucles <a id='4.2.3_Controladores-de-Bucles'></a>
Las palabras reservadas `Break` y `Continue`, son instrucciones que modifican el flujo de una estructura de repetición.
- **Break:** Se utiliza para salir de un bucle si se cumple una condición.
- **Continue:** Con esta instrucción se puede saltar una parte del bucle si se cumple una condición.  

En la guía no se va hacer mucho uso de ellos, sin embargo, el siguiente ejemplo muestra cómo hacer el [Mini_Ejemplo Contadores no Lineales](#Min-eje_Contadores-no-Lineales), con un bloque for haciendo uso de la instrucción break. <a id='Min-eje_Break'></a>

~~~python
# Mini_Ejemplo: Break (Adivinar un número con for)

## Ingreso datos:
import random
numero=str(random.randint(1,10))
numero=str(4)
print("Adivina el número entre 1 y 10, cuenta con 5 intentos")

for i in range(5):
    num_usuario=input("Ingrese un número")
    if num_usuario==numero:
        print("!Has adivinado, felicitaciones!")
        break
    elif i==3:
        print("Fallaste, ya solo te queda una oportunidad.")
    elif i==4:
        print("Fallaste de nuevo, el número era",numero)
    else:
        print("El número no es",num_usuario,"vuelve a intentarlo.")
        
print("Terminamos de jugar, !gracias!")
~~~


```python
# Pase aquí el mini ejemplo anterior
```

_____

| [***Anterior***](../3_Estructuras_Logicas/3_Estructuras_Logicas.ipynb#3_Estructuras-Logicas) <!--(https://mybinder.org/Introducción)--> | - | [***Siguiente***](../5_Estructura_de_Datos/5_Estructura_de_Datos.ipynb#5_Estructura-de-Datos-Basicas) <!--(https://www.python.org/Programas-en-Python)--> |
| :--------: | :-------: | :--------: |

| [**Home**](../Home.ipynb#Home)<!--(https://mybinder.org/Home)--> |
| :--------: |
