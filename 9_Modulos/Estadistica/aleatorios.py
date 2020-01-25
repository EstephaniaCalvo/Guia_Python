import random

def n_aleatorios(mayor,menor=1,n=10,nd=2):
    """
    Devuelve una lista de n números aleatorios entre el rango indicado, 
    se debe ingresar obligatoriamente número mayor del rango, por defecto el número menor es 1,
    la cantidad de números es 10 y el número de decimales es 2.
    """

    d=10**nd
    aleatorios=[]
    for i in range(n):
        aleatorios.append(random.randint(menor*d,mayor*d)/d)

    return aleatorios

def normales (mu,s,n=1000,nd=2):
    """
    Devuelve una lista de n números aleatorios normales con media mu, desviación estándar s, y con número de decimales nd.
    Por defecto n es 1000 y nd es 2.
    """
    
    a_normales=[round(random.normalvariate(mu,s),nd) for x in range(n)]

    return a_normales