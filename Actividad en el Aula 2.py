datos = "oso,perro,10,5 son animales"

elementos = datos.split(',')

def es_palindromo(palabra):
    return palabra.lower() == palabra.lower()[::-1]

oso = elementos[0].strip()
perro = elementos[1].strip()
num_perros = int(elementos[2].strip())
num_osos = int(elementos[3].strip().split()[0])

print(f" {oso} {'es' if es_palindromo(oso) else 'no es'} un palindromo")
print(f" {perro} {'es' if es_palindromo(perro) else 'no es'} un palindromo")
print(f" tenemos {num_osos} {oso.capitalize()}s")
print(f" tenemos {num_perros} {perro}s")
print(f" {oso} y {perro} son animales")
