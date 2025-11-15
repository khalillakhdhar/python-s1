#un entier est premier si il n'est divisible que par 1 et par lui même
n=int(input("donner un entier positif n: "))
if n==0 or n==1:
    print("%d n'est pas un nombre premier"%n)
else:
    premier=True
    for i in range(2,n):
        if n%i==0:
            premier=False
            break
    if premier:
        print("%d est un nombre premier"%n)
    else:
        print("%d n'est pas un nombre premier"%n)
#solution avec while
n=int(input("donner un entier positif n: "))
if n==0 or n==1:
    print("%d n'est pas un nombre premier"%n)
else:
    premier=True
    i=2
    while i< (n/2)+1:
        if n%i==0:
            premier=False
            break
        i+=1
    if premier:
        print("%d est un nombre premier"%n)
    else:
        print("%d n'est pas un nombre premier"%n)