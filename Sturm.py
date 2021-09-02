p0 = [-2,1,0,-4,0,0,1]
grado = len(p0) - 1
p1 = []
for i in range(grado):
    p1.append(p0[i+1]*(i+1))
print (p0)
print (p1)
aux = p0[-1]/grado
print (aux)
p2 = []
for i in range(grado-1):
    p2.append(p0[i]-p1[i-1]*aux)
print (p2)
