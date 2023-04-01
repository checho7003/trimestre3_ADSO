import sqlite3# Se importa el módulo sqlite3 para poder trabajar con bases de datos SQLite.
with sqlite3.connect('sqlitepython/conpython.db')as con:#Aca estblese una ruta absoluta a la base de datos de SQLlite llamada 'conpython.db' ubicada en el directorio 'sqlitepython'.
    micursor=con.cursor()#Se crea un cursor para poder ejecutar comandos SQL en la base de datos. La variable micursor guarda el cursor.
    sentencia="SELECT nombre,apellido FROM alumno;"# Se define una sentencia SQL que selecciona los campos "nombre" y "apellido" de todos los registros de la tabla "alumno".
    print(micursor.execute(sentencia).fetchmany(10))#Se ejecuta la sentencia SQL en la base de datos utilizando el cursor creado anteriormente. El método execute() ejecuta 
    #la sentencia SQL, y luego el método fetchmany(10) recupera los primeros 10 resultados de la consulta. Finalmente, se imprime la lista de tuplas que contienen los resultados.

#print()#Esta linea esta en un comentario por lo tanto no se ejecuta pero de igual forma imprime