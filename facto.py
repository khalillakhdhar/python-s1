x=int(input("donner un entier : "))
f=1
for i in range(2,x+1):
    f*=i
print("la factorielle de %d est %d"%(x,f))
