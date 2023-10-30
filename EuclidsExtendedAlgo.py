import sympy as sp 

def mygcdex(a,b):
    if b == 0: 
        return(1,0,a)
    else:
        q = sp.floor(a/b) # normal handle
        if b > 0:
            r = a - q*b
        elif b < 0:      # negative check 
            r = a - (q+1)*b

        (x,y,d) = mygcdex(b,r)
        newx = y   
        if b > 0:
            newy = x - q * y
        elif b < 0: 
            newy = x - y * (q+1)
        return (newx, newy, d)
    
print(mygcdex(710, 310))



