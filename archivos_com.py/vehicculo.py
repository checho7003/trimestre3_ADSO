class Vehiculo: #Se crea una clase llamada "Vehiculo"
    def __init__(self,placa,conductor): #Aqui se crea el constructor con los parametros "placa" y "conductor"
        self.__placa=placa #Aqui se define el atributo placa
        self.__conductor=conductor #Aqui se define el atributo conductor 
    def getConductor(self): #Aqui se crea la funcion con el metodo "getConductor"
        return self.__conductor #Aqui retorna el atributo privado "__conductor"
    def getPlaca(self): #Aqui se define la funcion con el metodo "getPlaca"
        return self.__placa #Aqui retorna el atributo privado "__placa"