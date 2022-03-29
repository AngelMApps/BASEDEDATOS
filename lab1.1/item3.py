import pandas as pd

df = pd.read_csv("datos1.csv", sep=",", header=None, encoding="latin-1")
lista_escuelas = []

for i in range(1, len(df)):
    if df[8][i] == "Mujeres":
        if df[39][i] == "Activa":
            turno_ver = df[37][i]
            for a in turno_ver:
                if a == "o":
                    lista_escuelas.append(df[3][i])

Escuelas_cumplen = set(lista_escuelas)
print(
    "Las escuelas que cumplen con los requisitios son las siguientes: ",
    Escuelas_cumplen,
)
