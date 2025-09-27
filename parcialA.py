#A. Cargue los datos e identifique cuantas variables categóricas(tipo object) y cuantas variables
#numéricas tiene
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np  
df=pd.read_csv("spotify-2023.csv", encoding="latin-1")
print(df.info())
print(df.describe)
print("el archivo cuenta con: \n", df.select_dtypes(include=['object']).shape[1], "object \n")
print("el archivo cuenta con : \n", df.select_dtypes(include=['int']).shape[1], "int \n")

#B. Desarrolle un algoritmo que nos diga cuantas canciones de Taylor Swift hay en la base de
#datos.
def taylor_swift (df):
    can_taylor=df[df["artist(s)_name"]=="Taylor Swift"].value_counts()
    return can_taylor
print(taylor_swift(df))
print("el numero de canciones de taylor swift en la base de datos es: \n", taylor_swift(df).shape[0])

#C. Encuentre la media de cada columna numérica en la base de datos. (Reporte solo la media de
#cada variable)

media=df.mean(numeric_only=True)
print("la media de cada columna numerica es: \n", media)

#D. Desarrolle una función que reciba como parámetro su base de datos y un año de
#lanzamiento y le devuelva la lista de todas las canciones lanzadas antes año


#E. Cree una tabla con una función de agregación, que cuente cuantas canciones
#hay de Taylor Swift y cuantas hay de Adele en la base de datos.

def adele (df):
    can_adele=df[df["artist(s)_name"]=="Adele"].value_counts()
    return can_adele
print(adele(df))
print("el numero de canciones de adele en la base de datos es: \n", adele(df).shape[0])

