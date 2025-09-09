with open("vehicle_log.txt","r") as file:
    lines=file.readlines()    
vehicle_data=[] #this list will store all the vehicle locatons we collect
for line in lines:
    parts=line.strip().split() #this will break the line into words
    if len(parts)<6:
        continue
    #now pick values one by one
    timestamp=parts[0]+" "+parts[1]
    vehicle_id = parts[2].split("=")[1]     
    latitude = parts[3].split("=")[1]
    longitude=parts[4].split("=")[1]
    speed=parts[5].split("=")[1]
    #now make a dictionary
    record={
        "time":timestamp,
        "id": vehicle_id,
        "lat":latitude,
        "lon":longitude,
        "speed":speed
    }
    #add tis record to list
    vehicle_data.append(record)
#now print the results
print("all vehicle records:\n")
for record in vehicle_data:
    print(record)
