# Exercice 1

tab = [1, "Eh !", 3, "Oh !"]

print(type(tab))

for val in tab :
    print (val)

tab[3] = "Ah! "
for i in range(len(tab)) :
    print(tab[i])

i=0

while i < len(tab) :
    print(tab[i])
    i+=1
