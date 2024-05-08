usuarios = []
usuario1 = []

while len(usuarios) < 5:
    
 
    nombre = input("Agregue el nombre del usuario: ")
    usuario1.append(nombre)

    apellido = input("Agrregue el apellido del usuario: ")
    usuario1.append(apellido)

    telefono = input("Agregue el telefono del usuario: ")
    usuario1.append(telefono)

    correo = input("Agregue el correo del usuario: ")
    usuario1.append(correo)

    clave = input("Agregue la clave del usuario: ")
    usuario1.append(clave)
    
    usuarios.append(usuario1)
    


for i in usuarios:
    print(i)



