# Los print que estan comentados, los utilicé para ver como iba funcionando el código.
rut = input("Ingrese su rut sin puntos ni digito verificador: ")
#genero una lista con los números ingresados y una lista con los numeros que multiplicaré
numeros_list =[2,3,4,5,6,7,2,3]
#print(numeros_list)
#cantidad_numeros=len(numeros_list)-1
#print(cantidad_numeros)
rut_list = []
for numero in rut:
    rut_list.append(int(numero)) #agregamos append para meter el nuevo numero en la lista
#print(rut_list)
rut_invertido = rut_list[::-1]
#print(rut_invertido) #para invertir el orden
producto = [x*y for x,y in zip(numeros_list,rut_invertido)]
#print(producto)
sumatoria = sum(producto)
#print(sum(producto))
modulo11 = sumatoria%11
#print(modulo11)
dv = 11 - modulo11
#print(dv)

if dv == 10:
    dv = "k"
elif dv == 11:
    dv = 0
else:
    dv=dv
print(f"Su digito verificador es: {dv}")

