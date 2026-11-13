debut = int(input("Donnez l’heure de début de la location (un entier) : "))
fin = int(input("Donnez l’heure de fin de la location (un entier) : "))

while debut < 0 or debut > 24 or fin < 0 or fin > 24 or debut >= fin:
    if debut < 0 or debut > 24 or fin < 0 or fin > 24:
        print("Les heures doivent être comprises entre 0 et 24 !")
    elif debut == fin:
        print("Attention ! l’heure de fin est identique à l’heure de début.")
    else:
        print("Attention ! le début de la location est après la fin ...")
    debut = int(input("Donnez l’heure de début de la location (un entier) : "))
    fin = int(input("Donnez l’heure de fin de la location (un entier) : "))

nb1 = 0
nb2 = 0
for heure in range(debut, fin):
    if heure < 7 or heure >= 17:
        nb1 = nb1 + 1
    else:
        nb2 = nb2 + 1

print("Vous avez loué votre vélo pendant")
if nb1 > 0:
    print(nb1, "heure(s) au tarif horaire de 1.0 euro(s)")
if nb2 > 0:
    print(nb2, "heure(s) au tarif horaire de 2.0 euro(s)")
prix = nb1 * 1.0 + nb2 * 2.0
print("Le montant total à payer est de", prix, "euro(s).")
