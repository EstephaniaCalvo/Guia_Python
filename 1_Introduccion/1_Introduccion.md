# 1. Introducción <a id='1_Introduccion'></a>

---
### [1.1. Presentación](#1.1_Presentacion)  
### [1.2. Instalación](#1.2_Instalacion)  
>[Opción 1: Python](#Opcion-1_Python)  
[Opción 2: Anaconda](#Opcion-2_Anaconda)  

### [1.3. Algunos IDE](1_3_Algunos_IDE/1_3_1_IDLE/1_3_1_IDLE.ipynb#1.3_Algunos-IDE) <!--(https://mybinder.org/Algunos-IDE/IDLE)-->  
>[1.3.1. IDLE](1_3_Algunos_IDE/1_3_1_IDLE/1_3_1_IDLE.ipynb#1.3.1_IDLE) <!--(https://mybinder.org/Algunos-IDE/IDLE)-->   
[1.3.2. JupyterLab](1_3_Algunos_IDE/1_3_2_JupyterLab/1_3_2_JupyterLab.ipynb#1.3.2_JupyterLab) <!--(https://mybinder.org/Algunos-IDE/JupyterLab)-->  

### [1.4. Instrucciones Guía Interactiva](1_4_Instrucciones_Guia_Interactiva/1_4_Instrucciones_Guia_Interactiva.ipynb#1.4_Insutrucciones-Guia-Interactiva) <!--(https://mybinder.org/Instrucciones)-->

---

## **1.1. Presentación** <a id='1.1_Presentacion'></a>

La presente guía esta creada a partir de la Pequeña Guía de Python Versión 0.5, del profesor Leonardo Rivera Cadavid y usada en el curso de Implementación de algoritmos de Ingeniería industrial, en la Universidad del Valle,  Cali, Colombia, 2017.

El objetivo principal es ayudar a una rápida familiarización con el lenguaje Python, el programa de desarrollo IDLE que viene incluido con este, el administrador de paquetes Anaconda y algunas de las aplicaciones incluidas allí, con el fin de apoyar  la [Guía de implementación de algoritmos de ingeniería industrial](https://sites.google.com/correounivalle.edu.co/guia-algortimos-industrial/home "Ir a la Guía de implementación de algoritmos de ingeniería industrial") de la Universidad valle, Cali, Colombia. 

Para mayor información sobre el lenguaje, su historia, su filosofía y su creador lo invito a consultar recursos como:

 > https://en.wikipedia.org/wiki/Python_(programming_language)  
https://www.python.org/about/  
https://docs.anaconda.com  

## **1.2. Instalación** <a id='1.2_Instalacion'></a>

Para poder empezar a programar con el lenguaje Python, se debe descargar un intérprete del lenguaje y un IDE (Integrated Development Environment, Entorno Integrado de Desarrollo), a continuación, se mostrarán dos formas más comunes para hacerlo.

###### **Nota:** Recomiendo instalar el administrador de paquetes y entornos Anaconda, porque tien no hay necesidad de instalar módulos aparte.

## Opción 1: Python <a id='Opcion-1_Python'></a>

#### - Contenido:  
- Interprete del lenguaje
- IDLE: Programa nativo para escribir código.

###### **Nota:** IDLE es considerado como un IDE, sin embargo, no lo considero un entorno sofisticado como Spyder o JupyterLab, de todas maneras, es un programa liviano, amigable y fácil de usar.

#### - Instalación 

Para ver los archivos y las instrucciones de instalación del intérprete de Python 3 ingrese [aquí](www.python.org/downloads/ "www.python.org/downloads/"). 

Por favor sigan las instrucciones para su respectivo sistema operativo. Hay versiones para Windows, Mac OS X y todos los sabores de Linux.

En este momento la versión vigente es la 3.8.0. Verá que en muchos casos aún ofrecen instaladores y otros recursos para Python 2.7. La razón es que existen muchos programas escritos en versiones anteriores, entonces aún se presta soporte para ellas. Sin embargo, el desarrollo y soporte para Python 2.7 se detendrá paulatinamente, y todos los sistemas migrarán a la versión más actualizada. **Por ello para el desarrollo de la guía utilizaremos Python 3.x**.

Tenga en cuenta que la instalación de esta opción es más rápida que la opción 2, sin embargo, solo tendrá preinstalados los módulos de la [libreria estándar](../9_Modulos/9_Modulos_y_Paquetes.ipynb#9.3_Libreria-Estandar "Ir al apartado 9.3. Libreria Estandar"), así que en el momento de ser requeridos otros módulos, estos deberán ser instalados por medio del administrador de paquetes **pip**, en esta guía se explicarán los pasos para la [instalación en Windows](../9_Modulos/9_Modulos_y_Paquetes.ipynb#9.4.1_Instalacion-de-Paquetes "Ir al apartado 9.4.1. Instalacion de Paquetes").

## Opción 2: Anaconda **(Recomendada)** <a id='Opcion-2_Anaconda'></a>

#### - ¿Qué es?

Anaconda es un administrador gratuito de paquetes y de entornos, y una distribución de data science de Python y R con una colección de más de 1,500+ paquetes de código abierto. Su instalación es fácil, y ofrece soporte comunitario gratuito.

#### - Contenido:

- Interprete de lenguaje Pyhon. 
- Anaconda Navigator: GUI (Graphical User Interface - Interfaz Gráfica de Usuario).
- Más de 250 paquetes preinstalados

###### **Nota:** Los paquetes preinstalados en para la versión actual en Windows los puede encontrar [aquí](https://docs.anaconda.com/anaconda/packages/py3.7_win-64/ "Ir a la documentación oficial de Anaconda")
- Jupyter Notebook
- JupyterLab
- Spyder
- Otras herramientas que **No** se utilizarán en la guía, como Glueviz, Orange 3, RStudio y VS Code.

#### - Instalación 

Para ver los archivos y las instrucciones de instalación de Anaconda para los diferentes sistemas operativos ingrese [aquí](https://www.anaconda.com/distribution/ "https://www.anaconda.com/distribution/"). 

En este momento la versión vigente es la 2019.10 para Python 3.7

-----

| [**Home**](../Home.ipynb#Home)<!--(https://mybinder.org/Home)--> | - | [**Siguiente**](1_3_Algunos_IDE/1_3_1_IDLE/1_3_1_IDLE.ipynb#1.3_Algunos-IDE)<!--(https://mybinder.org/v2/gh/EstephaniaCalvo/Pequena-Guia-Python/Home?filepath=1-Introduccion%2F1-2-1%20IDLE%2F1-3-1_IDLE.ipynb)--> |
| :--------: | :-------: | :--------: |
