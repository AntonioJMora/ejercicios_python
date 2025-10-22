n = int(input("Introduce el número de términos de la serie de Fibonacci: "))

a = 0
b = 1

if n >= 1:
    print(a)

if n >= 2:
    print(b)

for i in range(3, n + 1):
    siguiente = a + b
    print(siguiente)
    a = b
    b = siguiente