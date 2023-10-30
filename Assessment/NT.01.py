import sympy as sp

J = 2138
W = 614

def mygcd(a,b):
    if b==0: # if B is = 0, then the GCD is A
        return a
    else:
        q = sp.floor(a/b) #the Q or Quotient is calculated by dividing a/b but we only want a whole int so we use the floor function which returns the interger less than X
        r = a - q*b #We calculate the remainder by taking A and subtracting the Q * B which returns the remainder
        print(f"{a} = {b} * {q} + {r}") #We use an "f string" 
        return mygcd(b ,r)

p = mygcd(J,W)
print(f"GCD({J}, {W}) = {p}")


