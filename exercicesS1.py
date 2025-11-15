a=int(input("donner la valeur de la premiére borne de l'intervalle : "))
b=int(input("donner la valeur de la deuxiéme borne de l'intervalle : "))
somme=0
for i in range(a,b+1):
    somme=somme+i
print("la somme des entiers entre %d et %d est %d"%(a,b,somme))