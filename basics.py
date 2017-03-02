band = (["mel","geri","victoria","mel","emma"])
counts = {}

for name in band:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1

for name in counts:    #in order to print all names not only the first one
    print name, counts[name] #prints name and number of times it appears

