print("bienvenido calculadora \nSelecione una opcion \n1 para suma \n2 para resta \n3 para multiplicar \n4 para dividir \n5 para potencia \n6 raiz cuadrada")


op = int(input("Ingrese la operacion a operar xd"))
if op != 6:
    x = int(input("ingresa x\n"))
    y = int(input("ingresa y\n"))

if op == 1:
    print(x + y)
elif op == 2:
    print(x - y)
elif op == 3:
    print(x * y)
elif op == 4:
    print(x / y)
elif op == 5:
    print(x ** y)
elif op == 6:
    x = int(input("ingresa x"))
    print(x ** 0.5)