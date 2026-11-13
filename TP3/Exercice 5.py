n = int(input("Donner un entier positif : "))
while n < 0:
    n = int(input("Donner un entier positif : "))

choix = input("Choisir for ou while : ")
while choix != "for" and choix != "while":
    choix = input("Choisir for ou while : ")

f = 1
if choix == "for":
    for i in range(1, n + 1):
        f = f * i
        print(i, "! =", f)
else:
    i = 1
    while i <= n:
        f = f * i
        print(i, "! =", f)
        i = i + 1

print("Factorielle :", f)
