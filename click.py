import time
from linear import lin
from tri import tri
import numpy as np
import matplotlib.pyplot as plt

def click():
    pt=[]
    while len(pt)<1:
        plt.title('Select point with mouse', fontsize=16)
        pt = np.asarray(plt.ginput(1, timeout=-1))
    return pt[0]

def plot(p):
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
    plt.show(block=False)

p=[(0.3,0.4),(0.4,0.2),(0.5,0.6),(0.2,0.7)]#points
np.asarray(p)
while(True):
    plot(p)
    newp=click()
    if newp.any():
        p.append(newp)
        plot(p)
    if plt.waitforbuttonpress():
        break
 

plt.show()
    