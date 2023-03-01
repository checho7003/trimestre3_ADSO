def try_syntax(numerator, denominator): #Se define una función llamada try_syntax que toma dos argumentos, numerator y denominator.
    try: #Esta linea marca el inicio de un bloque de codigo donde se puede manipular las exceppciones.
        print(f'In the try block: {numerator}/{denominator}') #Imprime un mensaje indicando que el código se encuentra dentro del bloque try y muestra el valor de la operación de división que se realizará.
        result = numerator / denominator #Realiza la operación de división numerator / denominator y guarda el resultado en la variable result.
    except ZeroDivisionError as zde: #Si se produce una excepción de ZeroDivisionError durante la ejecución de la línea 4, el control se transfiere al bloque except.
        print(zde) #Imprime el mensaje de error almacenado en la variable zde.
    else: #Si no se produce una excepción, el control se transfiere al bloque else.
        print('The result is:', result) #Imprime el mensaje "The result is:" seguido del valor de result.
        return result #Devuelve el valor de result de la función.
    finally: #El bloque finally se ejecuta independientemente de si se produce una excepción o no.
        print('Exiting') #Imprime el mensaje "Exiting".
        #return "Fallo por zero"
#print(try_syntax(12, 4)) #Esta linea esta comentada por lo cual no se ejecuta 
print(try_syntax(11, 0)) #Llama a la función try_syntax con los argumentos 11 y 0, lo que provocará una excepción de división por cero.