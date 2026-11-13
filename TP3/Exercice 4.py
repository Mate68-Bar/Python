import random

x = random.randint(0, 100)
nb = 0
valeur = -1

while valeur != x:
    valeur = int(input("Deviner le nombre entre 0 et 100 : "))
    nb = nb + 1
    if valeur < x:
        print("Le nombre mystere est plus grand")
    elif valeur > x:
        print("Le nombre mystere est plus petit")
    else:
        print("Trouve ! Nombre de tours :", nb)
