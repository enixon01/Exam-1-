#Emily Nixon
#Mid11
import math
def trig (a,b,c):
    firstprt=2*math.pi*a**3
    secprt=3*math.sin(b)
    thrprt=530.27*math.sqrt(c+34)
    total = firstprt+secprt+thrprt
    return total
print (trig(20,0,30))

#Mid12
def div_by_five(x):
    if x%5==0:
        print("Yes, it is!")
    elif x%5 !=0:
        print("No, it is not.")
div_by_five(10)
div_by_five(56)


