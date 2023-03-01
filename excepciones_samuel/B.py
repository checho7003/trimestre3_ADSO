values = (1, 0) #Esta linea se crea una variable con el nombre 'values' donde se le asigna una 'tupla' que contiene dos parametros 
#x,y=19,30 #Esta linea está comentada y no se utiliza en el código.
#print(divmod(10,3)) #Esta linea también está comentada y si se descomenta, imprimirá el resultado de la función divmod, que divide 10 por 3 y devuelve el cociente y el resto de la división.
try: #Marca el inicio de un bloque de codigo donde se pueden manejar y manipular las excepciones.
    q, r = divmod(*values) #toma la función divmod() de Python, que toma dos argumentos y devuelve el cociente y el resto de la división entre ellos. En este caso, se utiliza el operador de desempaquetado (*) para pasar los valores de la tupla 'values' como argumentos individuales a la función divmod.
    #print('q=',q) #Esta comentada, por lo cual no se ejecutara en el programa. Sin embargo, si se descomenta esta línea, imprimirá el valor del cociente 'q' en la consola. 
    print(f'q={q}') #Imprime el valor de la variable utilizando un (format sitring)
    print(f'r={r}') #Imprime el valor de la variable utilizando un (format sitring)
except (ZeroDivisionError, TypeError) as e: #Si se produce la excepción ZeroDivisionError o TypeError, el bloque except capturará la excepción y la almacenará en la variable 'e'.
    print(type(e), e) #Se imprimirá el tipo de excepción y su mensaje.