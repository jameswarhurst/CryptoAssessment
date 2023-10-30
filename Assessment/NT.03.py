import sympy as sp

def mygcdex(a,b):
        if b==0: #If B = 0 then the linear combination of A and B is 1 and 0 
            return (1,0,a)
        else:
            q = sp.floor(a/b)
            if b > 0:
                r = a - q*b

            elif b < 0:
                r = a - (q+1)*b

            (x,y,d) = mygcdex(b,r)
            newx = y
            if b > 0:
                newy = x - q*y
            if b < 0:
                newy = x - y*(q+1)

            return (newx,newy,d)

p = mygcdex(710,310)
print(p)

#