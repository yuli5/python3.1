#ejercicio 26
#elabore un programa que lea 3 numeros enteros positivos y que muestre la suma
#la resta y la multiplicacion de todos.El resultado debe ser siempre positivo

valor1 = int(input("ingrese valor1:."))
valor2 = int(input("ingrese valor2:."))
valor3 = int(input("ingrese valor3:."))
suma = int(valor1) + int(valor2) + int(valor3)
resta = int(valor1) - int(valor2) - int(valor3)
multiplicacion = int(valor1) * int(valor2) * int(valor3)
print("la suma es:.{}".format(suma))
print("la resta es:.{}".format(resta))
print("la multiplicacion es:.{}".format(multiplicacion))
