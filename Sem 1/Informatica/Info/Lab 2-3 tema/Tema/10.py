from numpy import append
ok = 0
cont = 0
n = int(input("n = "))
while n != 0:
    m = int(input("m = "))
    if (m == 0):
        ok = 1
        break
    cm = m
    cifN = []
    cifM = []
    nrN = 0
    nrM = 0
    cif5N = 0
    cif5M = 0
    while n > 0:
        cifN.append(int(n % 10))
        nrN += 1
        n = int(n / 10)

    while m > 0:
        cifM.append(int(m % 10))
        nrM += 1
        m = int(m / 10)

    for i in range(0, nrN):
        if cifN[i] == 5:
            cif5N += 1
    for i in range(0, nrM):
        if cifM[i] == 5:
            cif5M += 1
    if cif5M < cif5N:
        cont += 1
    n = cm
print(cont)