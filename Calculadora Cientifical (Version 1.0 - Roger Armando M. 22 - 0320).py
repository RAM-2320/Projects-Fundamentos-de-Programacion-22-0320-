import math

def menu():
    # Opciones de la calculadora
    print("Seleccione una operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Raíz cuadrada")
    print("6. Elevar al cuadrado")
    print("7. Seno")
    print("8. Coseno")
    print("9. Tangente")
    print("10. Logaritmo")
    print("11. Grados a Radianes")
    print("12. Radianes a Grados")
    print("13. Inversa de Seno")
    print("14. Inversa de Coseno")
    print("15. Inversa de Tangente")
    print("16. Elevar a una potencia personalizada")
    print("17. Terminar")

def calculadora():
    continuar = True
    resultado = 0

    while continuar:
        menu()
        operacion = input("Ingrese el número de la operación que desea realizar: ")

#Operaciones aritmeticas basicas         
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
                while True:
                    if num2 == 0:
                        print("No se puede dividir por 0! Pruebe con otro número :)")
                        num2 = float(input("Ingrese el segundo valor: "))
                    else:
                        resultado = num1 / num2
                        break

    #Operaciones de raiz cuadrada
        elif operacion == '5':
            num = resultado if resultado != 0 else float(input("Ingrese un número: "))
            if num < 0:
                print("Error: No se puede calcular la raíz cuadrada de un número negativo.")
            else:
                resultado = math.sqrt(num)

        #Operaciones de elevar al cuadrado un numero
        elif operacion == '6':
            num = resultado if resultado != 0 else float(input("Ingrese un número: "))
            while True:
                if num == 0:
                    print("Error: No se puede elevar 0 al cuadrado! Pruebe con otro número :)")
                    num = float(input("Ingrese un número: "))
                else:
                    resultado = num ** 2
                    break

        #Operacion Trigonometrica: Seno
        elif operacion == '7':
            num = resultado if resultado != 0 else float(input("Ingrese un número: "))
            resultado = math.sin(math.radians(num))

        #Operacion Trigonometrica: Coseno
        elif operacion == '8':
            num = resultado if resultado != 0 else float(input("Ingrese un número: "))
            resultado = math.cos(math.radians(num))

        #Operacion Trigonometrica: Tangente
        elif operacion == '9':
            num = resultado if resultado != 0 else float(input("Ingrese un número: "))
            resultado = math.tan(math.radians(num))

        #Logatimo de 10
        elif operacion == '10':
            num = resultado if resultado != 0 else float(input("Ingrese un número: "))
            while True:
                if num <= 0:
                    print("Error: El logaritmo no está definido para cero o números negativos.")
                    num = float(input("Ingrese un número: "))
                else:
                    resultado = math.log10(num)
                    break

        #Conversion de grados a radianes
        elif operacion == '11':
            num = resultado if resultado != 0 else float(input("Ingrese un número en grados: "))
            resultado = math.radians(num)


        #Conversion de radianes a grados
        elif operacion == '12':
            num = resultado if resultado != 0 else float(input("Ingrese un número en radianes: "))
            resultado = math.degrees(num)

        #Operacion Trigonometrica Inversa: Seno = Arcseno
        elif operacion == '13':
            num = resultado if resultado != 0 else float(input("Ingrese un número (debe estar entre -1 y 1): "))
            if num < -1 or num > 1:
                print("Error: El valor debe estar entre -1 y 1.")
            else:
                resultado = math.degrees(math.asin(num))

        #Operacion Trigonometrica Inversa: Coseno = Arccoseno
        elif operacion == '14':
            num = resultado if resultado != 0 else float(input("Ingrese un número (debe estar entre -1 y 1): "))
            if num < -1 or num > 1:
                print("Error: El valor debe estar entre -1 y 1.")
            else:
                resultado = math.degrees(math.acos(num))


        #Operacion Trigonometrica Inversa: Tangente = Arcotangente
        elif operacion == '15':
            num = resultado if resultado != 0 else float(input("Ingrese un número: "))
            resultado = math.degrees(math.atan(num))


        #Elevar a la potencia de un numero cualquiera
        elif operacion == '16':
            num = resultado if resultado != 0 else float(input("Ingrese el número base: "))
            potencia = float(input("Ingrese la potencia a la que desea elevarlo: "))
            while True:
                if num == 0 or potencia == 0:
                    print("No se puede elevar a la potencia 0! Pruebe con otros números :)")
                    num = resultado if resultado != 0 else float(input("Ingrese el número base: "))
                    potencia = float(input("Ingrese la potencia a la que desea elevarlo: "))
                else:
                    resultado = num ** potencia
                    break

        #Terminar calculadora
        elif operacion == '17':
            print("Gracias por usar la calculadora :D.")
            break

        print(f"El resultado es: {resultado}")

        opcion = input("¿Desea continuar con el resultado anterior? (1: Sí, 2: No): ")
        if opcion == '2':
            print("Gracias por usar la calculadora :D.")
            continuar = False

calculadora()

 



