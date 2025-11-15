# x divisible par 5=> x%5==0
# m2 x divisible par 5 si son chiffre des unités est 0 ou 5
x=int(input("donner un positif entier svp: "))
u=x%10
if u==0 or u==5:
    print("x est divisible par 5")
else:
    print("x n'est pas divisible par 5")

age=int(input("donner votre age svp: "))
if age<12:
    print("enfant")
elif age<20:
    print("adolescent")
elif age<70:
    print("adulte")
else:
    print("senior")


