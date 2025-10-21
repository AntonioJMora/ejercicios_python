precio = input("Introduce el precio del producto (con dos decimales): ")
precio = float(precio)

euros = int(precio)
centimos = int((precio * 100) % 100)

print(f"Euros: {euros}, Céntimos: {centimos}")