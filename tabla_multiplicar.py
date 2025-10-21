numero = input("Introduce un numero entero: ")

print(f"Tabla de multiplicar del numero {numero}:")

for i in range(1,11):
    resultado = int(numero) * i
    print(f"{numero}x{i}={resultado}")