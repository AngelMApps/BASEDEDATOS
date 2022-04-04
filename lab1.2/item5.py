from configuration import initialization,eliminar,driver,service,pd
initialization()


licenses=[]
Business=[]

for i in range(0,len(service)):
    if service["lpep_pickup_datetime"][i].split('/')[0]=='28' and service["lpep_pickup_datetime"][i].split('/')[1]=='12':
        licenses.append(service['Vehicle_License_Number'][i])
licenses=eliminar(licenses)

for i in range(0,len(driver)):
    if driver["Vehicle_License_Number"][i] in licenses:
        Business.append(driver["Base_Name"][i])

Business=eliminar(Business)

res= pd.DataFrame(list(zip(Business)),columns=['Base Name'])
res.to_csv('item5.csv')
print(res)

