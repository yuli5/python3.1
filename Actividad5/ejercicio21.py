#ejercicio 21
#calcular el nuevo salario de un obrero si obtuvo un incremento del 25%
#sobre su salario anterios

INCREMENTO = 0.25
salario = 0
salario_nuevo = 0
salario = int(input("ingrese su salario:."))
salario_nuevo = salario * INCREMENTO
suma = salario_nuevo + salario
print("su salario nuevo es de:.{}".format(suma))
