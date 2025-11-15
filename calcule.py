x=int(input("donnez un nombre entier de 3 chiffres x: "))
# si x=365=> centaine=3 , dizaine=6 , unité=5 " 3+6+5=14 non divisible par 3 => x non divisible par 3
# diviser x en centaine,dizaine,unité et verifier si x est divisible par 3
c=x//100 #centaine 3
d=(x//10)%10 #dizaine 6
u=x%10 # unité 5
somme=c+d+u
if(somme%3==0):
    print(x," est divisible par 3")
else:
    print(x," n'est pas divisible par 3")