#include "BigInteger.h"

#include <cctype> // for isdigit
#include <iostream>
#include <iomanip>
using namespace std;

BigInteger::BigInteger() {
    int* digits = {0};
}

BigInteger::BigInteger(std::string D) {
    Size = size(D);
    for (int i = 0; i <= size(D); ++i)
        digits[i] = D[i] - '0';
}



int BigInteger::compare(const BigInteger& N) const {
    if (N.Size < Size)
        return 1;
    if (N.Size > Size)
        return -1;
    for (int i = 0; i <= Size; ++i) {
        if (N.digits[i] > digits[i])
            return -1;
        if (N.digits[i] < digits[i])
            return 1;
    }
    return 0;
}



bool operator==(const BigInteger& a, const BigInteger& b) {
    if (a.Size != b.Size)
        return false;
    for (int i = 1; i <= a.Size; ++i)
        if (a.digits[i] != b.digits[i])
            return false;
    return true;
}

bool operator<(const BigInteger& a, const BigInteger& b) {
    if (a.Size >= b.Size)
        return false;
    return true;
}

bool operator<=(const BigInteger& a, const BigInteger& b) {
    if (a.Size > b.Size)
        return false;
    if (a.Size < b.Size)
        return true;
    for (int i = 1; i <= a.Size; ++i)
        if (a.digits[i] > b.digits[i])
            return false;
    return true;
}

bool operator>(const BigInteger& a, const BigInteger& b) {
    if (a.Size <= b.Size)
        return false;
    return true;
}

bool operator>=(const BigInteger& a, const BigInteger& b) {
    if (a.Size < b.Size)
        return false;
    if (a.Size > b.Size)
        return true;
    for (int i = 1; i <= a.Size; ++i)
        if (a.digits[i] < b.digits[i])
            return false;
    return true;
}
