#calcular el nuevo salario de un empleado si obtuvo un incremento del 8% sobre
#su salario actual y un descuento de 2,5% por servicios

salario = 0
incremento = 0
descuento = 0
total = 0

salario = float(input("ingrese salario actual:."))
incremento = salario * 0.08
descuento = salario * 0.025
total = salario+incremento-descuento
print("el incremento es :.",incremento)
print("el descuento es:.",descuento)

print("\nsalario actual:.",total)
