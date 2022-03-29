import pandas as pd

temp_carreras = dict()
CARRERA_MAS_DEMANDADA = ""
df = pd.read_csv("datos2.csv", sep=";", header=None)
for i in range(1, 107833):
    if df[11][i] == "PROFESIONAL TÉCNICO":
        if df[10][i] in temp_carreras:
            temp_carreras[df[10][i]] += 1 
        else:
            temp_carreras[df[10][i]] = 1

temp_cantidad=sorted(temp_carreras.values(),reverse=True)[0]

for k,v in temp_carreras.items():
    if str(v) == str(temp_cantidad):
        CARRERA_MAS_DEMANDADA=k
print(CARRERA_MAS_DEMANDADA)
