#un constructor sabe que necesita 0,5 metros cubicos de arena por metro cuadrado
#de revoque a realizar. hacer un programa donde ingrese las medidas de una pared
#(largo y alto) expresada en metros y obtenga la cantidad de arena necesaria
#para revocarla.

arena_metro_cubico = 0.5
arena = 0
base = 0
altura = 0
arena_necesaria = 0

base = float(input("ingrese base de la pared:."))
altura = float(input("ingrese altura de la pared:."))
area = base * altura
arena_necesaria = area * arena_metro_cubico

print("se necesitan",arena_necesaria,"metros cubicos de arena")
