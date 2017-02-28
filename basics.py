mylist = [23,"hi",2.4e-10]
print mylist
count = 0
while count < 3: #while count is less than 3 
          item = mylist[count] 
          print item, mylist.index(item) #index -prints position on the list
          count += 1 #without it -neverending with 0s
