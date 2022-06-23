import numpy as np
import sympy as sp


def tri(p):
    t=sp.symbols('t')#define varible
    n=len(p)-1#n+1 poins
    m = n//2#if n is even then m=n/2, else m=(n-1)/2
    theta = n%2#if n is even then theta=0, else theta=1
    t_k=[2*np.pi/(n+1)*i for i in range(n+1)]
    #generation cx(t)
    a=[]#a_0,a_1,...,a_n
    b=[]#b_0,b_1,...,b_n
    for k in range(n+1):
        a_k = 0
        b_k = 0
        for j in range(n+1):
            a_k += p[j][0]*np.cos(j*t_k[k])
            b_k += p[j][0]*np.sin(j*t_k[k])
        a_k = 2*a_k/(n+1)#a_k
        b_k = 2*b_k/(n+1)#b_k
        a.append(a_k)
        b.append(b_k)
    expression = 0
    for k in range(1,m+1):
        expression += (a[k]*sp.cos(k*t)+b[k]*sp.sin(k*t))
    cx = a[0]/2+expression+theta/2*a[m+1]*sp.cos((m+1)*t)#pi,x
    #generation cy(t)
    a=[]#a_0,a_1,...,a_n
    b=[]#b_0,b_1,...,b_n
    for k in range(n+1):
        a_k = 0
        b_k = 0
        for j in range(n+1):
            a_k += p[j][1]*np.cos(j*t_k[k])
            b_k += p[j][1]*np.sin(j*t_k[k])
        a_k = 2*a_k/(n+1)#a_k
        b_k = 2*b_k/(n+1)#b_k
        a.append(a_k)
        b.append(b_k)
    expression = 0
    for k in range(1,m+1):
        expression += (a[k]*sp.cos(k*t)+b[k]*sp.sin(k*t))
    cy = a[0]/2+expression+theta/2*a[m+1]*sp.cos((m+1)*t)#pi,y
    
    pix=[cx.evalf(subs={t:i}) for i in np.linspace(0,2*np.pi,100)]+[cx.evalf(subs={t:0})]
    piy=[cy.evalf(subs={t:i}) for i in np.linspace(0,2*np.pi,100)]+[cy.evalf(subs={t:0})]
    return pix,piy