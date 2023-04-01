import sqlite3#Aqui se importa el modulo sqlite3

with sqlite3.connect('sqlitepython/conpython.db')as con:#Aqui establese una ruta absolua a la base de datos de SQLlite llamada "conpython.db" ubicada en el directorio "sqlitepython".
    micursor=con.cursor()#se crea un cursor para poder ejecutar comandos SQL en la base de datos, la variable "micursor" guarda el cursor
    sentencia="SELECT id,nombre,apellido FROM alumno WHERE id>=400;"#Se define una sentencia SQL que selecciona los campos "id","nombre" y "apellido" de todos los registros de la tabla "alumno" donde el valor de "id" sea mayor a 400.
    #print(micursor.execute(sentencia).fetchall())#La sentencia SQL definida anteriormente se ejecuta en la base de datos utilizando el cursor creado anteriormente. 
    # El método execute() ejecuta la sentencia SQL, y luego el método fetchall() recupera todos los resultados de la consulta. Sin embargo, esta línea está comentada y no tiene ningún efecto en la ejecución del programa.

def miselect(conexion,tabla,campo,operador,dato):#Aqui crea una funcion llamda "miselect" donde se le da como argumentos una conexion de una base de datos.
    micursor=conexion.cursor()#Se crea un cursor para poder ejecutar comandos SQL en la base de datos. La variable micursor guarda el cursor.
    sentencia=f"SELECT * FROM {tabla} WHERE {campo}{operador}'{dato}'"# Se define una sentencia SQL que selecciona todos los campos de la tabla especificada en la variable tabla donde el valor del campo 
    #especificado en la variable campo cumple la condición especificada por el operador de comparación en la variable operador y el valor a buscar en la variable dato.
    print(sentencia)#Impremite la variable sentencia SQL definida anteriormente.
    print(micursor.execute(sentencia).fetchall())#Se ejecuta la sentencia SQL en la base de datos utilizando el cursor creado anteriormente. 

miselect(con,'alumno','email','=','dbrabon2@irs.gov')#Se llama la funcion "miselect" con los argumentos especificados.


def modificar (conexion, tabla, campo, dato, id):
    micursor=conexion.cursor()
    sentencia=f"UPDATE {tabla} SET {campo}='{dato}' WHERE id='{id}'"
    micursor.execte(sentencia)
    con.commit()
    print("modificacion exitoso !!!!")

#modificaar(con,"alumno,"nombre,"Vegeta,1")
#DELETE FROM table_name WHERE condition;

def eliminar(conexion,tabla,campo,dato):
    micurosr=conexion.cursor()
    sentencia=f"DELETE FROM {tabla} WHERE {campo}='{dato}'"
    micursor.execute(sentencia)
    con.commit()
    print("Eliminacion exittosa !!!!")