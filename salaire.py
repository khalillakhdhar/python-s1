salaire=float(input("Entrez le salaire brut : "))
if(salaire<800):
    taxes=0
elif(salaire<1800):
    taxes=salaire*0.12
elif salaire<2400:
    taxes=salaire*0.18
else:
    taxes=salaire*0.20
salaire_net=salaire-taxes
print("le salaire brut est %f et le taux de taxes est %f et le salaire net est %f"%(salaire,taxes,salaire_net))