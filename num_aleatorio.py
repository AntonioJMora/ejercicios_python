import random
min = int(input("Introduce el valor mínimo: "))

max = int(input("Introduce el valor máximo: "))

aleatorio = random.randint(min, max)

print(f"El número aleatorio generado es: {aleatorio}")