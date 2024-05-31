valor_1 = int(input("Ingrese el primer valor: "))
valor_2 = int(input("Ingrese el segundo valor:"))

diferncia = abs(valor_1 - valor_2)

if diferncia % 2 == 0:

  print ("La suma de los valores:", valor_1 + valor_2)
elif diferncia < 10 and diferncia in [2,3,5,7]:
  print("El producto es: ", valor_1 * valor_2)
elif diferncia % 10 == 4:
  print ("Los digitos son: ", valor_1, valor_2)
else:
  print("Los valores dados no cumplen ni una condicion :(")
  print ("Los digitos dados son: ", valor_1, valor_2)
