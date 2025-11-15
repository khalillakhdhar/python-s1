def estMajeur(age): #function : => indentation (4 spaces)
    if age>=18:
        return True
    else:
        return False


age=int(input("donnez un age à vérifier: "))
if(estMajeur(age)):
    print("la personne est majeure")
else:
    print("la personne est mineure")
# print(message) ecrire
#var= input(message à afficher) => lire une valeur au clavier dans var
c=input("appuyez sur une touche pour quitter")
# pour convertir int(c) ou float(c) ou double(c)
