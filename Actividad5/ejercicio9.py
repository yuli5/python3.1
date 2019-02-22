#escriba un algoritmo que dado el numero de horas trabajadas por un empleado y el
#sueldo por hora, calcule el sueldo total de ese empleado. tenga en cuenta que las
#horas extras se pagan el doble.

sueldo = 0
horas_trab = 0
horas_extr = 0
total_trab = 0
total_extr = 0
total = 0

sueldo = float(input("ingrese sueldo por hora:."))
horas_trab = int(input("ingrese cantidad de horas trabajadas:."))
horas_extr = int(input("ingrese cantidad de horas extra:."))
total_trab = sueldo * horas_trab
total_extr = sueldo * horas_extr * 2
total = total_trab + total_extr

print("sueldo por horas:.",total_trab)
print("sueldo por horas extra:.",total_extr)
print("sueldo total:.",total)
