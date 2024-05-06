

user = "pp@mail.com"
key = 1234
phone = 5975062


usuario = input("Usuario: ")

clave = int(input("Clave: "))

Telefono = int(input("Telefono: "))



# Usando if-else cree un sistema de login que valide las credenciales, si cumple permita iniciar
# Y si no, que imprima un mensaje de validar creedenciales

if usuario == user or phone and clave == key:
    print("Es correcto")
else:
    print("incorrecto, coloque los datos correctos")