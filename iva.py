precio_final = input("Introduce el importe final: ")
precio_final = float(precio_final)

precio_sin_iva = precio_final / 1.10
iva_pagado = precio_final - precio_sin_iva

print(f"El importe sin IVA es: {precio_sin_iva}")
print(f"El IVA pagado es: {iva_pagado}")