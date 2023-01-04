from ast import Pass
import getpass
from string import ascii_lowercase

# Los print que estan comentados, los utilicé para ver como iba funcionando el código.
#print(ascii_lowercase)

password = getpass.getpass("Ingrese la clave secreta solo con letras(no incluir la ñ): ").lower()

#para saber el largo de la contraseña
#nro_caracteres= int(len(password))
#print(nro_caracteres)

#genero una lista con las letras de la contraseña y una lista con las letras ascii
password_list = []
for letter in password:
    password_list.append(letter) #agregamos append para meter el nuevo caracter en la lista
#print(password_list)

ascii_list =[]
for caracter in ascii_lowercase:
    ascii_list.append(caracter)
#print(ascii_list)

#Ahora hay que comparar si son iguales las letras y contar cada comparación que haga
contador = 0
clave = []
for letter in password_list:
    for caracter in ascii_list:
        if caracter == letter:
            #print(f"letra {caracter} coincide")
            clave.append(letter)
            contador += 1
            #print(contador)
        else:
            contador += 1
            #print(contador)
#print(f"La clave secreta es: {clave} ")

clave_secreta = ""
for letra in clave:
  clave_secreta += letra
print(f"Tu contraseña es: {clave_secreta} y se encontró en {contador} intentos")
