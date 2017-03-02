import numpy as np
a = np.arange(10)
print a
print a < 3
print np.less(a,3) #same result as above

condition = np.logical_or(a < 3, a >8)
new_a = np.where(condition, a*5, a*-5)
print new_a

print 3< a< 8
