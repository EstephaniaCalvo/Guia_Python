c=['aquamarine', 'bisque', 'blue', 'blueviolet', 'brown', 'burlywood', 'chartreuse', 'chocolate', 'coral', 'cornflowerblue', 'crimson', 'cyan', 'dgreen', 'lightblue', 'lightcoral', 'lightgreen', 'lightgrey', 'lightpink', 'lightsalmon', 'lightseagreen', 'lightslategrey', 'lime', 'limegreen', 'magenta', 'maroon', 'mediumaquamarine', 'mediumblue', 'mediumorchid', 'mediumpurple', 'mediumseagreen', 'mediumslateblue', 'mediumspringgreen', 'mediumturquoise', 'mediumvioletred', 'midnightblue', 'moccasin', 'navajowhite', 'navy', 'olive', 'olivedrab', 'orange', 'orangered', 'orchid', 'palegoldenrod', 'palegreen', 'paleturquoise', 'palevioletred', 'peachpuff', 'peru', 'pink', 'plum', 'purple', 'rebeccapurple', 'red', 'rosybrown', 'royalblue', 'saddlebrown', 'salmon', 'sandybrown', 'seagreen', 'sienna', 'skyblue', 'slateblue', 'slategrey', 'springgreen', 'steelblue', 'tan', 'teal', 'thistle', 'tomato', 'turquoise', 'violet', 'wheat', 'yellow', 'yellowgreen']

# Caso 1: Data con números decimales, negativos y con moda múltiple.

data_1=[0.27, 4.29, -7.72, 2.87, -1.12, -2.6, 2.97, 3.55, 1.81, -1.33, 2.6, 0.93, 5.07, -1.8, 0.52, 2.7, 5.53, 1.2, 6.64, 0.23, 3.71, 3.61, 2.36, 4.01, 2.23, 4.5, 1.5, 2.84, -2.74, -0.56, 1.74, 3.37, 2.98, 5.27, -0.73, -2.34, 1.89, -4.35, 1.2, 4.07, 2.35, 3.76, -0.73, 2.48, -0.25, 2.13, 0.0, 2.95, -1.87, 5.42, 2.95, 1.14, 3.67, -3.81, -3.13, 3.64, 2.46, 4.55, -3.79, -4.41, -0.29, 4.33, 8.78, 0.26, -0.2, -0.39, 0.57, -0.63, 3.62, -3.6, 0.1, 1.55, 8.24, 4.79, -0.11, 4.54, 6.52, 4.57, 4.29, -0.13, 1.67, 2.56, 1.42, -0.14, 6.27, 3.16, -1.13, 3.74, 4.04, -0.27, 1.78, -1.39, 11.65, 2.94, -2.68, -1.85, 4.17, 2.4, 4.85, 4.61]

medidas_1=(1.7529, 2.1799999999999997, [-1.8, -0.73, 2.95, 4.29], 3.107965099644148, 19.37, 9.65944706060606)

clases_1=[[-7.72, -3.846], [-3.846, 0.028], [0.028, 3.902], [3.902, 7.776], [7.776, 11.65]]

tabla_1=([3.0, 28.0, 45.0, 21.0, 3.0], [0.03, 0.28, 0.45, 0.21, 0.03], [3.0, 31.0, 76.0, 97.0, 100.0], [0.03, 0.31, 0.76, 0.97, 1.0])

# Caso 2: Data con números enteros y con moda única.

data_2=[1.0, 2.0, 2.0, 3.0, 3.0, 3.0, 4.0, 4.0, 4.0, 4.0, 5.0, 5.0, 5.0, 5.0, 5.0, 6.0, 6.0, 6.0, 6.0, 6.0, 6.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0, 7.0]

medidas_2=(5.0, 5.0, 7.0, 1.7638342073763937, 6.0, 3.111111111111111)

clases_2=[[1.0, 1.9], [1.9, 2.7], [2.7, 3.6], [3.6, 4.4], [4.4, 5.3], [5.3, 6.1], [6.1, 7.0]]

tabla_2=([1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0], [0.03571428571428571, 0.07142857142857142, 0.10714285714285714, 0.14285714285714285, 0.17857142857142858, 0.21428571428571427, 0.25], [1.0, 3.0, 6.0, 10.0, 15.0, 21.0, 28.0], [0.03571428571428571, 0.10714285714285714, 0.21428571428571427, 0.35714285714285715, 0.5357142857142857, 0.75, 1.0])