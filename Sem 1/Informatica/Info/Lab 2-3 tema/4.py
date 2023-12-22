n = int(input("n = "))
digits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while n > 0:
    u = int(n % 10)
    digits[u] += 1
    n /= 10
for i in range(0, 10, 1):
    print(digits[i], end=' ')
    