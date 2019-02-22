#ejercico 18
#una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente
#desea saber cuanto debera pagar finalmente por su compra


DESC = 0.15
compra = 0
descuento = 0

compra = int(input("ingrese el costo de su compra:."))
descuento = compra * DESC
total = compra - descuento
print("su descuento es de:.{}".format(descuento))
print("el total a pagar es de:.{}".format(total))
