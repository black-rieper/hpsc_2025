from numpy import sqrt
sqrt(2.0)
x=9.0
s=1.0
kmax=10
for k in range(kmax):
    s=0.5*(s+(x/s))

