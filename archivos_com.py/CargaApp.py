from Carga import * #Esta linea importa la clase "carga" desde el archivo "carga.py"
from Conductor import * #Esta linea importa la clase "conductor" desde el arhivo "conductores.py"
# c1=Conductor('Luis',12345) #
# carga1=Carga('aaa-123',c1,5,2) #
# print(carga1) #
nomConductor=input('Ingrese nombre del conductor') #Aqui crea una variable donde le pide al usuario que ingrese el nombre del conductor. 
docConductor=int(input('Ingrese documento del conductor')) #Aqui crea una variable donde le pide al usuario que ingrese el documento del conductor.
placa=input('ingrese placa') #Se crea una variable donde de pide al usuario que ingrese la placa. 
capacidad=input('ingrese capacidad en toneladas') #Se crea una variable donde le dise al usuario que ingrese la capacidad de tonelada.
ejes=input('ingrese numero de ejes') #Se crea una variable donde le pide al usuario que ingrese el numero de ejes.
c1=Conductor(nomConductor,docConductor) #Esta linea crea una instancia de la clase "Conductor" con los datos ingresados por el usuario.
obCarga=Carga(placa,c1,capacidad,ejes) #Esta linea crea una insancia de la clase "Carga" con los parametros, "placa" , "conductor" , "capacidad" y "ejes" ingresados por el usaurio
cadConductor=obCarga.getConductor().getNombre()+','+str(obCarga.getConductor().getDocumento()) #Esta linea obtiene el nombre y el documento del conductor de la instancia de "carga" creada anteriormente y los concatena en una cadena separada por una coma. 

cadCarga=obCarga.getPlaca()+','+cadConductor+','+str(obCarga.getCapacidad())+','+str(obCarga.getEjes()) #Esta linea crea una variable donde obtiene la paca, el conductor,la capacidad y los ejes de la instancia de "carga" creada anteriormente y los concatenaen una cadena separada por comas.

with open('poo-archivos/listado.txt','a') as flujo: 
    flujo.write(cadCarga+'\n') 
 #En la linea 17 y 18 la línea de código abre el archivo listado.txt en modo de escritura 
 # ('a' significa que se va a agregar información al final del archivo) y escribe la cadena cadCarga seguida de un salto de línea 
 # ('\n'). Esto significa que se está almacenando la información de la instancia de Carga creada anteriormente en el archivo listado.txt.