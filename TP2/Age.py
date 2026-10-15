import datetime

annee = int(input("Donnez votre age :"))
Date = datetime.datetime.now().year - annee
print("Votre annee de naissance est : ", Date)

