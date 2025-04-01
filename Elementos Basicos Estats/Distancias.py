import numpy as np
import pandas as pd
from scipy.spatial import distance
 #Definimos ls coordenadas de las tiendas

tiendas={
  'Tienda A':(1,1),
  'Tienda B':(1,5),
  'Tienda C':(7,1),
  'Tienda D':(3,3),
  'Tienda E':(4,8)

 }

#Convertir las coordenadas a un dataframe para facilitar el calculo

df_tiendas = pd.DataFrame(tiendas).T
df_tiendas.columns=['X','Y']
print("coordenadas de las tiendas: ")
print(df_tiendas)

#Inicializamos un dataframe para almacenar las distancias

distancias_eu=pd.DataFrame(index=df_tiendas.index,columns=df_tiendas.index)
distancias_mh=pd.DataFrame(index=df_tiendas.index,columns=df_tiendas.index)
distancias_ch=pd.DataFrame(index=df_tiendas.index,columns=df_tiendas.index)

#Calculo de las distancias 

for i in df_tiendas.index:
    for j in df_tiendas.index:
        #Distancia Euclidiana
        distancias_eu.loc[i,j]=distance.euclidean(df_tiendas.loc[i],df_tiendas.loc[j])
        #Distancia Manhattan
        distancias_mh.loc[i,j]=distance.cityblock(df_tiendas.loc[i],df_tiendas.loc[j])
        #Distancia Chebyshev
        distancias_ch.loc[i,j]=distance.chebyshev(df_tiendas.loc[i],df_tiendas.loc[j])
        
#Mostar los Resultados
print("\n Distancias Euclideanas entre las Tiendas: ")
print(distancias_eu)
print("\n Distancias Manhattan entre las Tiendas: ")
print(distancias_mh)
print("\n Distancias Chebyshev entre las Tiendas: ")
print(distancias_ch)
