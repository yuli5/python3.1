#calcular el descuento y el monto a pagar por un medicamento cualquiera en una
#farmacia si todos los medicamentos  tiene un descuento del 35%

precio = 0
descuento = 0

precio = float(input("ingrese el precio de los medicamentos:."))
descuento = precio * 0.35

print("precio del medicamento, menos descuento del 35%:.",(precio-descuento))
