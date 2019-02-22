
horas = 0 #3600 segundos
minutos = 0 #60 segundos
segundos = 0
total = 0

horas = int(input("ingrese horas:"))
minutos = int(input("ingrese minutos:."))
segundos = int(input("ingrese segundo:."))

total = (((horas * 3600) + (minutos * 60) + segundos) * 0.25)

print("costo total del proceso Bs.",total)
