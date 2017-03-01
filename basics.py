def calc_hypo(a,b):
    if type(a) not in (int,float) or type(b) not in (int,float): #check!
        print 'wrong argument'
        return False
    if a <= 0 or b <= 0:
        print 'wrong argument'
        return False
    else: #we do not need else here, then hypo and return are indented as if
        hypo = (a**2 + b**2)**0.5
        return hypo

print calc_hypo(3,4)





