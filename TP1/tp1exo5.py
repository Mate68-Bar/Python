# tp1exo5.py

jour = int(input("Veuillez saisir le jour : "))
heure = int(input("Veuillez saisir l'heure : "))
minute = int(input("Veuillez saisir la minute : "))

minutes_ecoulees = (jour - 1) * 24 * 60 + heure * 60 + minute

print(minutes_ecoulees)
