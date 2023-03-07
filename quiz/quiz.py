class registro:
    def __init__(self,ide,nombre,edad,telefono,usuario,contraseña):
        self.__ide=ide 
        self.__nombre=nombre
        self.__edad=edad
        self.__telefono=telefono
        self.__usuario=usuario
        self.__contraseña=contraseña
        
    def getveregistro(self):
        return self.__ide, self.__nombre, self.__edad, self.__telefono, self.__usuario, self.__contraseña 
    
    def getide(self):
        return self.__ide
    
    def getnombre(self):
        return self.__nombre 

    def getedad(self):
        return self.__edad
    
    def gettelefono(self):
        return self.__telefono 
    
    def getusuario(self):
        return self.__usuario
    
    def getcontraseña(self):
        return self.__contraseña
    
    def setide(self,ide):
        self.__ide=ide
    
    def setnombre(self,nombre):
        self.__nombre=nombre
    
    def setedad(self,edad):
        self.__edad=edad 

    def settelefono(self,telefono):
        self.__telefono=telefono

    def setusuaruio(self,usuario):
        self.__usuario=usuario

    def setcontraseña(self,contraseña):
        self.__contraseña=contraseña


class profesor(registro):
    def __init__(self, usuario, contraseña):
        self.__usuario=usuario
        self.__contraseña=contraseña
    
    def getusuario(self):
        return self.__usuraio 
    

    

obj=registro(1000626703, "andres", 30, 313456982, "andres.21@goma.com", "la_mejor_mascota" )


print(obj.getide(), obj.getnombre())

