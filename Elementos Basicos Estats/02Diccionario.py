import pandas as pd

#desviacion tipica
def estadistica_notas(notas):
    notas = pd.Series(notas)
    estadisticas = pd.Series([notas.min(), notas.max(), notas.mean(), notas.std(), index=['Min', 'Max', 'Media', 'Desviacion Estandar']])
    return estadisticas

def aprobados(notas):
    notas = pd.Series(notas)
    return notas[notas >= 5].sort_values(ascending=False)

notas = {'Juan': 5.9, 'Juanita': 6.6}
