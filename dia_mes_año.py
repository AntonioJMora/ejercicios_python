fecha = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")

partes = fecha.split("/")

print(f"Dia: {partes[0]}, Mes: {partes[1]}, Año: {partes[2]}")
