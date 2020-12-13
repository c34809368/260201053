#BerraAvcı-260201053-HW2
filename =open("provinces.txt",encoding="utf-8")
text=filename.readlines()
provincesdict=dict()
tupnums=tuple() 
for line in text:
    line=str(line)
    linelist=line.split(",")
    provincesdict[linelist[0]]=tupnums
    linelist.remove(linelist[0]) #latitude,longitude pairs
    tupnums=tuple(linelist)

provinces=list(provincesdict.keys())
notProvince=list()

while True:
    departureProvince=input("Departure Province:\n")
    departureProvince.upper()
    if departureProvince not in provinces:
        print("Province not found!")
        lengthDep=len(departureProvince)
        for province in provinces:
            if province[:lengthDep]==departureProvince:
                notProvince.append(province)
                if len(notProvince)==1:
                    print("Possible province:"+str(notProvince))
                else:
                    possiblepro=str(notProvince)[1:-1]
                    print("Possible provinces:"+possiblepro)
        notProvince.clear()
        notProvince=list()
    else:
        arrivalProvince=input("Arrival Province:\n")
        if arrivalProvince not in provinces:
            print("Province not found!")
            lengthDep=len(arrivalProvince)
            for province in provinces:
                if province[:lengthDep]==arrivalProvince:
                    notProvince.append(province)
                    if len(notProvince)==1:
                      print("Possible province:"+str(notProvince))
                    else:
                      possiblepro=str(notProvince)[1:-1]
                      print("Possible provinces:"+possiblepro)
            notProvince.clear()
            print("Possible province:",possiblepro)
            
        else:
            if departureProvince==arrivalProvince:
                print("Enter a different province!")
                continue
            else:
                travel=input("Enter travel type:")
                travel=travel.upper()
                speed=0
                if travel=="CAR":
                    speed=90
                elif travel=="MOTORCYCLE":
                    speed=80
                elif travel=="BICYCLE":
                    speed=25
                else:
                    travel=input("Enter travel type:")
                    
                dep=provinces.index(departureProvince)
                arr=provinces.index(arrivalProvince)
                
                values=list(provincesdict.values())
                values.pop(0)
                
                depX=values[dep][0]
                depY=values[dep][1]
                arrX=values[dep][0]
                arrY=values[dep][1]
                
                dX=float(arrX)-float(depX)
                dY=float(arrY)-float(depY)
                
                distance=((dX**2)+(dY**2))**(0.5)
                distance_km=distance*100
                
                print(distance_km)                    
                