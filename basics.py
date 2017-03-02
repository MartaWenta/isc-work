import numpy as np

a = np.array([2, 3.2, 5.5, -6.4, -2.2, 2.4])
print a
print a[1]
print a[1:4]

b = np.array([[2, 3.2, 5.5, -6.4, -2.2, 2.4],
             [1, 22, 4, 0.1, 5.3, -9],
             [3, 1, 2.1, 21, 1.1, -2]]) #nawiasyyy!!!!

print b
print b[:,3]
print b[1:4,0:4]
print b[1:,2]
print b[:]

