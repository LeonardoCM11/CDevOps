print("Bienvenido a la calculadora de IMC")

peso = float(input("introduce tu peso en kg"))
altura = float(input("ingresa tu altura"))

IMC = peso / (altura ** 2)


print("Tu imc es  ", round(IMC,2))

