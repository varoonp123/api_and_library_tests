import scipy as sp
import scipy.integrate as integrate
import scipy.special as special
import numpy as np

#integrate Bessel function of order lambda from 0 to 4.5
#returns 2 values. First is Riemann approximation. 2nd is error. 
result = integrate.quad(lambda x: special.jv(2.5,x),0,4.5)

print(result[0])

#exmaple of an improper integral

res2 = integrate.quad(lambda x: np.exp(-3*x)/(x**3), 1, np.inf)
print(res2[0])

#double integration example
#integrate xy from 0..1/2 in the y and 0 to 1-2y in the x
area = integrate.dblquad(lambda x,y: x*y, 0,.5, lambda x: 0,lambda x: 1-2*x)

print(area)

