import numpy as np
a = np.array([range(4), range(10,14)])
print a
print np.reshape(a,(2,2,2))
print np.transpose(a)
print np.ravel(a)
print a.astype(np.float64) #change the type of an array




