from numpy import sqrt
sqrt(2.0)
x=10000.0
s=1.0
kmax=100
tol=1.0e-14
for k in range(kmax):
    print(f"At iteration {k} the value of s={s}")
    s0=s
    s =0.5*(s+(x/s))
    delta_s=s-s0
    if(abs(delta_s)/x< tol):
        break
