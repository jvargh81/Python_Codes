f = 0
c = -100
while (c != f) :
    f = (1.8 * c) +32
    #c_nv = c
    #c = round(c,2)
    #f = round(f,2)
    if (c > f):
        #Debug message
        #print "value of f and c is %f %f*"%(f,c)
        c = c + 1
    elif (c < f):
        #Debug message
        #print "value of f and c is %f %f**"%(f,c)
        c = c - 1;



print ("The approximate value at which both f and c are equal is : %d %d " %(c, f))
    



















