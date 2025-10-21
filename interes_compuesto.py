capital = input("Introduce la cantidad depositada en la cuenta de ahorros: ")
capital = int(capital)

interes = 0.04

ahorro1 = capital*(1+interes)
ahorro2 = ahorro1*(1+interes)
ahorro3 = ahorro2*(1+interes)

print(f"Ahorros tras el primer año: {ahorro1}")
print(f"Ahorros tras el segundo año: {ahorro2}")
print(f"Ahorros tras el tercer año: {ahorro3}")