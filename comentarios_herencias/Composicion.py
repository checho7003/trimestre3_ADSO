class Aprendiz: # En esta linea se crea una clase llamada Aprendiz
    def __init__(self,nombre): #Aqui se define el constructor con su paremtro (nombre)
        self.__nombre=nombre #Se inicializa el atributo privado (__nombre) con el valor del parametro 'titulo'
        self.__cursos=[] #Aqui se crea una lista vacia con el atributo privado __cursos

    def agregarCurso(self,titulo): #Se crea una funcion llamada agregarCurso con su parametro (titulo)
        self.__cursos.append(titulo) #Se agrega el título del curso dado como argumento a la lista de cursos del aprendiz. Esto se hace utilizando el método "append" de la lista, que agrega un elemento al final de la misma.

    def getCursos(self): #Aqui se crea una funcion con el metodo getCurso
        return self.__cursos #Aqui retorna la lista __cursos 

class Curso: #Aqui se crea una clase llamada Curso
    def __init__(self,titulo): #Se crea el contructor con su parametro (titulo)
        self.__titulo=titulo #Se inicializa el atributo privado (__titulo) con el valor del parametro 'titulo'

    def getTitulo(self): #Se hace una funcion con el metodo getTitulo
        return self.__titulo #Retorna el titulo del curso 
    
a=Aprendiz('Martha') #Se crea una instacia de la clase 'Aprendiz' llamada 'a' con el nombre "Martha"
c1=Curso('Python Intermedio') #Se cra una instancia de la calse 'curso' llamada 'c1' con el nombre "Python Intermedio"  
c2=Curso('Python Basico') #Se cra una instancia de la calse 'curso' llamada 'c2' con el nombre "Python Basico" 
c3=Curso('Introduccion a Java') #Se cra una instancia de la calse 'curso' llamada 'c3' con el nombre "Introduccion a Java" 

a.agregarCurso(c1) #El curso 'c1'  se agrega a la lista de cursos del aprendiz (a), utilizando el método agregarCurso que se definió previamente.
a.agregarCurso(c2) #El curso 'c2'  se agrega a la lista de cursos del aprendiz (a), utilizando el método agregarCurso que se definió previamente.
a.agregarCurso(c3) #El curso 'c3'  se agrega a la lista de cursos del aprendiz (a), utilizando el método agregarCurso que se definió previamente.

print(a.getCursos()) #Se imprime la listade cursos del aprendiz 'a' utilizando el metodo 'getCursos'


for curso in a.getCursos(): #Se inicia un bucle (for) que recorre cada elemento de la lista de cursos(__cursos) del aprendiz 'a' obtenida a través del método getCursos(). El valor de cada elemento se almacena en la variable curso.
    print(curso.getTitulo()) #Esta línea imprime el título del curso actual utilizando el método getTitulo() de la instancia de la clase Curso.