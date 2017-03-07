import mysql.connector
conn = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='python')
mycursor = conn.cursor()
respuesta = "si"

def Operaciones():

    print("registrar un dato: 1")
    print("ver un dato: 2")
    print("borrar un dato: 3")
    print("modificar un dato: 4")

def Insert(username,email,cc):

    query = "INSERT INTO prueba(`id`, `name`, `email`, `cc`) VALUES ('','%s','%s','%i')" % (username, email, cc)
    mycursor.execute(query)
    conn.commit()

def Update(cc,username):

    query = "UPDATE prueba SET name='%s' WHERE cc = %i" % (username, int(cc))
    mycursor.execute(query)
    conn.commit()

def Select():

    query = "SELECT * FROM prueba"
    result = mycursor.execute(query)
    print(result)

def Delete(username):

    query = "DELETE FROM prueba WHERE name = '%s'" % username
    mycursor.execute(query)

while respuesta == "si":
    Operaciones()
    numero = int(input("que quiere hacer? ", ))

    if numero == 1:
        username = input("name : ", )
        email = input("email : ", )
        cc = int(input("cc : ", ))
        Insert(username,email,cc)
        respuesta = input("desea continuar : si / no  ", )

    elif numero == 2:
        Select()
        respuesta = input("desea continuar : si / no  ", )

    elif numero == 3:
        Delete(username)
        respuesta = input("desea continuar : si / no  ", )

    elif numero == 4:
        cc = int(input("cc : ", ))
        username = input("name : ", )
        Update(cc, username)
        respuesta = input("desea continuar : si / no  ", )

    else:
        print("numero de operacion invalido")
        respuesta = input("desea continuar : si / no  ", )

else:
    print("paramero invalido solo es permitido si o no.")
    print(" ")
    respuesta = input("desea continuar : si / no  ", )






