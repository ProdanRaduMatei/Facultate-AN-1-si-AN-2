def CommonDigits(N, M):
    count = 0
    freq1 = [0] * 10
    freq2 = [0] * 10
    while N > 0:
        freq1[N % 10] += 1
        N = N // 10
    while M > 0:
        freq2[M % 10] += 1
        M = M // 10
    for i in range(10):
        if freq1[i] > 0 and freq2[i] > 0:
            count += 1
    print(count)
    for i in range(10):
        if freq1[i] > 0 and freq2[i] > 0:
            print(i, end=', ')
    

if __name__ == '__main__':
    N = int(input("n = "))
    M = int(input("m = "))
    CommonDigits(N, M)