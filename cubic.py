from matplotlib import pyplot as plt
import numpy as np
from scipy import interpolate

p=np.array([[0.3,0.4],[0.4,0.2],[0.5,0.6],[0.2,0.7]])#points
p.sort(axis=0)

cs=interpolate.CubicSpline(p[:,0],p[:,1])
fig=plt.figure()
x_interp=np.arange(p[0,0],p[-1,0]+0.01,0.01)
cs_interp=cs(x_interp)
plt.plot(x_interp,cs_interp,label='cubic interpolat')
plt.scatter(p[:,0],p[:,1],c='r',label='interpolationspunkte')
plt.legend()
plt.show()