print("1.suma 2.resta 3.multi 4.division".center(50,"-")
opcion= input(":.")

if opcion == "1":
    valor1 = input("ingresa primer valor")
    valor2 = input("ingresa segundo valor")
    suma = int(valor1) + int(valor2)
    print("la suma es:. {}".format(suma))
elif opcion == "2":
    valor1 = input("ingrese primer valor")
    valor2 = input("ingresa segundo valor")
    valor3 = input("ingrese tercer valor")
    resta = int(valor1) - int(valor2) - int(valor3)
    print("la resta es:. {}".format(resta))
elif opcion == "3":
    valor1 = input("ingrese primer valor")
    valor2 = input("ingresa segundo valor")
    valor3 = input("ingrese tercer valor")
    valor4 = input("ingrese cuarto valor")
    multi = int(valor1) * int(valor2) * int(valor3) * int(valor4)
    print("la multi es:. {}".format(multi))
elif opcion == "4":
    valor1 = input("ingrese primer valor")
    valor2 = input("ingresa segundo valor")
    division = int(valor1) / int(valor2)
    print("la division es:. {}".format(division))
else:
    print("opcion no valida")
