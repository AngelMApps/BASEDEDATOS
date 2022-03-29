from configuration import initialization,service

initialization()

placas = service["Vehicle_License_Number"].value_counts().head(10)
for i in range(0, 10):
    print(placas.index[i])