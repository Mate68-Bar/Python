# Exerice 3 : Produit scalaire

nMax = 10
v1 = []
v2 = []
n = int(input("Quelle est la taille de vos vecteurs [entre 1 et 10] ? "))
while not (n >= 1 and n <= nMax):
    n = int(input("Entrez une taille valide : "))
for i in range(n):
    nombre = int(input(f"Entrez le nombre pour v1[{i}] : "))
    v1.append(nombre)
for i in range(n):
    nombre1 = int(input(f"Entrez le nombre pour v2[{i}] : "))
    v2.append(nombre)
produit = 0
for i in range(n):
    produit += v1[i] * v2[i]
print(f"Le produit scalaire de v1 par v2 vaut {produit}")
