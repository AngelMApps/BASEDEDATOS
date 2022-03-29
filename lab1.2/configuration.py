import pandas as pd

driver = pd.read_csv("driver.csv", delimiter=",")
service = pd.read_csv("service.csv", delimiter=",")

# ELIMINANDO ESPACIOS EN BLANCO
def initialization():
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
    n_l=[]
    for i in lista:
        if(i not in n_l):
            n_l.append(i)
    return n_l

def buscar(valor, lista_buscar):
    for i in range(0,len(lista_buscar)):
        #print("DRIVER: ", lista_buscar[i])
        if(valor==lista_buscar[i]):
            return i,True








