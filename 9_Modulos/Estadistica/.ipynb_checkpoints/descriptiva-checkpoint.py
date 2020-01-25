import statistics

def f_moda(data):
    "Determina la moda en un conjunto de datos, si existen modas múltiples devuelve una lista de estas"
    
    valores=list(set(data))
    l_fr = [[data.count(x)] for x in set(valores)]
    fr_max=max(l_fr)
    n_modas=l_fr.count(fr_max) 
    if n_modas>1: 
        r_moda=[]
        for i in range(len(l_fr)):
            if l_fr[i]== fr_max:
                r_moda.append(valores[i])
                r_moda.sort()
    else:
        r_moda= statistics.mode(data)
        
    return r_moda
    
def centramiento(data):
    "Cálcula la media, mediana, y moda de un conjunto de datos y las devuelve en una tupla"
    
    r_media= statistics.mean(data)
    r_mediana= statistics.median(data)
    r_moda=f_moda(data)
    
    return (r_media, r_mediana, r_moda)

def dispercion(data):
    "Devuelve el rango, la desviación estándar y la varianza de una muestra y una población, en una tupla"
    
    r_rango= max(data)-min(data)
    r_desviacion= statistics.stdev(data)
    r_p_desviacion= statistics.pstdev(data)
    r_varianza=statistics.variance(data)
    r_p_varianza=statistics.pvariance(data)

    return (r_rango, r_desviacion, r_p_desviacion, r_varianza, r_p_varianza)