poids=float(input("Entrez votre poids en kg: "))
taille=float(input("Entrez votre taille en mètre: "))
imc=round(poids/(taille*taille))
print("Votre IMC est de: ",imc)
if imc<20:
    print("Vous êtes en insuffisance pondérale")
elif imc<25:
    print("Vous avez un poids normal")
else:
    print("Vous êtes en surpoids")