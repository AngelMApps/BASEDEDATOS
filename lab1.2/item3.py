from configuration import initialization,driver,service
import operator
initialization()

PlacasDeChoferesNoActivos = []
servicios=dict()
NombreServicioCNA=dict()

for i in range(len(driver)):
    if driver['Active'][i]=='NO':
        PlacasDeChoferesNoActivos.append(driver["Vehicle_License_Number"][i])

for i in range(len(service)):
    if service['Vehicle_License_Number'][i] in PlacasDeChoferesNoActivos:
        if service['Vehicle_License_Number'][i] in servicios:
            servicios[service['Vehicle_License_Number'][i]]+=1
        else:
            servicios[service['Vehicle_License_Number'][i]]=1

for i in range(len(driver)):
    for k,v in servicios.items():
        if k== driver["Vehicle_License_Number"][i]:
            NombreServicioCNA[driver["Name"][i]]=v
sortedDict = sorted(NombreServicioCNA.items(), key=operator.itemgetter(1), reverse=True)
print(sortedDict)
