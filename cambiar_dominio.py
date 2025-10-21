correo = input("Introduce tu correo electrónico: ")

partes = correo.split("@")

nuevo_correo = partes[0] + "@ceu.es"

print(f"Tu nuevo correo es: {nuevo_correo}")