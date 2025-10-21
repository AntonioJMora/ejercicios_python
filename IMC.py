peso = input("Introduce tu peso en kg: ")
peso = float(peso)

estatura = input("Introduce tu estatura en metros: ")
estatura = float(estatura)

imc = peso / (estatura*estatura)

print(f"Tu indice de masa corporal es: {imc}")