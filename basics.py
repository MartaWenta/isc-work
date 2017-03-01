one = range(1,11)
print one
one[0]=10
print one
one.append(11)
print one
one.append([12,13,14]) #wrong [10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, [12, 13, 14]]

print one
one.extend([12,13,14])#correct 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, [12, 13, 14], 12, 13, 14]

print one

