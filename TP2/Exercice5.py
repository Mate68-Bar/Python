nb = int(input("Entrez un nombre entier :"))
if nb % 2 == 1 and nb > 0:
    print("Le nombre est positif et impaire")
elif nb % 2 == 1 and nb < 0:
    print("Le nombre est negatif et impaire")
elif nb % 2 == 0  and nb < 0:
    print("Le nombre est négatif et paire")
elif nb % 2 == 0 and nb > 0:
    print("Le nombre postiif et paire")
else:
    print("Le nombre est négatif et impaire")