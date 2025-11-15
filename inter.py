a=int(input("Entrez un entier a: "))
b=int(input("Entrez un entier b: "))
for i in range(a,b+1):
    if i%3==0:
        print("%d est multiple de 3"%i)