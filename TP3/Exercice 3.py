import time

n = int(input("Donner un entier positif : "))
while n < 0:
    n = int(input("Donner un entier positif : "))

# Avec for
for i in range(n, -1, -1):
    print(i)
    time.sleep(1)

# Avec while
i = n
while i >= 0:
    print(i)
    time.sleep(1)
    i = i - 1
