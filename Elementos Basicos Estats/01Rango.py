import pandas as pd

#escribir un programa que pregunte al usaurio por las ventas de un rango de años,
#antes y despues de aplicarles un descuento

inicio= int(input('introduce el año de ventas inicial:'))
fin= int(input('Indroduce el año final de ventas: '))

ventas= {}

for i in range(inicio, fin +1):
    ventas[i] = float(input('Introduce las ventas del año '+ str(i) +": "))
    ventas = pd.Series(ventas)
    print('Ventas \n', ventas)
    print('Ventas con descuento \n', ventas *0.9)