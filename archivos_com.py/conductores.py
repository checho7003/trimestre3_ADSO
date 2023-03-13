class Conductor: #Se crea una clase llamada "Conductor"
    def __init__(self,nombre,documento): #Se define el constructo con sus parametros "nombre", "documento".
        self.__nombre=nombre #Aqui se define el atributo nombre
        self.__documento=documento #Aqui se define el atributo documento
    def getNombre(self): #Se crea un funcion con el metodo "getNombre"
        return self.__nombre #Retorna el atributo privado "__nombre"
    def getDocumento(self): #se crea una funcioncon el metodo "getDocuento"
        return self.__documento #Retorna el atributo privado "__documento"
        