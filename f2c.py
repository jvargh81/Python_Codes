f = 32
c = 0
f_ans = 0
c_ans = 0
c_nv = 0
while (c != f) :
    c = (f - 32) * (0.56)
    c_nv = c
    c = round(c,2)
    f = round(f,2)
    if (f < 32):        
        c = c * (-1)
    if (c > f):
        #Debug message
        #print "value of f and c is %f %f*"%(f,c)
        f = f + 0.01
    elif (c < f):
        #Debug message
        #print "value of f and c is %f %f**"%(f,c)
        f = f - 0.01;



print "The approximate value at which both f and c are equal is : %d %d "%(c_nv, f)
    



















