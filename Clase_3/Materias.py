print("Mis calificaciones")

DevOps = float(input("Ingresa tu calificacion en DevOps\n"))
Ingles = float(input("Ingresa tu calificacion en Ingles\n"))
FullStack = float(input("Ingresa tu calificacion en FullStack\n"))
Redes = float(input("Ingresa tu calificacion en Redes\n"))
Sedi = float(input("Ingresa tu calificacion en Sedi\n"))

promedio = (DevOps + Ingles + FullStack + Redes + Sedi)/5

if promedio >= 6 and promedio < 7:
    print("pasaste pero checa eso porfa", promedio)

elif promedio >= 7 and promedio < 8:
    print("pasate pero puedes mejorar ")

elif promedio >= 8 and promedio < 9:
    print("Bien ahi")

elif promedio >= 9 and promedio < 10:
    print("que crack")

elif promedio == 10:
    print("excelente")

elif promedio > 10:
    print("muy bien")

else:
    print("reprobaste")

