#A tuple is a sequence of immutable Python objects. Tuples are sequences, just like lists.

mylist = [23, "hi", 2.4e-10]

(first, middle, last) = mylist
print first,middle,last
(first, middle, last) = (middle, last, first)
print first, middle, last

    




