from Vehiculo import * #Esta linea importa la clase "Vehiculo" desde el archivo "Vehiculo.py"
class Carga(Vehiculo): #Aqui se crea la clase llamada "carga ", lo cual es una subclase de "Vehiculo"
    def __init__(self,placa,conductor,capacidad,ejes): #Aqui se define el constructor con sus parametros "placa", "constructor", "capacidad" y "ejes".
        Vehiculo.__init__(self,placa,conductor) #Esta linea de codigo llama al metodo constructor de la clase "Vehiculo" y le pasa los argumentos "placa" y "conductor".
        self.__conductor=conductor #AQui se define el atributo "conductor"
        self.__ejes=ejes #Aqui se define el atributo "ejes"
    def getCapacidad(self): #Aqui se crea la funcion con el metodo "getCApacidad"
        return self.__capacidad #Se retorna el atributo privao "__capacidad" 
    def getEjes(self): #Aqui se crea la funcion con el metodo "getEjes"
        return self.__ejes #Se retorna el atributo privado "__ejes"
