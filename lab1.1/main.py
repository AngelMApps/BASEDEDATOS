from collections import OrderedDict
import pandas as pd

#ITEM 1
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

#ITEM 2
df = pd.read_csv("datos1.csv", sep=',', header=None,encoding='latin-1')
CENTROS_EDUCATIVOS = []
CORREOS=dict()

for i in range(166523):
    if (str(df[16][i])[0]=='w') and (len(str(df[16][i]).split('.'))>2) and (str(df[16][i]).split('.')[2]=='edu'):
        if len(str(df[16][i]).split('.'))>=4:
            if str(df[16][i]).split('.')[3][:2]=="pe":
                    CORREOS[i]=df[16][i]

for k,v in CORREOS.items():
    CENTROS_EDUCATIVOS.append(df[3][k])
    
CENTROS_EDUCATIVOS=list(OrderedDict.fromkeys(CENTROS_EDUCATIVOS))

for centro in CENTROS_EDUCATIVOS:
    print(centro)

#ITEM 3
#8 2 mujeres
#total-5 turno
#total-4 1 activo 2 inactivo 
