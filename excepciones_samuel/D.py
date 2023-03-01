def edad(): #Se define una función llamada edad.
    try: #Esta linea marca el inicio de un bloque de codigo donde se puede manipular las exceppciones
        tuedad=int(input("introduce tu edad")) #Solicita al usuario que introduzca su edad, convierte la entrada en un número entero y lo asigna a la variable tuedad.
        print(f'tu edad es  {tuedad}') #Imprime un mensaje que muestra la edad del usuario.
        #print('Tu edad es ',tuedad) #Esta linea esta comentada por lo tanto no se ejecutara en el prorama.
    except ValueError as e: #Si se produce una excepción de ValueError durante la ejecución de la línea 3, el control se transfiere al bloque except.
        print(e) #Imprime el mensaje de error almacenado en la variable e.
        print("La edad debe ser un valor numerico...") #Imprime un mensaje de error que indica que la edad debe ser un valor numérico.
        edad() #Llama a la función edad de forma recursiva.
    else: #Si no se produce una excepción, el control se transfiere al bloque else.
        print('Viene por el else') #Imprime un mensaje indicando que el control llegó al bloque else.

edad() #Llama a la función edad para iniciar el proceso de solicitud de edad al usuario.

