import numpy as np

def addPoint(p):
    while(1):
        pn=input("coordinate(x,y) (0=exit): ").split(',')
        pn=[float(i) for i in pn]
        if pn == [0]:
            break
        elif np.isreal(pn).all()==True and len(pn)==2:
            pn=p.append(pn)
        else:
            print("Invalid")
    return p