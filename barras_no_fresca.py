precio_normal = 3.49
descuento = 0.60

barras_no_frescas = input("Introduce el número de barras no frescas vendidas: ")
barras_no_frescas = int(barras_no_frescas)

precio_descuento = precio_normal *(1-descuento)
coste_total = precio_descuento * barras_no_frescas

print(f"Precio habitual de una barra de pan: {precio_normal}€")
print(f"Descuento aplicado: {descuento*100}%")
print(f"Coste total por las barras no frescas: {coste_total}€")