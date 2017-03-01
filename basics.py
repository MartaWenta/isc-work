with open ('weather.csv','r') as reader:
    lines = reader.readline() #read the first line
    rain=[]
    for line in reader.readlines(): #reads lines from a file
        r=line.strip().split(",")[-1] #extract the values from last column
        r= float(r) #make it a float number
        rain.append(r) #append to the rain list
print rain 

with open ('myrain2.txt','w') as writer: #save to file
  writer.write(str(rain))  
    for r in rain:                      
       writer.write(str(r)+"\n")
    

with open ('myrain2.txt','w') as writer: #save to file
  writer.write(str(rain)) #also works but not as a column of values


