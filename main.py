#iteracion sobre la lista de nombres que imprima solamente los nombres que tengan igual o mas de tres vocales.

Nombre_input = input("Ingrese su nombre: ")
vocales = ["a","e","i","o","u"]
contador_vocales = 0

for letra in Nombre_input:
  if letra in vocales:
    contador_vocales += 1

if contador_vocales >= 3:
  print ("El nombre dado tiene 3 o mas vocales :)")
else:
  print ("El nombre dado tiene menos de 3 vocales :(")