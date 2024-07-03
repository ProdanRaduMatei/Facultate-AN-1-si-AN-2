//Implement 3 different algorithms for computing the greatest common divisor of 2 natural numbers.
// One of the algorithms should work for numbers of arbitrary size!
// Perform a comparative running-time analysis of these algorithms for a set of at least 10 inputs (use
// appropriate time units in order to differentiate the algorithms).

#include <iostream>
#include <string>
#include <chrono>

using namespace std;


//run time analysis
//gcd1: O(log n)
//gcd2: O(n)
//recgcd: O(log n)


long long gcd1(long long a, long long b) {
    if (a == 0 || b == 0)
        return 0;
    long long r;
    while (b != 0) {
        r = a % b;
        a = b;
        b = r;
    }
    return a;
}

long long gcd2(long long a, long long b) {
    if (a == 0 || b == 0)
        return 0;
    long long r;
    while (a != b) {
        if (a > b) {
            r = a - b;
            a = r;
        } else {
            r = b - a;
            b = r;
        }
    }
    return a;
}

long long recgcd(unsigned long long a, unsigned long long b) {
    if (b == 0)
        return a;
    else
        return recgcd(b, a % b);
}

std::string gcd3(const std::string& num1, const std::string& num2) {
    // Convert character strings to integers
    unsigned long long a = 0, b = 0;
    for (char digit : num1)
        a = a * 10 + (digit - '0');
    for (char digit : num2)
        b = b * 10 + (digit - '0');
    // Compute the GCD using the recursive Euclidean algorithm
    unsigned long long r = recgcd(a, b);
    // Convert the GCD back to a string
    std::string result = std::to_string(r);
    return result;
}

int test() {
    //10 test cases for each algorithm
    //gcd1
    auto start = chrono::steady_clock::now();
    cout << "gcd1" << endl;
    cout << "gcd1(10, 5) = " << gcd1(10, 5) << endl;
    cout << "gcd1(10, 3) = " << gcd1(10, 3) << endl;
    cout << "gcd1(10, 7) = " << gcd1(10, 7) << endl;
    cout << "gcd1(10, 9) = " << gcd1(10, 9) << endl;
    cout << "gcd1(10, 11) = " << gcd1(10, 11) << endl;
    cout << "gcd1(10, 13) = " << gcd1(10, 13) << endl;
    cout << "gcd1(10, 15) = " << gcd1(10, 15) << endl;
    cout << "gcd1(10, 17) = " << gcd1(10, 17) << endl;
    cout << "gcd1(10, 19) = " << gcd1(10, 19) << endl;
    cout << "gcd1(10, 21) = " << gcd1(10, 21) << endl;
    auto end = chrono::steady_clock::now();
    cout << "Elapsed time in nanoseconds : " << chrono::duration_cast<chrono::nanoseconds>(end - start).count() << " ns" << endl << endl;

    auto start1 = chrono::steady_clock::now();
    //gcd2
    cout << "gcd2" << endl;
    cout << "gcd2(10, 5) = " << gcd2(10, 5) << endl;
    cout << "gcd2(10, 3) = " << gcd2(10, 3) << endl;
    cout << "gcd2(10, 7) = " << gcd2(10, 7) << endl;
    cout << "gcd2(10, 9) = " << gcd2(10, 9) << endl;
    cout << "gcd2(10, 11) = " << gcd2(10, 11) << endl;
    cout << "gcd2(10, 13) = " << gcd2(10, 13) << endl;
    cout << "gcd2(10, 15) = " << gcd2(10, 15) << endl;
    cout << "gcd2(10, 17) = " << gcd2(10, 17) << endl;
    cout << "gcd2(10, 19) = " << gcd2(10, 19) << endl;
    cout << "gcd2(10, 21) = " << gcd2(10, 21) << endl;
    auto end1 = chrono::steady_clock::now();
    cout << "Elapsed time in nanoseconds : " << chrono::duration_cast<chrono::nanoseconds>(end1 - start1).count() << " ns" << endl << endl;

    auto start2 = chrono::steady_clock::now();
    //gcd3
    cout << "gcd3" << endl;
    cout << "gcd3(10, 5) = " << gcd3("10", "5") << endl;
    cout << "gcd3(10, 3) = " << gcd3("10", "3") << endl;
    cout << "gcd3(10, 7) = " << gcd3("10", "7") << endl;
    cout << "gcd3(10, 9) = " << gcd3("10", "9") << endl;
    cout << "gcd3(10, 11) = " << gcd3("10", "11") << endl;
    cout << "gcd3(10, 13) = " << gcd3("10", "13") << endl;
    cout << "gcd3(10, 15) = " << gcd3("10", "15") << endl;
    cout << "gcd3(10, 17) = " << gcd3("10", "17") << endl;
    cout << "gcd3(10, 19) = " << gcd3("10", "19") << endl;
    cout << "gcd3(10, 21) = " << gcd3("10", "21") << endl;
    auto end2 = chrono::steady_clock::now();
    cout << "Elapsed time in nanoseconds : " << chrono::duration_cast<chrono::nanoseconds>(end2 - start2).count() << " ns" << endl << endl;

    return 0;
}

int main() {
    cout << "Enter 1 if you want to test the algorithms or 2 if you want to enter your own numbers: ";
    int choice;
    cin >> choice;
    if (choice == 1) {
        test();
    }
    else {
        long long a = -1, b = -1;
        string c, d;
        while (a <= 0) {
            cout << "a = ";
            cin >> a;
        }
        while (b <= 0) {
            cout << "b = ";
            cin >> b;
        }
        cout << "Enter two large numbers:" << endl;
        cout << "c = ";
        cin >> c;
        cout << "d = ";
        cin >> d;
        cout << "gcd1 = " << gcd1(a, b) << endl;
        cout << "gcd2 = " << gcd2(a, b) << endl;
        cout << "gcd3 = " << gcd3(c, d) << endl;
    }
    return 0;
}
