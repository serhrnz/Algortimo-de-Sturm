#determinamos el resultado del polinimio respecto a x
def HORNER(p, z):
    #si un único p es igual a uno se deben de cumplir las determinadas caracaterísticas
    if len (p)!= 1:
        n = len(p)-1
        x = p[0]
        y = x
        #definimos un rango para i
        for i in range(1,n):
            x = p[i]+z*x
            y = x+z*y
        x = p[n]+z*x
        #obtenemos el valor de x
        return x
    else:
        #si no se cumple un único p igual a 1 regresamos p
        return float(p[0])

#derivamos el polinimio 
def DERIVAR (p):
    pp = []
    for i in range (len(p)-1,0,-1):
        pp.append(p[i]*i)
    pp = list(reversed(pp))
    #obtenemos el resultado de la derivada
    return pp

#dividimos el polinimio y su derivada
def DIVIDIR (p, pp):
    #si se cumplen q y s continuamos el proceso
    while True:
        q = 0
        s = p[len(p)-1]/pp[len(pp)-1]
        #asignamos un rango para i
        for i in range (len(pp)-1,-1,-1):
            t = s*pp[i]
            w = p[(len(p)-1)-q]-t
            p[(len(p)-1)-q]=w
            q = q+1
        #obtenemos el valor de i
        i = len(p)-1
        while p [i]==0:
            p.pop(i)
            i = i-1
        #Si el polinomio es menor que la derivada detenemos el procedimiento
        if len(p)<len(pp):
            break
    #obtenemos el resultado de p para j
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
