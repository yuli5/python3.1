#ejercicio 16
#suponga que un individuo desea invetir su capital en un banco y desea saber
#cuanto dinero ganara despues de un año si el banco paga a razon de 2,5% mensual

PORC = 0.025
cap = 0

cap = int(input("ingrese el capital a invertir:."))
multiplicacion = cap * PORC
total = multiplicacion * 12

print("el dinero a pagar en un año es de:.{}".format(total))
