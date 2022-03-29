from collections import OrderedDict
import pandas as pd

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

print(CENTROS_EDUCATIVOS)
