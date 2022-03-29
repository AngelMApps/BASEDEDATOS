import pandas as pd

temp_titulos = dict()
TITULOS_POR_DEPARTAMENTO = dict()
df = pd.read_csv("datos2.csv", sep=";", header=None)

for i in range(1, 107833):
    if len(str(df[9][i])) > 3:
        if df[9][i] not in temp_titulos:
            temp_titulos[df[9][i]] = df[2][i]
            print(df[9][i]+" - "+df[2][i])

for k, v in temp_titulos.items():
    if v in TITULOS_POR_DEPARTAMENTO:
        TITULOS_POR_DEPARTAMENTO[v] += 1
    else:
        TITULOS_POR_DEPARTAMENTO[v] = 1


