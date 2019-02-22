#calcula el precio de un boleto de viaje, tomando en cuenta el numero de
#kilometros que se van a recorrer, sinedo el precio Bs/.10,50 por Km.

precio_km = 10.50
kms = 0
total = 0

kms = float(input("ingrese kilometros a recorrer:."))
total = precio_km * kms

print("precio del boleto: Bs.",total)
