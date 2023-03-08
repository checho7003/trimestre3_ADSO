class registro:
    def __init__(self,ide,nombre,rol,edad,telefono,usuario,contraseña):
        self.__ide=ide 
        self.__nombre=nombre
        self.__rol=rol
        self.__edad=edad
        self.__telefono=telefono
        self.__usuario=usuario
        self.__contraseña=contraseña
        
    def getveregistro(self):
        return self.__ide, self.__nombre, self.__rol,self.__edad, self.__telefono, self.__usuario, self.__contraseña 
    
    def getide(self):
        return self.__ide
    
    def getnombre(self):
        return self.__nombre 

    def getrol(self):
        return self.__rol

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

    def setrol(self,rol):
        self.__rol=rol
    
    def setedad(self,edad):
        self.__edad=edad 

    def settelefono(self,telefono):
        self.__telefono=telefono

    def setusuaruio(self,usuario):
        self.__usuario=usuario

    def setcontraseña(self,contraseña):
        self.__contraseña=contraseña


class profesor:
    def __init__(self, usuario, contraseña):
        self.__usuario=usuario
        self.__contraseña=contraseña
        
class materias:
    def __init__(self,id,nombre,descipcion,instructor,cronograma):
        self.__id=id
        self.__nombre=nombre
        self.__descrpcion=descripcion
        self.__instructor=instructor
        self.__cronograma=cronograma

    def getid(self):
        return self.__id

    def getnombre(self):
        return self.__nombre

    def getdescrip(self):
        return self.__descripcion
    
    def getinstructor(self):
        return self.__instructor

    def getcrono(self):
        return self._cronograma

    def setcrono(self,cornograma):
        self.__conograma=cronograma
  

obj=registro (1000626703, "andres","Profesor", 30, 313456982, "andres.21@goma.com", "mascota")


print('Documento:',obj.getide(),'\n','Nombre:',obj.getnombre(),'\n','Rol:',obj.getrol(),"\n",'Edad:',obj.getedad(),'\n','Telefono:', obj.gettelefono(),'\n','Usuario:',obj.getusuario(),'\n','Contraseña:',obj.getcontraseña())

