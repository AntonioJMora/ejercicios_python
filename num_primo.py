numero = input("Introduce un numero entero: ")

es_primo = True
numero = int(numero)

if (numero <= 1):
    es_primo = False
else:
    for i in range(2, numero - 1):
        if (numero % i == 0):
            es_primo = False
            break
if es_primo:
    print(f"{numero} es un numero primo")
else:
    print(f"{numero} no es un numero primo")