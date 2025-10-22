nombre_producto = input("Introduce el nombre del producto: ")

precio = input("Introduce el precio unitario del producto: ")

unidades = input("Introduce el número de unidades: ")

precio = float(precio)
unidades = int(unidades)

coste_total = precio * unidades

print(f"Producto: {nombre_producto}")
print(f"Precio unitario: {precio:6.2f}")
print(f"Unidades: {unidades:03d}")
print(f"Coste total: {coste_total:08.2f}")