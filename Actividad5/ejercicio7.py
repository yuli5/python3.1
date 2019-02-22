#en un hospital exsiten 3 areas: urgencias, pediatria y traumatologia. el
#presupuesto anual del hospital se reparte de la siguiente manera:
#urgencias 37%
#pediatria 42%
#traumatologia 21

urgencias = 0
pediatria = 0
traumatologia = 0
presupuesto = 0

presupuesto = float(input("ingrese presupuesto anual para el hospital"))
urgencias = presupuesto * 0.37
pediatria = presupuesto * 0.42
traumatologia = presupuesto * 0.21

print("el area de urgencias recibira la cantidad de dinero de:.",urgencias)
print("el area de pediatria recibira la cantidad de dinero de:.",pediatria)
print("el area de traumatologia recibira la cantidad de dinero de:.",traumatologia)
