#ejercicio 17
#un vendedor recibe un sueldo base mas un 10% extra por comision de sus ventas,
#el vendedor desea saber cuanto dinero obtendra por concepto de comisiones por
#las tres ventas que realiza en el mes y el total que recibira en el mes
#tomando en cuenta su sueldo base y comisiones.

sueldo = 0
EXTRA = 0.10
ven1 = 0
ven2 = 0
ven3 = 0
sueldo = int(input("ingrese su sueldo base:."))
ven1 = int(input("ingrese la cantidad de su venta:."))
ven2 = int(input("ingrese la cantidad de su venta:."))
ven3 = int(input("ingrese la cantidad de su venta:."))
suma = (ven1 + ven2 + ven3) * EXTRA
total = sueldo +suma
print("pago de sus comisiones:.{}".format(suma))
print("el total de sueldo es de:.{}".format(total))
