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

"""
class profesor(registro):
    def __init__(self,credenciales):
        registro.getveregistro(self,usuario,contraseña)
   
 """       


class materias:                  
    def __init__(self,ide,nombre,descripcion,instructor,cronograma):
        self.__ide=ide
        self.nombre=nombre
        self.descripcion=descripcion
        self.instructor=instructor
        self.cronograma=cronograma

    def getvermaterias(self):
        return self.__ide, self.nombre, self.descripcion, self.instructor, self.cronograma
    
    def setid(self,ide):
        self.__ide=ide

    def setnombre(self,nombre):
        self.__nombre=nombre

    def setdescrip(self,descripcion):
        self.__descripcion=descripcion

    def setintructor(self,instructor):
        self.__instructor=instructor 

    def setcrono(self,cronograma):
        self.__cronograma=cronograma

class curso:
    def __init__(self,ide,descripcion,fecha,curso):
        self.__ide=ide
        self.descripcion=descripcion
        self.fecha=fecha
        self.curso=curso

    def getvercurso(self):
        return self.__ide, self.descripcion, self.fecha, self.curso
    
    def setide(self,ide):
        self.__ide=ide

    def setdescripcion(self,descripcion):
        self.__descripcion=descripcion

    def setfecha(self,fecha):
        self.__fecha=fecha

    def setcurso(self,curso):
        self.__curso=curso

class transacciones:
    def __init__(self,ide,detalles,telefono):
        self.__ide=ide
        self.detalles=detalles
        self.telefono=telefono

    def getvertransaccion(self):
        return self.__ide, self.detalles, self.telefono
    
    def setide(self,ide):
        self.__ide=ide

    def setdetalles(self,detalles):
        self.__detalles=detalles

    def settelefono(self,telefono):
        self.__telefono=telefono

class transaccion:
    def __init__(self,id,detalles,requerimientos,datos):
        self.__id=id
        self.detalles=detalles
        self.requerimeintos=requerimientos 
        self.datos=datos

    
    




  
obj=registro(1000626703, "andres","Profesor", 30, 313456982, "andres.21@goma.com", "mascota")
#obj1=profesor("andres.21@goma.com","mascota")
obj2=materias(15,"Matematicas","enfatizado a numeros","javier","Lunes y miercoles")
obj3=curso(2014, "Calculo dimencional", "5 de agosto", 1010)
obj4=transacciones(5014, "juan carlos, 15años, matematicas", 304695712)
obj5=transaccion()
# print("Registro","\n"'Documento:',obj.getide(),'\n','Nombre:',obj.getnombre(),'\n','Rol:',obj.getrol(),"\n",'Edad:',obj.getedad(),'\n','Telefono:', obj.gettelefono(),'\n','Usuario:',obj.getusuario(),'\n','Contraseña:',obj.getcontraseña())
# print("materias:","\n",'id:',obj2.getid(),"\n","Nombre:",obj2.getnombre(),"\n","Descripcion:",obj2.getdescrip(),"\n","Instructor:",obj2.getinstructor(),"\n","Cronograma:",obj2.getcrono())

print(obj.getveregistro())
print(obj2.getvermaterias())
print(obj3.getvercurso())
print(obj4.getvertransaccion())