from matplotlib import pyplot as plt
import numpy as np
import sympy as sp
from linear import lin
from tri import tri
from addPoint import addPoint

p=[(0.3,0.4),(0.4,0.2),(0.5,0.6),(0.2,0.7)]#points

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

p=addPoint(p)
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
