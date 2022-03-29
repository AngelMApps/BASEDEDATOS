import pandas as pd

temp_titulos = dict()
TITULOS_POR_DEPARTAMENTO = dict()
df = pd.read_csv("datos2.csv", sep=";", header=None)

print(df.columns.values)
print(df[9])
