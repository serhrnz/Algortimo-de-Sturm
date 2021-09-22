def HORNER(p, z):
    if len (p)!= 1:
        n = len(p)-1
        x = p[0]
        y = x
        for i in range(1,n):
            x = p[i]+z*x
            y = x+z*y
        x = p[n]+z*x
        return x
    else:
        return float(p[0])

def DERIVAR (p):
    pp = []
    for i in range (len(p)-1,0,-1):
        pp.append(p[i]*i)
    pp = list(reversed(pp))
    return pp

def DIVIDIR (p, pp):
    while True:
        q = 0
        s = p[len(p)-1]/pp[len(pp)-1]
        for i in range (len(pp)-1,-1,-1):
            t = s*pp[i]
            w = p[(len(p)-1)-q]-t
            p[(len(p)-1)-q]=w
            q = q+1
        i = len(p)-1
        while p [i]==0:
            p.pop(i)
            i = i-1
        if len(p)<len(pp):
            break
    p=[j*-1 for j in p]
    return p

def STURM (p,izq,der):
    valoresizq=[]
    valoresder=[]
    print ("\nP0:\n",p)
    valoresizq.append(HORNER(list (reversed(p)),izq))
    valoresder.append(HORNER(list (reversed(p)),der))
    pp = DERIVAR(p)
    valoresizq.append(HORNER(list (reversed(pp)),izq))
    valoresder.append(HORNER(list (reversed(pp)),der))
    print ("\nP1:\n",pp)
    i=2
    while True: 
        print ("\nP{:d}:".format(i))
        ppp = DIVIDIR(p,pp)
        valoresizq.append(HORNER(list (reversed(ppp)),izq))
        valoresder.append(HORNER(list (reversed(ppp)),der))
        print (ppp)
        i+=1
        if len (ppp)!= 1:
            p = pp 
            pp = ppp
        else:
            break
    print("\nPolinomios evaluados en {:d}:".format(izq))
    print(valoresizq)
    print("\nPolinomios evaluados en {:d}:".format(der))
    print(valoresder)

    sigmaizq=0
    sigmader=0
    for i in range(len(valoresizq)-1):
        if valoresizq[i]/valoresizq[i+1]<0:
            sigmaizq+=1
    for i in range(len(valoresder)-1):
        if valoresder[i]/valoresder[i+1]<0:
            sigmader+=1
    
    raices=abs(sigmaizq-sigmader)
    print("\nExisten {:d} raíces del polinomio en el intervalo [{:d},{:d}]".format(raices,izq,der))

STURM([-2,1,0,-4,0,0,1],-2,2)
