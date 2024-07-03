#include <iostream>
#include <vector>

// Extended Euclidean Algorithm to find modular inverse
int extendedGCD(int a, int m, int &x, int &y) {
    if (a == 0) {
        x = 0;
        y = 1;
        return m;
    }
    int x1, y1;
    int gcd = extendedGCD(m % a, a, x1, y1);
    x = y1 - (m / a) * x1;
    y = x1;
    return gcd;
}

// Function to find the modular inverse of 'a' modulo 'm'
int modInverse(int a, int m) {
    int x, y;
    int gcd = extendedGCD(a, m, x, y);
    // Modular inverse does not exist
    if (gcd != 1)
        return -1;
    return (x % m + m) % m;
}

// Function to solve a system of congruences using the Chinese Remainder Theorem
int solveCongruences(const std::vector<int> &a, const std::vector<int> &m) {
    int n = a.size();
    if (n != m.size()) {
        std::cerr << "Number of remainders must be equal to the number of moduli." << std::endl;
        return -1;
    }
    int M = 1; // Product of all moduli
    for (int i = 0; i < n; i++)
        M *= m[i];
    int x = 0;
    for (int i = 0; i < n; i++) {
        int Mi = M / m[i];
        int Mi_inverse = modInverse(Mi, m[i]);
        if (Mi_inverse == -1) {
            std::cerr << "Modular inverse does not exist." << std::endl;
            return -1;
        }
        x += a[i] * Mi * Mi_inverse;
    }
    // Reduce x modulo M to get the smallest non-negative solution
    x = (x % M + M) % M;
    return x;
}

int main() {
    std::vector<int> a = {2, 3, 4}; // x = 2 (mod 3), x = 3 (mod 5), x = 2 (mod 7)
    std::vector<int> m = {5, 7, 11};
    int solution = solveCongruences(a, m);
    if (solution != -1)
        std::cout << "The solution is: " << solution << std::endl;
    return 0;
}
