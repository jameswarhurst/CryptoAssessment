import sympy as sp

def mygcdex(a,b):
        if b==0: #if B == 0 then we have the GCD as A, and if the B is 0 the coefficent is 1 for A
            return (1,0,a)
        else:
            q = sp.floor(a/b)
            r = a - q*b
            (x,y,d) = mygcdex(b,r)
            newx = y
            newy = x - y * (q*1)
            return (newx,newy,d)