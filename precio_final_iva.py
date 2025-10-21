sin_iva = input("Introduce el importe total sin IVA: ")

sin_iva = int(sin_iva)

iva = input("Introduce el tipo de IVA (en porcentaje): ")

iva = int(iva)

precio_final = sin_iva + (sin_iva*iva/100)

print(f"El precio final del articulo es: {precio_final}")