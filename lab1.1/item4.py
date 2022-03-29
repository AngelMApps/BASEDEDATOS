import pandas as pd

#40 fecha registro
ANIO_CREACION=dict()
res=""
df = pd.read_csv("datos1.csv", sep=',', header=None,encoding='latin-1')
for i in df[40]:
    if i !="fechareg" and len(str(i))>3:
        if i in ANIO_CREACION:
            ANIO_CREACION[i]+=1
        else:
            ANIO_CREACION[i]=1

temp=sorted(ANIO_CREACION.values(),reverse=True)[:1]

for k,v in ANIO_CREACION.items():
    if v in temp:
        res=k
        
res=res.split('-')[2]
print(res)