#Escriba una clase Empleado que tenga como propiedades
#nombre, cargo, salario
#escriba metodos contructores, setters y getters
#escriba un método que permita calcular cuanto gana el empleado en una hora
#un método para saber cuanto recibe de incremento si el salario sube con el IPC. Si gana el mínimo se le aumenta el ipc + 3%
#Un método que reciba una cantidad de horas extras y calcule el salario incrementando las extras. No puede hacer mas de dos horas diarias y trabaja de luenes a viernes. Valide
#crear una bariable de clase que aumente de uno en uno cada vez que se cree una variable persona.

class empleado:
    contador=0
    def __init__(self,nombre,cargo,salario):
        self.__nombre=nombre
        self.__cargo=cargo
        self.__salario=salario
        empleado.contador += 1

    def getmagia(self):
        return self.__nombre, self.__cargo, self.__salario, empleado.contador

    def getnombre(self):
        return self.__nombre
    
    def getcargo(self):
        return self.__cargo
    
    def getsalario(self):
        return self.__salario
    
    def setnombre(self,nombre):
        self.__nombre=nombre

    def setcatgo(self,cargo):                    
        self.__cargo=cargo                                          

    def setsalario(self,salario):
        self.__salario=salario



    def salario1(self):
        i = round(self.__salario / 240,2)
        return 'El empleado gana por hora:', i 

    def incremento (self):
        if  self.__salario == 1200000:
            self.__salario *= 1.163
            return "epa laa arepa"
        elif self.__salario < 1200000:
            return "te estan robando papu"
        elif self.__salario > 1200000:
            self.__salario = 1.133
            return "conformese con lo que le damos"
    
    def calculo(self,horas):       
        if horas <= 10:
            vl1 = round(horas * self.__salario / 240)
            self.__salario += horas * self.__salario / 240
            print("Este es el total que se gana en horas extra: ",vl1)
            print('Esta es la sumatoria del salario mas las horas extra:', self.__salario)
        else:
            print ('Solo puede hacer 10 horas como mucho a la semana.')

emple=empleado("antonio","oficinista",1200000)
print(emple.getmagia())
print(emple.getnombre())
print(emple.getcargo())
print(emple.getsalario())
print(emple.salario1())
print(emple.incremento())   
emple.calculo(8)

emple1=empleado("Julio","Gerente",3200000)
print(emple1.getmagia())
print(emple1.getnombre())
print(emple1.getcargo())
print(emple1.getsalario())
print(emple1.salario1())
print(emple1.incremento())   
emple1.calculo(12)


