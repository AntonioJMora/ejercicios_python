telefono = input("Introduce el número de teléfono (formato: +34-número-extensión): ")

partes = telefono.split("-")

print(f"El número sin prefijo ni extensión es: {partes[1]}")