import numpy as np
import numpy.ma as MA
m1 = MA.masked_array(range(1,9))
print m1
m2= m1.reshape(2,4) #2 rows 4 columns
print m2
m3 =MA.masked_greater(m2, 6)
print m3
print m3*100
m4 = m3 - np.ones((2,4))
print m4




 


    
