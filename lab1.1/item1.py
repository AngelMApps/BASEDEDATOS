import pandas as pd

df = pd.read_csv("datos2.csv", sep=';', header=None)

DEPARTAMENTOS_LOCALES_EDUCATIVOS=dict()
res=dict()

for departamento in df[2]:
    if departamento!= "NOMBRE DEPARTAMENTO":
        if departamento in DEPARTAMENTOS_LOCALES_EDUCATIVOS:
            DEPARTAMENTOS_LOCALES_EDUCATIVOS[departamento]+=1
        else:
            DEPARTAMENTOS_LOCALES_EDUCATIVOS[departamento]=1

DEPARTAMENTOS_LOCALES_EDUCATIVOS.popitem()

temp=sorted(DEPARTAMENTOS_LOCALES_EDUCATIVOS.values(),reverse=True)[:3]

for k,v in DEPARTAMENTOS_LOCALES_EDUCATIVOS.items():
    if v in temp:
        res[k]=v
        
print(res)