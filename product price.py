import numpy as np
price=np.array([30,20,10,40])
quantites=np.array([3,2,4,5])
d=np.array([20,10,5,15])
t=np.array([3,2,1,4])
n=int(input('enter product number'))
n1=int(input('enter quantity'))
t_p=((price[n-1]-((d[n-1]/100))*price[n-1])+((t[n-1]/100*price[n-1]))*n1)
print(t_p,'is the total price of the produt')
