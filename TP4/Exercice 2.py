# Exercice 2 : Calcul de moyennes

# Demande le nombre d'étudiants à l'utilisateur
nombreEtudiants = int(input("Donner le nombre d'etudiants : "))
moyenne = 0.0
# Déclaration d'une liste vide qui va contenir autant de notes que d'étudiants
notes = []
for i in range(nombreEtudiants):
    note = float(input("Note étudiant : "))

    while note < 0 or note > 20:
        note = float(input(f"Note invalide ! Entrez une note entre 0 et 20 pour l'étudiant {i} : "))
    notes.append(note)
    moyenne += note / nombreEtudiants
for i in range(nombreEtudiants):
    print(f"Moyenne de la classe: {moyenne}")
    ecart = notes[i] - moyenne
    print(f"Étudiant {i} : écart à la moyenne = {ecart}")