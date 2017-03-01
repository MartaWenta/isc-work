with open ('weather.csv','r') as reader:
    line = reader.readline() #read the first line
    while line: #loop which continues until readline() returns empty string
        print line
        line = reader.readline()
    print "the end"


    




