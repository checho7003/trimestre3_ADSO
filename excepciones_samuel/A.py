try: #Marca el inicio de unbloque de codigo para manipular excepciones.
    #print(1/1)) #La línea 2 está comentada, pero si se descomenta esta línea, el código intentará imprimir el resultado de la división 1/1, lo cual no genera ninguna excepción.
    raise SyntaxError #La siguiente línea raise SyntaxError simula la generación de una excepción SyntaxError, que se utiliza para indicar un error de sintaxis en el código. En este caso, la excepción se levanta intencionalmente para que el bloque except se ejecute.
except SyntaxError: #El bloque except captura la excepción SyntaxError y ejecuta la instrucción print('Cierra el parentesis'), que simplemente imprime el mensaje "Cierra el parentesis" en la consola.
    print('Cierra el parentesis')

