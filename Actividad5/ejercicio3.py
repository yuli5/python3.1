 #calcularmel monto a pagar en una cabina de internet si el costo por hora es
#de Bs/.1.5 y por cada 5 horas te dan una hora de promocion gratis
COSTO_HORA = 1.50
Horas = 0
promocion = 0
total = 0

horas = int(input("ingrese numero de horas:"))

if horas < 5:
    total = horas * COSTO_HORA
    print("total: Bs.",total)
else:
    promocion = Horas * COSTO_HORA
    total = promocion - COSTO_HORA
    print("total: Bs.",total)
