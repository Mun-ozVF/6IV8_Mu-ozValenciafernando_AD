import pandas as pd
import matplotlib.pyplot as plt

#importamos documento

df = pd.read_csv("proyecto1.csv")

#1 ventas totales de comercio

vent_totales = df["ventas_tot"].sum()

print(vent_totales)

#Adeudos y no adeudos, porcentaje correspondiente


