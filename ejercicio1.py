quetzales_dolar = 7.13
dolar_quetzales = 0.13
cantidad = 0
total = 0
print("Bienvenidos al conversor".center(50,"-"))
opcion=input("1- quetzales a dolares 2- dolares a quetzales:.")

if opcion == "1":
    quetzales = input ("cantidad de quetzales")
    saldo = float(quetzales) / quetzales_dolar
    print("la conversion es {}".format(saldo))
elif opcion == "2":
    dolares = input ("cantidad de dolares")
    saldo = float(dolares) * quetzales_dolar
    print("la conversion es {}".format(saldo))
else:
    print("opcion no valida")
