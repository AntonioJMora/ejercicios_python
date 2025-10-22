a = float(input("Introduce la longitud del primer lado: "))

b = float(input("Introduce la longitud del segundo lado: "))

c = float(input("Introduce la longitud del tercer lado: "))

semi = (a + b + c) / 2

area = (semi * (semi - a) * (semi - b) * (semi - c)) ** 0.5

print(f"El área del triángulo es: {area}")