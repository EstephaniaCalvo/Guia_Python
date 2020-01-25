import matplotlib.pyplot as plt
from random import choice

colores=['aquamarine', 'bisque', 'blue', 'blueviolet', 'brown', 'burlywood', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'crimson', 'cyan', 'green', 'lightblue', 'lightcoral', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightslategrey', 'lime', 'limegreen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'moccasin', 'navajowhite', 'navy', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'peachpuff', 'peru', 'pink', 'plum', 'purple', 'rebeccapurple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'sienna', 'skyblue', 'slateblue', 'slategrey', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'yellow', 'yellowgreen']

def histograma (nombre,datos,n_clases,tipo="h",modo="c",name_data="Datos",u_color=None, n_label=None):
    """
    Genera un historgrama según el tipo indicado y  el modo de presentación indicado.
    Sus argumentos obligatorios son: El nombre del gráfico, la lista de datos, el número de clases.
    
    Por defecto el tipo de gráfico es el histograma simple, 'h', pero también admite valores para:
    Histograma normalizado: 'hn'
    Histograma acumulativo:'ha'
    
    Por defeccto el modo de presentación es 'c' para solo crear el gráfico, aúnque tambien admite los siguientes valores:
    'm': Lo muestra.
    'ms': Llo muestra y lo guarda como archivo.png
    's': Lo guarda como archivo.png
    
    Además el nombre del eje x (name_data) es Datos y el color del gráfico (u_color) es aleatorio
    """
    
    if u_color==None:
        u_color=choice(colores)
    plt.title(nombre,fontsize=18)
    plt.ylabel("Frecuencia",fontsize=14)
    plt.xlabel(name_data,fontsize=14)
    
    if tipo=="h":
        histograma=plt.hist(datos,n_clases,edgecolor=u_color,color=u_color,alpha=0.5,label=n_label)
    elif tipo=="hn":
        histograma=plt.hist(datos,n_clases,density=True,edgecolor=u_color,color=u_color,alpha=0.5,label=n_label)
        plt.ylabel("Frec. Relativa")
    elif tipo=="ha":
        histograma=plt.hist(datos,n_clases,cumulative=True,edgecolor=u_color,color=u_color,alpha=0.5,label=n_label)

    clases=histograma[1]
    plt.xticks(clases)
    
    if modo=="m":
        plt.show(block=False)
        plt.close()
    elif modo=='s':
        plt.savefig(nombre+".png")
        plt.close()
    elif modo=="ms":
        plt.savefig(nombre+".png")
        plt.show(block=False)
        plt.close()
    elif modo=="c":
        return histograma



def h_comparativo (l_nombres,l_datos,l_n_clases,l_tipos,l_colores,modo="m"):
    """
    Genera un varios histogramas para compararlos apartir de las siguientes listas para cado histogramas.
    l_nombres: Nombres.
    l_datos: Listas de datos.
    l_n_clases: Números de clases.
    l_tipos: Tipos de histograma. ('h': simple, 'hn': normalizado, 'ha': acumulativo)
    l_colores: Colores, si se desea que sea aleatorio poner en la lista una cadena vacía ''.
    
    Y por último esta el argumento modo que no es una cadena: 
    
    modo: Modo de presentación del histograma comparativo ('m': mostrar, 'ms': mostrar y guardar, 's': guardar)
    """
    
    n=len(l_nombres)
    
    for i in range(0,n):
        if l_colores[i]=="":
            histograma(l_nombres[i],l_datos[i],l_n_clases[i],l_tipos[i],modo="c",n_label=l_nombres[i])
        else:
            histograma(l_nombres[i],l_datos[i],l_n_clases[i],l_tipos[i],lcolores[i],modo="c",n_label=l_nombres[i])
    plt.title("Histograma comparativo")
    plt.ylabel("Frecuencias")
    plt.legend()
    
    if modo=='m':
        plt.show(block=False)
        plt.close()
    elif modo=='s':
        plt.savefig("Histograma comparativo.png")
        plt.close()
    elif modo=='ms':
        plt.savefig("Histograma comparativo.png")
        plt.show(block=False)
        plt.close()
        
    return None
            