# Exercice 2

# a)
n = int(input("Donner N : "))
while n < 0:
    n = int(input("Donner N positif ou nul : "))

somme = 0
for i in range(n + 1):
    somme = somme + i
print("Somme :", somme)

# b)
valeur = int(input("Entrer 100 pour arreter : "))
while valeur != 100:
    valeur = int(input("Entrer 100 pour arreter : "))

# c)
nb1 = 0
nb2 = 0
nb3 = 0

for i in range(10):
    valeur = float(input("Donner une valeur entre 0 et 20 : "))
    while valeur < 0 or valeur > 20:
        valeur = float(input("Recommencer, entre 0 et 20 : "))

    if valeur < 10:
        nb1 = nb1 + 1
    elif valeur < 15:
        nb2 = nb2 + 1
    else:
        nb3 = nb3 + 1

print("Valeurs < 10 :", nb1)
print("Valeurs entre 10 inclus et 15 exclu :", nb2)
print("Valeurs >= 15 :", nb3)

# d)
x = float(input("Donner X > 1 : "))
while x <= 1:
    x = float(input("Recommencer, X > 1 : "))

n = 0
somme = 0
while somme + n + 1 <= x:
    n = n + 1
    somme = somme + n

print("N =", n)
