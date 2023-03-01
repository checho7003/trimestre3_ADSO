#def divisores(num): #Aqui se defini una funcion llamada 'divisores' que toma como parametro un 'num.'
#     for i in range(num): #Esta línea crea un bucle 'for' que itera sobre los números en el rango desde 0 hasta 'num - 1'.   
#         if num%i==0: #Esta línea de código verifica si 'i' es un divisor de 'num'. Si el resto de la división de 'num' entre 'i' es 0, entonces 'i' es un divisor de 'num' y el código dentro del bloque if se ejecuta.  
#             print(i,' es divisor')  #Esta line de codigo imprime un mensaje en la consola que indica que 'i' es un divisor de 'num'.

# try: #Marca el inicio de un bloque de codigo donde se pueden controlar y manejar posibles excepciones que pueden ocurrir durante la ejecucion del codigo.
#     divisores(19)  
# except:  

def divisores(num):  #Aqui se defini una funcion llamada 'divisores' que toma como parametro un 'num'.

    if type(num)!=int:  #Verifica si el tipo de dato del parámetro 'num' no es un número entero.
        print('Solo trabaja con numeros')  #Imprime un mensaje en la consola indicando que la funcion solo trabaja con numeros enteros 
    else:  #Si el tipo de dato de 'num' es un número entero, se ejecuta el bloque de código que sigue a else:.
        try:  #Marca el inicio de un bloque de codigo donde se pueden controlar y manejar posibles excepciones que pueden ocurrir durante la ejecucion del codigo. 
            for i in range(1,num): #Crea un bucle 'for' que itera a traves de de un rango de numeros, comenzando en 1 y terminando en 'num-1'  
                if num%i==0: #Esta línea de código verifica si 'i' es un divisor de 'num'. Si el resto de la división de 'num' entre 'i' es 0, entonces 'i' es un divisor de 'num' y el código dentro del bloque if se ejecuta.
                    print(i,' es divisor')  #Esta linea de codigo imprime en la consola si 'i' es divisor.
        except ZeroDivisionError:  #Si durante de la ejecucion del bloque 'try' se produce una excepcion 'ZeroDivisionError' el programa ejecuta el codigo dentro del bloque 'except ZeroDivsionError'
            print('Indeterminacion')  #Esta linea de codigo imprime la palabra 'indeterminacion' 
        except TypeError: #Esta excepción puede ocurrir si el usuario proporciona un argumento que no es un número entero, como una cadena o una lista.
            print('No ingreso un numero') #Esta linea de codigo imprime la palabra 'No ingreso un numero'
        except: #Esta linea de codigo maneja cualquier otra excepcion que pueda ocurrir durante la ejecucion de la funcion 'divisores'. 
            print('Error no determinado') #Imprime la palabra 'Error no determinado'
 
divisores([]) #Esta linea de codigo produce un error y no realiza la tarea prevista de imprimir los divisores de un numero.
print('El programa continua desde aqui') #Imprime la palabra 'El programa continua desde aqui'
