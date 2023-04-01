import sqlite3# Se importa el módulo sqlite3 para poder trabajar con bases de datos SQLite.
#con=sqlite3.connect('C:\\narvaez\\db\\conpython.db')
con=sqlite3.connect('sqlitepython/conpython.db')# Se establece una conexión a la base de datos llamada "conpython.db" que se encuentra en una carpeta llamada "sqlitepython". La variable con guarda la conexión a la base de datos.
print(type(con))# Se imprime el tipo de dato de la variable con para verificar que sea una conexión a SQLite. 
micursor=con.cursor()#Se crea un cursor para poder ejecutar comandos SQL en la base de datos. La variable micursor guarda el cursor.
print(type(micursor))#Se imprime el tipo de dato de la variable micursor para verificar que sea un cursor.
sentencia="SELECT * from alumno;"# Se define una sentencia SQL que selecciona todos los registros de la tabla "alumno".
micursor.execute(sentencia)#Se ejecuta la sentencia SQL en la base de datos utilizando el cursor creado anteriormente.
for fila in micursor.fetchall():# Se recorren todos los registros devueltos por la consulta y se guarda cada uno en la variable fila.
    print(fila[0])#Se imprime el valor de la primera columna de la fila actual.
    print(fila[1])#Se imprime el valor de la segunda columna de la fila actual.
    print(fila[2])#Se imprime el valor de la tercera columna de la fila actual.
    print(fila[3])#Se imprime el valor de la caurta columna de la fila actual.
    print('-'*50)# Se imprime una línea de guiones para separar cada registro impreso en la consola.





