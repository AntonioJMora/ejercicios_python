numero = input("Introduce un número entero: ")

cuenta = int(numero) % 2

if cuenta == 0:
    print(f"{numero} es un número par")
else:
    print(f"{numero} es un numero impar")