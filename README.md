# agenda

import mysql.connector

conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='python')
mycursor = conn.cursor()
respuesta = "si"
numero = 0
while respuesta == "si":


    print("registrar un dato: 1")
    print("ver un dato: 2")
    print("borrar un dato: 3")
    print("modificar un dato: 4")
    numero = int(input("que quiere hacer? ",))
    if numero == 1:

        username = input("name : ", )
        email = input("email : ", )
        cc = int(input("cc : ", ))
        query = "INSERT INTO prueba(`id`, `name`, `email`, `cc`) VALUES ('','%s','%s','%i')" % (username, email, cc)
        mycursor.execute(query)
        conn.commit()
        respuesta = input("desea continuar : si / no  ", )
    elif numero==2:
        query = "SELECT * FROM prueba"
        result = mycursor.execute(query)
        print(result)
        respuesta = input("desea continuar : si / no  ", )
    elif numero == 3:
        username = input("name", )
        query = "DELETE FROM prueba WHERE name = '%s'" % username
        mycursor.execute(query)
        respuesta = input("desea continuar : si / no  ", )
    elif numero == 4:
        id = input("ID: ")
        username = input("Nuevo valor: ")
        query = "UPDATE prueba SET name='%s' WHERE id = %i" % (username, int(id))
        mycursor.execute(query)
        conn.commit()
        respuesta = input("desea continuar : si / no  ", )

