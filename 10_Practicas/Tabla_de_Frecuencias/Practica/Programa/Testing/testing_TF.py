# Título: testing_TF.py
# Autor: Estpehania Calvo

# Constanstes
c=['aquamarine', 'bisque', 'blue', 'blueviolet', 'brown', 'burlywood', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'crimson', 'cyan', 'dgreen', 'lightblue', 'lightcoral', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightslategrey', 'lime', 'limegreen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'moccasin', 'navajowhite', 'navy', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'peachpuff', 'peru', 'pink', 'plum', 'purple', 'rebeccapurple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'sienna', 'skyblue', 'slateblue', 'slategrey', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'yellow', 'yellowgreen']

datos= [62.2, 70.9, 70.0, 58.3, 56.0, 81.9, 73.2, 75.4, 63.1, 78.8, 65.6, 76.8, 59.9, 58.5, 65.5, 78.8, 57.6, 80.0, 76.5, 52.2, 75.0, 58.5, 70.0, 71.9, 69.3, 58.7, 74.2, 77.5, 76.0, 63.3, 65.7, 82.4, 84.2, 79.9, 66.7, 59.9, 72.8, 65.9, 72.3, 68.9, 48.8, 64.9, 56.7, 66.6, 76.6, 98.6, 68.1, 79.7, 82.8, 50.6, 70.2, 85.8, 80.6, 67.6, 61.6, 64.6, 57.3, 85.0, 73.3, 64.2, 63.1, 79.2, 63.6, 81.1, 44.0, 64.0, 82.0, 57.5, 76.0, 68.6, 60.2, 79.3, 60.4, 76.4, 80.9, 70.9, 76.2, 67.0, 86.5, 83.5, 67.8, 76.2, 70.0, 65.7, 80.8, 83.9, 83.0, 68.2, 66.0, 72.7, 75.6, 72.6, 67.0, 66.7, 38.8, 85.8, 72.7, 74.6, 59.3, 73.6, 70.1, 52.7, 76.6, 71.3, 77.3, 55.2, 73.7, 72.8, 57.0, 51.3, 82.6, 77.5, 71.3, 84.9, 83.5, 75.5, 85.5, 57.4, 62.5, 72.5, 76.1, 70.4, 62.4, 73.5, 88.4, 76.0, 66.7, 89.0, 76.8, 84.8, 64.7, 73.3, 61.1, 62.1, 54.7, 45.6, 72.9, 56.2, 62.0, 60.2, 61.1, 69.6, 69.1, 67.2, 90.5, 64.5, 69.4, 70.3, 63.3, 79.2, 71.6, 64.4, 75.2, 74.7, 68.9, 85.3, 76.9, 63.3, 55.9, 52.3, 61.1, 67.1, 73.8, 70.8, 70.1, 85.5, 75.2, 66.4, 78.5, 53.5, 66.0, 68.3, 76.9, 62.6, 67.5, 61.4, 76.0, 67.8, 61.2, 67.7, 57.4, 64.5, 82.1, 72.8, 69.8, 57.4, 82.6, 73.0, 61.1, 76.0, 51.3, 52.8, 76.8, 60.8, 45.9, 60.1, 55.0, 66.0, 61.1, 55.5, 77.0, 87.5, 80.7, 78.0, 56.6, 83.7, 77.4, 82.6, 65.1, 74.1, 60.2, 56.5, 60.5, 74.2, 86.8, 78.3, 65.3, 77.8, 77.4, 66.0, 93.3, 69.9, 88.7, 48.0, 78.3, 73.8, 53.5, 62.1, 79.6, 59.5, 76.7, 70.0, 64.2, 72.0, 62.5, 70.3, 60.9, 52.7, 78.8, 54.7, 51.1, 59.5, 75.6, 57.6, 63.5, 78.4, 85.6, 82.9, 76.4, 77.0, 66.4, 57.7, 70.9, 61.6, 55.9, 58.1, 79.5, 83.5, 69.0, 70.6, 76.2, 56.4, 68.7, 79.4, 63.2, 56.8, 77.1, 87.3, 76.3, 72.9, 74.5, 68.6, 49.2, 72.3, 51.6, 75.4, 57.7, 64.3, 67.8, 66.0, 61.5, 58.9, 66.6, 62.8, 43.4, 66.0, 71.4, 63.8, 61.4, 76.2, 85.2, 47.3, 72.4, 69.5, 58.8, 69.7, 78.3, 95.3, 69.9, 71.1, 77.2, 74.6, 75.6, 82.8, 51.2, 66.4, 68.2, 64.1, 64.1, 54.5, 91.1, 88.1, 77.1, 66.8, 82.9, 74.4, 63.7, 56.3, 76.8, 61.1, 61.5, 66.0, 56.5, 52.1, 62.9, 77.5, 90.0, 78.6, 51.9, 64.1, 85.2, 71.0, 60.5, 81.4, 62.1, 71.5, 66.6, 69.2, 48.1, 70.8, 92.2, 68.9, 93.1, 67.4, 71.0, 87.9, 88.4, 69.4, 66.8, 70.0, 77.9, 59.5, 73.7, 81.4, 57.3, 60.7, 72.9, 65.6, 56.9, 66.5, 57.2, 71.6, 79.2, 60.0, 55.0, 74.5, 62.2, 61.7, 83.4, 70.6, 48.0, 52.2, 61.7, 75.4, 81.9, 54.6, 64.9, 64.6, 52.7, 91.2, 57.2, 59.5, 74.0, 87.1, 70.7, 62.4, 66.7, 68.1, 78.9, 65.9, 72.3, 73.3, 81.9, 60.1, 90.0, 54.5, 68.6, 63.5, 44.0, 74.6, 59.5, 70.6, 68.4, 77.3, 71.7, 70.2, 84.2, 74.8, 68.1, 75.7, 81.9, 72.9, 82.4, 92.6, 84.1, 63.2, 71.1, 64.9, 80.3, 90.1, 69.8, 44.6, 61.1, 79.9, 74.6, 58.8, 79.3, 66.4, 69.4, 92.8, 58.6, 70.2, 58.4, 81.2, 64.2, 73.6, 70.6, 61.4, 50.7, 63.0, 89.5, 61.8, 58.2, 58.8, 65.3, 64.7, 68.6, 69.6, 95.3, 63.2, 68.8, 78.3, 73.9, 78.9, 73.8, 66.2, 70.8, 55.2, 69.7, 69.4, 86.6, 59.4, 63.6, 68.6, 72.1, 81.2, 79.7, 60.6, 58.3, 69.8, 58.1, 64.8, 71.0, 74.7, 69.6, 67.9, 71.0, 54.7, 68.1, 71.2, 57.9, 75.6, 77.6, 88.0, 57.2, 77.7, 69.7, 65.9, 62.6, 86.0, 79.5, 79.0, 66.5, 69.3, 63.2, 78.7, 68.8, 64.2, 65.7, 65.6, 83.6, 52.7, 66.1, 48.0, 66.1, 63.4, 76.5, 70.6, 74.0, 57.7, 67.6, 71.7, 71.5, 66.3, 87.5, 52.1, 63.6, 76.2, 65.6, 54.8, 70.5, 75.4, 64.1, 85.1, 55.9, 67.2, 90.1, 57.7, 79.3, 71.8, 75.9, 69.4, 66.8, 54.0, 65.8, 85.5, 71.3, 71.3, 50.3, 60.2, 77.5, 74.4, 69.6, 75.0, 74.5, 61.4, 75.9, 56.4, 68.9, 74.2, 65.0, 78.2, 71.6, 66.6, 67.8, 83.0, 63.4, 87.6, 67.3, 79.8, 58.3, 71.4, 53.2, 72.5, 75.4, 57.4, 59.8, 70.9, 76.7, 61.8, 65.2, 54.9, 56.1, 74.5, 66.0, 60.1, 82.3, 76.2, 58.5, 67.1, 80.2, 69.8, 61.0, 83.3, 70.6, 71.9, 79.9, 67.7, 66.5, 61.7, 78.3, 61.8, 60.0, 68.2, 88.1, 56.9, 80.5, 83.8, 71.6, 80.7, 72.9, 55.6, 70.8, 79.9, 69.9, 89.1, 70.8, 68.2, 76.5, 67.3, 81.5, 66.0, 70.3, 56.0, 63.9, 79.8, 60.3, 71.0, 69.4, 63.0, 75.7, 65.9, 64.9, 75.6, 52.9, 69.1, 77.7, 56.4, 63.8, 52.1, 71.2, 69.8, 69.0, 59.7, 67.0, 68.5, 74.0, 54.3, 75.8, 80.0, 57.0, 77.9, 64.5, 62.7, 81.6, 80.1, 83.4, 71.7, 64.9, 78.0, 83.1, 83.4, 67.2, 79.3, 55.9, 56.2, 73.7, 66.4, 64.0, 77.2, 72.8, 81.4, 73.0, 73.2, 66.1, 59.3, 71.9, 92.1, 75.1, 79.2, 68.8, 76.1, 73.3, 61.7, 83.3, 73.9, 68.5, 63.9, 72.3, 72.5, 57.2, 77.4, 79.9, 82.0, 72.6, 71.4, 78.6, 66.8, 66.3, 68.7, 88.7, 79.3, 67.8, 64.2, 64.2, 67.2, 50.1, 73.4, 87.1, 79.2, 69.4, 68.4, 92.1, 74.2, 76.9, 78.8, 72.8, 69.8, 62.5, 55.2, 75.0, 75.3, 71.6, 59.9, 74.1, 78.3, 67.7, 56.9, 76.0, 76.6]

k=7

r_rango=59.8

def test_lectura_entradas(funcion):
    "Prueba la función lectura_entradas"

    # Capturar los resultados
    archivos,k,colores=funcion("Ej_Entradas.txt")

    # Comprobar los salidas esperadas
    l_a, l_k, l_c=(['Ej_Temp_Ad.txt', 'Ej_Temp_Llen.txt'],[7, 7], ['', 'dodgerblue'])

    try:
        assert(archivos==l_a and k==l_k and colores[1]==l_c[1] and colores[0] in c)
        return print("La función lectura_entradas es correcta")
    
    except(AssertionError):
        print("La función lectura_entradas no es correcta")
        
def test_lectura_datos(funcion):
    "Prueba la función lectura_datos"

    # Capturar los resultados
    l_data=[]
    data=funcion("Ej_Temp_Ad.txt",l_data)

    # Comprobar los salidas esperadas
    s_datos=datos
    l_datos=[datos]

    try:
        assert(data==s_datos and l_data==l_datos)
        return print("La función lectura_datos es correcta")
    
    except(AssertionError):
        print("La función lectura_datos no es correcta")
        
def test_medidas(funcion):
    "Prueba la función medidas"

    # Capturar los resultados
    resultados=funcion(datos)

    # Comprobar los salidas esperadas
    s_esperadas=(69.67333333333333, 69.8, 66.0, 10.011088983849813, 59.8, 100.2219026425591)

    try:
        assert(resultados==s_esperadas)
        return print("La función medidas es correcta")
    
    except(AssertionError):
        print("La función medidas no es correcta")
        
def test_clases(funcion):
    "Prueba la función clases"

    # Capturar los resultados
    resultados=funcion(datos,k,r_rango)

    # Comprobar los salidas esperadas
    s_esperadas=[(38.79, 47.34), (47.34, 55.89), (55.89, 64.43), (64.43, 72.98), (72.98, 81.52), (81.52, 90.07), (90.07, 98.61)]

    try:
        assert(resultados==s_esperadas)
        return print("La función clases es correcta")
    
    except(AssertionError):
        print("La función clases no es correcta")
        
def test_frecuencias(funcion):
    "Prueba la función frecuencias"

    # Capturar los resultados
    resultados=funcion(datos,k)

    # Comprobar los salidas esperadas
    s_esperadas=([8.0, 48.0, 164.0, 233.0, 180.0, 72.0, 15.0],[0.011111111111111112,0.06666666666666667, 0.22777777777777777, 0.3236111111111111,0.25,0.1,0.020833333333333332],[8.0, 56.0, 220.0, 453.0, 633.0, 705.0, 720.0],[0.011111111111111112, 0.07777777777777778, 0.3055555555555556, 0.6291666666666667, 0.8791666666666667, 0.9791666666666666, 1.0])

    try:
        assert(resultados==s_esperadas)
        return print("La función frecuencias es correcta")
    
    except(AssertionError):
        print("La función frecuencias no es correcta")