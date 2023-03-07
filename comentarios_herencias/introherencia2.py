class A1: #Aqui se crea la clase llamdad (A1).
    def __init__(self): #Se define el contructor.  
        pass #Es el marcador de posicion para que evite un error al ejecutar el programa.
    def saludo(self): #Se crea una funcion llamda "saludo".
        print('Hola desde A1') #Iprime "Hola desde A1".

class A2: #Crea un clase llamada (A2).
    def __init__(self): #Se define el contructor.
        pass #Es el marcador de posicion para que evite un error al ejecutar el programa.
    def saludo(self): #Se crea una funcion llamada "saludo"
        print('Hola desde A2') #Imprime "Hola desde A2"


class B(A2,A1): #Se crea una clase llamada (B) donde invoca a las super clases (A2,A1)
    def __init__(self): #Se define el constructo
        pass ##Es el marcador de posicion para que evite un error al ejecutar el programa.
    def saludo(self): #Es una funcion llamada saludo 
        print('Hola desde B') #Imprime "hola desde B"
    def __str__(self): #se crea una funcion con el metodo (__str__)
        return 'Soy un objeto de la clase B' #retorna "Soy un objeto desde la clase B"
obj=B() #Se crea una instancia de las clase 'B' llamada "obj"
print(obj.__str__()) #Se imprime la funcion __str__ con las instancia "obj" de la clase "B" da como resulado "Soy un objeto de la clase B"
#obj.saludo() #Estas dos líneas están comentadas, por lo que no se ejecutan cuando se corre el programa. Si se quitan los comentarios, llamarán a la función "saludo" dos veces con la instancia "obj" de la clase "B".
#obj.saludo()


#cad="sena" #Se crea una variable llamada 'cad' y se le asiga la cadena "sena"
#lista=[1,2,3] #Se crea una variable llamad "lista" con el valor [1,2,3]
#print(cad.__str__()) #Se llama la funcion 'str()' en la variable "cad" para que imprima la cadena, se imprime "sena"  
#print(lista.__str__()) #Se llama la funcion 'str()' en la variable "lista" para que imprima la lista que se le asigno, el cual es '[1,2,3]'
