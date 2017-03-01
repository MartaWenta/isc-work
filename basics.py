#A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists.

mylist = [23, "hi", 2.4e-10]

for i,count in enumerate(mylist): 
    print type(i),type(count) #i and count are either float or integer or string from mylist

for iin enumerate(mylist): 
    print type(i) #i is a tuple!

    




