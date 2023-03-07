class Curso: #Esta linea de codigo se crea una clase con su respectivo nombre 
    def __init__(self,titulo): #En esta linea de codigo se inicializa con su funcion y sus parametros.
        self.__titulo=titulo #Aque en esta linea se define el atributo 

    def getTitulo(self): #En esta linea se define una funcion con el parametro self
        return self.__titulo #Aqui se retorna el parametro titulo 

class Aprendiz: #Esta linea crea una subclase llamada aprendiz 
    def __init__(self,nombre): #Aqui se se inicializa el constructor con su funcion y paremtros 
        self.__nombre=nombre #En esta linea se definie el atributo nombre 
        self.__cursos=[] #Aqui se crea una lista vasia con el atributo privado __curso 

    def agregarCurso(self,nombreCursito): #En esta linea se define una funcion con sus parametros 
        cursito=Curso(nombreCursito) #En esta linea se crea un objeto llamado cursito de la clase curso con el parametro (nombrecursito)
        self.__cursos.append(cursito) #Aqui se implementa la lista 

    def getCursos(self): #Aqui se define una funcion con el metodo getCurso 
        return self.__cursos #Aqui se retorna la lista de __cursos
    
ap=Aprendiz('Sofia') #Se crea una instancia de la clase Aprendiz llamada (ap) con el valor del parametro 'sofia'
ap.agregarCurso('Python Basico') #Aqui se llama la funcion agregarCurso con el valor del parametor 'Python Basico'
ap.agregarCurso('Python Intermedio') #Aqui se llama la funcion agregarCurso con el valor del parametor 'Python Intermedio'

for c in ap.getCursos(): #Aqui se crea un ciclo (for)  que recorre cada elemento de la lista cursos(__cursos) de la instancia 'ap' de la clase 'aprendiz' y se gurada cada elemento en la variable 'c' 
    print(c.getTitulo()) #Aqui se imprime el metodo 'getTitulo' con la instancia (c) de la clase 'curso' y se imprime su resultado.