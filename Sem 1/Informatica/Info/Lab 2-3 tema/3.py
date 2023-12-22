n = int(input("n = "))
k = int(input("k = "))
p = 1
ok = 1
while p <= k:
    if ok == 1:
        print(p, end = '')
        ok = 0
    else:
        print(",", p, end = '')
    p = p * n
print(' ')