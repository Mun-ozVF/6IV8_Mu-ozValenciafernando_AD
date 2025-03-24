import numpy as np
import matplotlib.pyplot as plt

#vamos a crear una semilla random para reproductividad
np.random.seed(0)

#buscamos los parametros para una distribcion
#Media

media = 0

#Desviasion estandar
sigma1 = 1
sigma2 = 2
sigma3 = 3

#El numero de muestras para el anailisis
n_muestras = 1000

#generamos los datos de las distribusiones normales

data1 = np.random.normal(media, sigma1, n_muestras)
data2 = np.random.normal(media, sigma2, n_muestras)
data3 = np.random.normal(media, sigma3, n_muestras)

#Configura la grafica
plt.figure(figsize=(10,6))

#Carga las frecuencias a partir de una grafica de histograma
plt.hist(data1, bins=30, color="blue", density=True, label="Desviacion Estandar = 1", alpha =0.5)
plt.hist(data2, bins=30, color="green", density=True, label="Desviacion Estandar = 2", alpha =0.5)
plt.hist(data3, bins=30, color="orange", density=True, label="Desviacion Estandar = 3", alpha =0.5)

#a Graficar

plt.title("Comparacion de Distribuciones normales con una semilla en random")
plt.xlabel("Valor")
plt.ylabel("Densidad")
plt.axhline(0, color="Black", linewidth=0.5, ls="--")
plt.axvline(0, color="Black", linewidth=0.5, ls="--")
plt.legend()
plt.grid()
plt.show()
