from configuration import initialization, driver, service

initialization()

VEHICULE_NUMBER=0
for i in range(len(driver)):
    if driver["Name"][i]=="PAULINO,RAMON":
        VEHICULE_NUMBER=driver["Vehicle_License_Number"][i]
        break

print(service[service['Vehicle_License_Number']==VEHICULE_NUMBER])

