#ejercicio 15
#obtener la edad de una persona en meses; si se ingresa su edad en años y meses.
#Ejemplo: ingresado 3años 4meses debe mostrar 40meses.

meses = 0
anios = 0

anios = int(input("ingrese su edad en anios:."))
meses = int(input("ingrese meses despues del anios:."))
multiplicacion = anios * 12
suma = meses + multiplicacion

print("total de su edad en meses:.{}".format(suma))
