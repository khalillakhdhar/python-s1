import oriented

Personne1= oriented.Person("khalil",35)
Personne2= oriented.Person("amine",17)
print(Personne1.greet())
if Personne1.is_adult():
    print(f"{Personne1.name} est majeur")
else:
    print(f"{Personne1.name} est mineur")
print(Personne2.greet())
if Personne2.is_adult():
    print(f"{Personne2.name} est majeur")
else:
    print(f"{Personne2.name} est mineur")
    

