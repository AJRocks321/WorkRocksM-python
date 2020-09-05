import random
import math

p=3.14159265
a=float(input("give number of sides you want "))
b=float(input("also type size for graph"))
m=2*p/a #per sector
c1=float(input("give special point"))
c2=float(input())
n=int(input("number of output points"))

t=int(a)
sin=[]
cos=[]
for i in range(t):
    sin.append(float(math.sin(i*m)))
    cos.append(float(math.cos(i*m)))

#coordinates of main polygon
x=[]
y=[]
for j in range(t):
    x.append(float(b*cos[j]))
    y.append(float(b*sin[j]))

#there are n points* 01234..(n-1)
for k in range(n):
    h=random.randint(0,t)
    for l in range(t):
    	if (h==l):
    		c1=float(c1+x[l])/2
    		c2=float(c2+y[l])/2
    		print(c1," ",c2)
    		break
    
