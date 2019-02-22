#calcular el cambio de monedas en dolares y euros al ingresar cienrta cantidad
#en Bs. (tipo de cambio $=2.150Bs, Euros: 1.45 $)

DOLARES = 2150
EUROS = 3117.5
cantidad = 0
total = 0

opcion = int(input("\n1.DOLARES A Bs\n2.EUROS a Bs\ningrese su opcion:."))

if(opcion == 1):
    cantidad = float(input("ingrese cantidad en dolares:."))
    total = cantidad * DOLARES
    print("su total es de Bs.",total)
elif(opcion == 2):
    cantidad = float(input("ingrese cantidad en euros:."))
    total = cantidad * EUROS
    print("su total es Bs.",total)
else:
    print("opcion incorrecta")
