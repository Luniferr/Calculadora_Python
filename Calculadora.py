def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: No se puede dividir por cero"
    return a / b

def es_entero(numero):
    return numero.is_integer()

def es_par(numero):
    return numero % 2 == 0

while True:
    print("Menu:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Comprobar si un número es entero")
    print("6. Comprobar si un número es par")
    print("7. Salir")

    try:
        opcion = int(input("Ingresa el número de la operación que deseas realizar: "))
    except ValueError:
        print("Error: Ingresa un número válido.")
        continue

    if opcion == 7:
        print("Hasta la próxima.")
        break

    if opcion in (1, 2, 3, 4):
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Ingresa números válidos.")
            continue

        if opcion == 1:
            print(f"Resultado: {suma(num1, num2)}")
        elif opcion == 2:
            print(f"Resultado: {resta(num1, num2)}")
        elif opcion == 3:
            print(f"Resultado: {multiplicacion(num1, num2)}")
        elif opcion == 4:
            print(f"Resultado: {division(num1, num2)}")
    elif opcion == 5:
        try:
            numero = int(input("Ingresa un número para comprobar si es un entero: "))
        except ValueError:
            print("Error: Ingresa un número entero válido.")
            continue

        if es_entero(numero):
            print(f"{numero} es un número entero.")
        else:
            print(f"{numero} no es un número entero.")
    elif opcion == 6:
        try:
            numero = int(input("Ingresa un número para comprobar si es par: "))
        except ValueError:
            print("Error: Ingresa un número entero válido.")
            continue

        if es_par(numero):
            print(f"{numero} es un número par.")
        else:
            print(f"{numero} no es un número par.")
    else:
        print("Error: Opción no válida. Ingresa un número del 1 al 7.")
