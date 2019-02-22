#ejercicio 20
#un maestro desea saber un porcentaje de hombres y que porcentaje de muejeres
#hay en un grupo de estudiantes.

print("Desea saber el porcentaje de hombres y mujeres")

PORC = 100

t = int(input("ingrese la cantidad total de alumnos:."))
h = int(input("ingrese la cantidad de hombres:."))
m = int(input("ingrese la cantidad de mujeres:."))

h1 = (h * PORC)/t
m1 = (m * PORC)/t

print("el porcentaje de hombres es{}".format(h1))
print("el procentaje de muejeres es {}".format(m1))
