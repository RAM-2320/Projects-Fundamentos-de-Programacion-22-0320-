import math

def menu():
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Raíz cuadrada")
    print("6. Elevar al cuadrado")
    print("7. Terminar")

def calculadora():
    continuar = True
    resultado = 0

    while continuar:
        menu()
        operacion = input("Ingrese el número de la operación que desea realizar: ")

        if operacion in ['1', '2', '3', '4']:
            num1 = resultado if resultado != 0 else float(input("Ingrese un primer valor: "))
            num2 = float(input("Ingrese el segundo valor: "))

            if operacion == '1':
                resultado = num1 + num2
            elif operacion == '2':
                resultado = num1 - num2
            elif operacion == '3':
                resultado = num1 * num2
            elif operacion == '4':
                resultado = num1 / num2

        elif operacion == '5':
            num = resultado if resultado != 0 else float(input("Ingrese un número: "))
            resultado = math.sqrt(num)

        elif operacion == '6':
            num = resultado if resultado != 0 else float(input("Ingrese un número: "))
            resultado = num ** 2

        elif operacion == '7':
            print("Gracias por usar la calculadora :D.")
            break

        print(f"El resultado es: {resultado}")

        opcion = input("¿Desea continuar con el resultado anterior? (1: Sí, 2: No): ")
        if opcion == '2':
            print("Gracias por usar la calculadora :D.")
            continuar = False

calculadora()

