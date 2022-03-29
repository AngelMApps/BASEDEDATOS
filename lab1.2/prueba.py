import pandas as pd
import numpy as np
from datetime import datetime
from re import S


driver = pd.read_csv("driver.csv", delimiter=",")
service = pd.read_csv("service.csv", delimiter=",")

# ELIMINANDO ESPACIOS EN BLANCO
driver["Name"] = driver["Name"].apply(lambda x: x.strip())
driver["Base_Name"] = driver["Base_Name"].apply(lambda x: x.strip())
driver["Base_Website"] = driver["Base_Website"].apply(lambda x: x.strip())
driver["Base_Address"] = driver["Base_Address"].apply(lambda x: x.strip())
driver["Vehicle_License_Number"] = driver["Vehicle_License_Number"].apply(
    lambda x: x.strip()
)
driver["Active"] = driver["Active"].apply(lambda x: x.strip())

service["Vehicle_License_Number"] = service["Vehicle_License_Number"].apply(
    lambda x: x.strip()
)


def eliminar(lista):
    n_l = []
    for i in lista:
        if i not in n_l:
            n_l.append(i)
    return n_l


P = driver["Base_Name"]
S = service["Vehicle_License_Number"]
P_L = driver["Vehicle_License_Number"]
DRIVER = eliminar(P)
SERVICE = eliminar(S)
DRIVER_LICENSE = eliminar(P_L)
lista_empresas = []
numeros = []

contador = 1
for i in SERVICE:
    for a in DRIVER_LICENSE:
        if i == a:
            numeros.append(i)


for i in range(1, 4006):
    if i < len(numeros):
        print("11")
        if numeros[i] in DRIVER_LICENSE:
            print("22")
            lista_empresas.append(P[i])

# print(numero)
print(set(lista_empresas))
print(len(set(lista_empresas)))

# print(set(numeros))
# print(len(set(numeros)))
