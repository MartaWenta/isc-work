import numpy.ma as MA
a = MA.masked_array(range(9), fill_value = -999)
print a, a.fill_value
a[2] = MA.masked
print a
print a.mask #printing the mask
b = MA.masked_where(a >6, a) #a less than 7  so the mask is set to larger than 6 
print 'b=', b 
print 'b missing values', b.fill_value
x= MA.filled(b)
print b
print type(b)


 


    
