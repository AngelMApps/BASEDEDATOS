from configuration import initialization,service,driver
initialization()

#5480709 
#5164199 845
EMPRESAS=dict()
SERVICES=dict()

for s in service["Vehicle_License_Number"]:
    if s in SERVICES:
        SERVICES[s]+=1
    else:
        SERVICES[s]=1

for i in range(len(driver["Vehicle_License_Number"])):
    if driver["Vehicle_License_Number"][i] in SERVICES:
        if driver["Base_Name"][i] in EMPRESAS:
            EMPRESAS[driver["Base_Name"][i]]+=SERVICES[driver["Vehicle_License_Number"][i]]
        else:
            EMPRESAS[driver["Base_Name"][i]]=SERVICES[driver["Vehicle_License_Number"][i]]

print(EMPRESAS)
print(len(EMPRESAS))
