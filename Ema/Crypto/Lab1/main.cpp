#include <iostream>
#include <string>
#include <chrono>

using namespace std;

std::string gcd3(const std::string& num1, const std::string& num2) {
    //Transform the strings into numbers
    unsigned long long a = 0, b = 0;
    for (char digit : num1)
        a = a * 10 + (digit - '0');
    for (char digit : num2)
        b = b * 10 + (digit - '0');
    // Euclid's algorithm
    if (a <= 0 || b <= 0)
        return "0";
    while (b != 0) {
        unsigned long long temp = b;
        b = a % b;
        a = temp;
    }
    //Transform the result into a string
    std::string result = std::to_string(a);
    return result;
}

long long gcd2(long long a, long long b) {
    if (a == 0 || b == 0)
        return 0;
    long long r;
    while (a != b) {
        if (a > b) {
            r = a - b;
            a = r;
        }
        else {
            r = b - a;
            b = r;
        }
    }
    return a;
}

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

int test() {
    //10 cases for each function
    //gcd1

    auto start = std::chrono::high_resolution_clock::now();
    cout << "gcd1" << endl;
    cout << "gcd1(20, 5) = " << gcd1(20, 5) << endl;
    cout << "gcd1(20, 3) = " << gcd1(20, 3) << endl;
    cout << "gcd1(20, 7) = " << gcd1(20, 7) << endl;
    cout << "gcd1(20, 19) = " << gcd1(20, 9) << endl;
    cout << "gcd1(20, 11) = " << gcd1(20, 11) << endl;
    cout << "gcd1(20, 13) = " << gcd1(20, 13) << endl;
    cout << "gcd1(20, 25) = " << gcd1(20, 25) << endl;
    cout << "gcd1(20, 47) = " << gcd1(20, 47) << endl;
    cout << "gcd1(20, 59) = " << gcd1(20, 59) << endl;
    cout << "gcd1(20, 21) = " << gcd1(20, 21) << endl;
    auto finish = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> elapsed = finish - start;
    cout << "Elapsed time in nanoseconds : " << chrono::duration_cast<chrono::nanoseconds>(finish - start).count() << " ns" << endl << endl;

    //gcd2
    auto start1 = std::chrono::high_resolution_clock::now();
    cout << "gcd2" << endl;
    cout << "gcd2(20, 15) = " << gcd2(20, 15) << endl;
    cout << "gcd2(20, 32) = " << gcd2(20, 32) << endl;
    cout << "gcd2(20, 70) = " << gcd2(20, 70) << endl;
    cout << "gcd2(20, 9) = " << gcd2(20, 9) << endl;
    cout << "gcd2(20, 11) = " << gcd2(20, 11) << endl;
    cout << "gcd2(20, 13) = " << gcd2(20, 13) << endl;
    cout << "gcd2(20, 5) = " << gcd2(20, 15) << endl;
    cout << "gcd2(20, 17) = " << gcd2(20, 17) << endl;
    cout << "gcd2(20, 19) = " << gcd2(20, 39) << endl;
    cout << "gcd2(20, 21) = " << gcd2(20, 41) << endl;
    auto finish1 = std::chrono::high_resolution_clock::now();
    cout << "Elapsed time in nanoseconds : " << chrono::duration_cast<chrono::nanoseconds>(finish1 - start1).count() << " ns" << endl << endl;

    //gcd3
    auto start2 = std::chrono::high_resolution_clock::now();
    cout << "gcd3" << endl;
    cout << "gcd3(20, 15) = " << gcd3("20", "15") << endl;
    cout << "gcd3(20, 3) = " << gcd3("20", "3") << endl;
    cout << "gcd3(20, 7) = " << gcd3("20", "7") << endl;
    cout << "gcd3(20, 9) = " << gcd3("20", "9") << endl;
    cout << "gcd3(20, 11) = " << gcd3("20", "11") << endl;
    cout << "gcd3(20, 13) = " << gcd3("20", "13") << endl;
    cout << "gcd3(20, 5) = " << gcd3("20", "5") << endl;
    cout << "gcd3(20, 17) = " << gcd3("20", "17") << endl;
    cout << "gcd3(20, 9) = " << gcd3("20", "9") << endl;
    cout << "gcd3(20, 11) = " << gcd3("20", "11") << endl;
    auto finish2 = std::chrono::high_resolution_clock::now();
    cout << "Elapsed time in nanoseconds : " << chrono::duration_cast<chrono::nanoseconds>(finish2 - start2).count() << " ns" << endl << endl;
    return 0;
}

int main() {
    int choice;
    test();
    return 0;
}
