from matplotlib import pyplot as plt
import numpy as np
import sympy as sp
from linear import lin
from tri import tri

p=[(0.3,0.4),(0.4,0.2),(0.5,0.6),(0.2,0.7)]#points


while(1):
    pn=input("coordinate(x,y) (0=exit): ").split(',')
    pn=[float(i) for i in pn]
    if pn == [0]:
        break
    elif np.isreal(pn).all()==True and len(pn)==2:
        pn=p.append(pn)
    else:
        print("Invalid")

n=len(p)-1
pix,piy=tri(p)
x,y=lin(p)

plt.plot(x,y,label='linear interpolat')
plt.plot(pix,piy,label='trigonometric interpolat')
plt.scatter(x,y,label='interpolationspunkte')
for i in range(n+1):
    plt.annotate('p'+str(i),p[i],(p[i][0]+0.01,p[i][1]+0.01))#annotate
plt.legend()
plt.show(block=False)

while(1):
    pn=input("coordinate(x,y) (0=exit): ").split(',')
    pn=[float(i) for i in pn]
    if pn == [0]:
        break
    elif np.isreal(pn).all()==True and len(pn)==2:
        pn=p.append(pn)
    else:
        print("Invalid")

n=len(p)-1
pix,piy=tri(p)
x,y=lin(p)
plt.clf()
plt.plot(x,y,label='linear interpolat')
plt.plot(pix,piy,label='trigonometric interpolat')
plt.scatter(x,y,label='interpolationspunkte')
for i in range(n+1):
    plt.annotate('p'+str(i),p[i],(p[i][0]+0.01,p[i][1]+0.01))#annotate
plt.legend()
plt.draw()
plt.show()
