## 1.3.2. JupyterLab <a id='1.3.2_JupyterLab'></a>

---
[1.3.2.1. Interfáz](#1.3.2.1_Interfaz)  
[1.3.2.2. Jupyter Notebooks](#1.3.2.2_Jupyter_Notebooks)    
[1.3.2.3. Celdas de Código](#1.3.2.3_Celdas_de_Codigo)  

---
JupyterLab es IDE basado en web para manipular Jupyter notebooks, código, y datos, viene preinstlado en el administrador de entornos y paquetes Anaconda, [aquí](https://jupyter.org/ "Ir a la página oficial de Jupyter") puede entrar a la página oficial de Jupyter.

### 1.3.2.1. Interfáz

Como es basado en Web JupyterLab se abre en el navegador, su una interfaz tiene muchos más detalles que la de [IDLE](../1_3_1_IDLE/1_3_1_IDLE.ipynb "Ir al apartado 1.3.1. IDLE"), para ver su guía oficial ingrese [aquí](https://jupyterlab.readthedocs.io/en/latest/user/interface.html "Ir a la guía oficial de la interfaz de Jupyter."). A continuación se mostrarán sus partes principales.

![interfaz1.png](Imagenes/interfaz1.png "Ejemplo: Interfáz de JupyterLab")

1. **Menú:** Es lo que está señalado en cuadro verde, con este menú se puede interactuar con la pestaña que esté activa, y la configuración de la interfaz en general.

2. **Barra izquierda:** Es la barra que está en el recuadro azul, por defecto viene abierta si quiere ocultarla vaya a **View/Show Left Sidebar/**. Contiene varias opciones, sin embargo, para la guía solo es necesario conocer dos: 
    - **Barra de navegación**: Tiene el símbolo de la carpeta y sierve para navegar por los directorios.
    - **Barra de terminales y kernels**: Está justo abajo de la barra de navegación y con ella se puede cerrar las seciones los kernels de los notebooks, consolas y terminales que han sido abiertos.
    ![interfaz2](Imagenes/Interfaz2.png "Ver la interfaz de la brra de terminales y kernels")

3. **Mesa de trabajo:** Es es espacio donde se abren las petañas de los documentos con los que se van a trabajar y está señalado con rojo, como puede ver puede contener varias pestañas a la vez, según la diposición que haya elegido el usuario, para organizar una pestañas solo debe arrastrarla hasta el lugar donde quiera ponerla.
    Jupyter soporta la visualizacion de varios archivos, algunos de ellos son: 
    - **Jupyter Notebooks:** Documento .ipynb
    - **Consolas:** En la guía se utlizarán como si fueran el Shell de IDLE.
    - **Terminales:** Simbolo del sistema.
    - **Imágenes:** Archivos .png, .jpg. .gif.
    - **Archivos de texto plano:** .txt, .md(makrdow)
    
    Además de los documentos también contiene el Laucher, donde están todos los documentos y/o apliciones que se puede crear o abrir.

### 1.3.2.2. Jupyter Notebooks <a id='1.3.2.2_Jupyter_Notebooks'></a>

Es un documento que permite insteractuar con celdas de código para correr el lenguaje indicado y con celdas de texto plano escrito con Markdown, ampliamente usado en ciencias de datos y el mundo académico por las claras ventajas que presenta al compartir y visualizar proyectos con código en vivo. La extención de este tipo de doucmentos es .ipynb

Si está en la versión interactiva de la guía, usted se encuentra ahora en un notebook, para abrir uno nuevo diríjase a la carpeta donde quiere crearlo con el navegador de archivos, después abrálo con el Laucher o vaya a **File/New/Notebook**, selecciones Python 3 como Kernel, por defecto se creará una celda de código.

Antes de ver las opciones para interactuar con las celdas, hay que concer la diferencia entre estar afuera o adentro de una celda. 

**Adentro:** Para entrar a una celda solamente de clik dentro de ella.
![Celda1](Imagenes/Celda1.png "Estar adentro de una celda")


**Afuera:** Para salir de una celda de click entre la barra azul y el recuardro de la celda.

![Celda2](Imagenes/Celda2.png "Estar adentro de una celda")

Estos son los atajos de teclado que funcionan cuando se está afuera de celda.

- **A :** Crear una celda nueva arriba de la posición acutual
- **B :** Crear una celda nueva abajo de la posición acutual
- **M :** Convertir a celda Markdonw
- **Y :** Convertir a celda de código
- **DD :** Borrar una celda
- **Shift + M :** Juntar dos celdas 
- **C :** Copiar
- **X :** Cortar
- **V :** Pegar
- **Z :** Revertir
- **Shit + Z :** Devolver

Cuando está en una celda use estos atajos:

- **Ctrl + C :** Copiar
- **Ctrl + X :** Cortar
- **Ctrl + V :** Pegar
- **Ctrl + Z :** Revertir
- **Ctrl + Y :** Devolver
- **Ctrl + Shift + - :** Dividir celda
- **Ctrl + Enter :** Correr la celda
- **Ctrl + Shift + Enter :** Correr la celda y avanzar.

### 1.3.2.3. Celdas de Código <a id='1.3.2.3_Celdas_de_Codigo'></a>

Las celdas de código funcionan como si fueran una consola o un editor de código, solo puenden ejecutarse si el kernel es Python 3, las funciones de este están en el **Menú/Kernel**, para seleccionarlo vaya a la esquina izquierda del notebook y de clik al lado del círculo y seleccione Python.

Los atajos de teclado para interactuar con el son:

- **|| :** Interrumpir.
- **00 :** Restaurar

Otras opciones importante son: 
- **Limpiar salidas:** Click derecho/Clear outputs.
- **Limpiar todoas las salidas:** Clik derecho/Clear all outputs.

Las celdas de código de un notebook están enlazadas por ejemplo, ejecute las siguientes celdas en orden, y luego restaure el kernel y ejecutelas en desorden, muy probablemente le saldrá NameError porque una de las variables no ha sido inicializada, para regresar al estado inicial, restuare el kernel y limpie todos las salidas.


```python
a=345
```


```python
b=876
```


```python
c=b-a
c
```

Tambien se puede escribir todo como si fuera un son lo bloque de código:


```python
x=3
y=9
z=y-x
z
```

Al estár conectadas es como si fuera un solo código:


```python
print("a:",a)
print("b:",b)
print("c:",c)
print("x:",x)
print("y:",y)
print("z:",z)
```

-----

| [**Anteriror**](../1_3_1_IDLE/1_3_1_IDLE.ipynb#1.3.1_IDLE) <!--(https://mybinder.org/Algunos-IDE/Spyder)--> | - | [**Siguiente**](../../1_4_Instrucciones_Guia_Interactiva/1_4_Instrucciones_Guia_Interactiva.ipynb#1.4_Insutrucciones-Guia-Interactiva) <!--(https://mybinder.org/Instrucciones)--> |
| :--------: | :-------: | :--------: |

| [**Home**](../../../Home.ipynb#Home)<!--(https://mybinder.org/Home)--> |
| :--------: |
