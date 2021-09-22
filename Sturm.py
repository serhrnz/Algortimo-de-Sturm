#Se define la función HORNER que evalúa el polinomio p en el valor z
def HORNER(p, z):
    #Si la longitud de p es mayor a 1, se realiza el algoritmo de manera normal
    if len (p)!= 1:
        n = len(p)-1
        x = p[0]
        y = x
        #Definimos un rango para i
        for i in range(1,n):
            x = p[i]+z*x
            y = x+z*y
        x = p[n]+z*x
        #Obtenemos el valor del polinomio evaluado en z
        return x
    else:
        #Si la longitud de p es 1, significa que en realidad es una constante, ya que es de grado 0, por lo que únicamente pediremos que nos regrese el valor del único elemento
        return float(p[0])

#Se define la función DERIVAR que nos devuelve la derivada del polinomio p
def DERIVAR (p):
    pp = []
    for i in range (len(p)-1,0,-1):
        pp.append(p[i]*i)
    pp = list(reversed(pp))
    #Obtenemos la derivada
    return pp

#Se define la función que nos permitirá dividir dos polinomios
def DIVIDIR (p, pp):
    while True:
        q = 0
        s = p[len(p)-1]/pp[len(pp)-1]
        #Asignamos el rango de iteraciones para i
        for i in range (len(pp)-1,-1,-1):
            t = s*pp[i]
            w = p[(len(p)-1)-q]-t
            p[(len(p)-1)-q]=w
            q = q+1
        #Asignamos a i el valor del grado del polinomio
        i = len(p)-1
        while p [i]==0:
            p.pop(i)
            i = i-1
        #Si el polinomio es menor que la derivada detenemos el proceso
        if len(p)<len(pp):
            break
    p=[j*-1 for j in p]
    return p

def STURM (p,izq,der):
    #Se declaran las listas que contendrán los resultados de los polinomios obtenidos, evaluados en los extremos izquierdo y derecho de nuestro intervalo
    valoresizq=[]
    valoresder=[]
    print ("\nP0:\n",p)
    #Se agregan a cada lista el resultado de evaluar p0 en los extremos
    valoresizq.append(HORNER(list (reversed(p)),izq))
    valoresder.append(HORNER(list (reversed(p)),der))
    pp = DERIVAR(p)
    #Se agregan a cada lista el resultado de evaluar p1 en los extremos
    valoresizq.append(HORNER(list (reversed(pp)),izq))
    valoresder.append(HORNER(list (reversed(pp)),der))
    #Imprimimos el valor de pp como P1 
    print ("\nP1:\n",pp)
    #Se inicia el contador de los siguientes Pi polinomios
    i=2
    while True: 
        print ("\nP{:d}:".format(i))
        ppp = DIVIDIR(p,pp)
        #Se agregan a cada lista el resultado de evaluar Pi en los extremos
        valoresizq.append(HORNER(list (reversed(ppp)),izq))
        valoresder.append(HORNER(list (reversed(ppp)),der))
        print (ppp)
        #Se incrementa el contador de polinomio en 1, cada vez que se haga una división
        i+=1
        #Se hace la división de los elementos de las listas hasta obtener una constante como residuo
        if len (ppp)!= 1:
            p = pp 
            pp = ppp
        else:
            break
    #Se imprimen las dos listas de los polinomios evaluados en el extremo izquierdo y derecho
    print("\nPolinomios evaluados en {:d}:".format(izq))
    print(valoresizq)
    print("\nPolinomios evaluados en {:d}:".format(der))
    print(valoresder)
    #Se declaran las sigmas (izq y der) se contarán los cambios de signo en los valores obtenidos de los polinomios
    sigmaizq=0
    sigmader=0
    for i in range(len(valoresizq)-1):
        if valoresizq[i]/valoresizq[i+1]<0:
            sigmaizq+=1
    for i in range(len(valoresder)-1):
        if valoresder[i]/valoresder[i+1]<0:
            sigmader+=1
    #El valor absoluto de la diferencia de las sigmas, es el número de raíces que tiene el polinomio dentro del intervalo
    raices=abs(sigmaizq-sigmader)
    #Imprimimos el número de raíces del polinomio
    print("\nExisten {:d} raíces del polinomio en el intervalo [{:d},{:d}]".format(raices,izq,der))
#Este es nuestro programa principal, donde llamamos a nuestra función principal con los parámetros que se desee
STURM([-2,1,0,-4,0,0,1],-2,2)
