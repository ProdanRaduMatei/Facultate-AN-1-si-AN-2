//Miller-Rabin algorithm. It will work for numbers of arbitrary size.

#include <iostream>

using namespace std;

// This function calculates (a * b) % c taking into account that a * b might overflow
long long mulmod(long long a,long long b,long long c) { 
    long long x = 0, y = a % c;
    while (b > 0) { // we iterate over all the bits of b
        if (b % 2 == 1) // if the last bit of b is 1, then we add y to x
            x = (x + y) % c; // we keep the modulo operation every time we can
        y = (y * 2) % c; // we double y
        b /= 2; // we move one bit to the right
    }
    return x % c;
}

// This function calculates (a ^ b) % c
long long modulo(long long a, long long b, long long c) {
    long long x = 1, y = a;
    while (b > 0){ // we iterate over all the bits of b
        if (b % 2 == 1) // if the last bit of b is 1, then we multiply x by y
            x = mulmod(x, y, c); // we keep the modulo operation every time we can
        y = mulmod(y, y, c); // we square y
        b /= 2; // we move one bit to the right
    }
    return x % c;
}

// Miller-Rabin primality test, iteration signifies the accuracy of the test
bool Miller(long long p, int iteration) {
    if (p < 2)
        return false;
    if (p != 2 && p % 2 == 0)
        return false;
    long long s = p - 1; // s is the exponent
    while (s % 2 == 0)
        s /= 2; // we extract all the powers of 2
    for (int i = 0; i < iteration; i++) {
        long long a = rand() % (p - 1) + 1, temp = s; // we select a random number
        long long mod = modulo(a, temp, p); // and we test if a^s is equivalent to 1 modulo p
        while (temp != p - 1 && mod != 1 && mod != p - 1) { // we repeat the test until we discover a number different of 1 and p-1
            mod = mulmod(mod, mod, p); // we square the number
            temp *= 2; // we increase the exponent
        }
        if (mod != p - 1 && temp % 2 == 0) // if the number is different of p-1 and the exponent is even, then p is not prime
            return false;
    }
    return true;
}

int main() {
    int iteration = 5;
    long long num;
    cout << "Enter integer to test primality: ";
    cin >> num;
    if (Miller(num, iteration))
        cout << num << " is prime" << endl;
    else
        cout << num << " is not prime" << endl;
    return 0;
}