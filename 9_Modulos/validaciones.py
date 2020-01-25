def v_num_entero(mensaje):
    "Pide un número entero mostrando el mensaje indicado, hasta que el valor ingresado sea válido"
    
    try:
        num=int(input(mensaje))
        
        return num
    except(ValueError):
        print("""
        \n------------------------------------------------------------------\n
        Ha ingresado un válor inválido vuelva a intentartlo.
        \n------------------------------------------------------------------\n
        """)
        return v_num_entero(mensaje)
    
def v_num_decimal(mensaje):
    "Pide un número décimal mostrando el mensaje indicado, hasta que el valor ingresado sea válido"

    try:
        num=input(mensaje)
        num=float(num)
        
        return num
    except(ValueError):
        print("""
        \n------------------------------------------------------------------\n
        Ha ingresado un válor inválido vuelva a intentartlo.
        \n------------------------------------------------------------------
        """)

        indice=num.index(",")

        if num[:indice].isnumeric() and num[indice+1:].isnumeric():
            print("""
        Recuerde que el décimal se índica con punto ( . ).
        \n------------------------------------------------------------------\n
        """)

        return v_num_decimal(mensaje)

def v_rango(mensaje,minimo,maximo):
    "Pide un número dentro de un rango según el mensaje indicado, hasta que el válor ingresado sea válido"

    lineas=("\n------------------------------------------------------------------\n")
    try:
        num=input(mensaje)
        num=float(num)
        try:    
            if not minimo<=num<=maximo:
                raise ValueError() 

        except(ValueError):
            print(lineas+"Recuerde ingresar un valor dentro del rango indicado."+lineas)

            return v_rango(mensaje,minimo,maximo)

    except(ValueError):
        print(lineas+"No ingresado un válor inválido vuelva a intentartlo"+lineas)

        return v_rango(mensjae)