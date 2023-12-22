#include "BigInteger.h"

#include <cctype> // for isdigit
#include <iostream>
#include <iomanip>
using namespace std;

BigInteger::BigInteger() {
    sign = 1;
    Size = 0;
    nr = 0;
    for (int i = 0; i < 201; i++) {
        digits[i] = 0;
    }
}

BigInteger::BigInteger(string D) {
    sign = 1;
    Size = 0;
    nr = 0;
    for (int i = 0; i < 201; i++) {
        digits[i] = 0;
    }
    if (D[0] == '-') {
        sign = -1;
        D.erase(0, 1);
    }
    for (int i = 0; i < D.size(); i++) {
        if (isdigit(D[i])) {
            digits[Size] = D[i] - '0';
            Size++;
        }
    }
}

BigInteger::BigInteger(const BigInteger& other) {
    sign = other.sign;
    Size = other.Size;
    nr = other.nr;
    for (int i = 0; i < 201; i++) {
        digits[i] = other.digits[i];
    }
}

BigInteger::~BigInteger() {
    //delete[] digits;
}

int BigInteger::compare(const BigInteger& N) const {
    if (N.Size < Size)
        return 1;
    if (N.Size > Size)
        return -1;
    for (int i = 0; i != Size; ++i) {
        if (N.digits[i] > digits[i])
            return -1;
        if (N.digits[i] < digits[i])
            return 1;
    }
    return 0;
}
BigInteger BigInteger::sub(const BigInteger& N) {
    BigInteger result;
    result.Size = 0;
    result.sign = 1;
    if (sign == N.sign) {
        if (sign == 1) {
            if (compare(N) == 1) {
                result.sign = 1;
                int carry = 0;
                for (int i = 0; i != Size; i++) {
                    int sum = digits[i] - N.digits[i] - carry;
                    if (sum < 0) {
                        sum += 10;
                        carry = 1;
                    }
                    else {
                        carry = 0;
                    }
                    result.digits[result.Size] = sum;
                    result.Size++;
                }
            }
            else {
                result = sub(*this);
                result.sign = -1;
            }
        }
        else {
            if (compare(N) == 1) {
                result = sub(*this);
                result.sign = -1;
            }
            else {
                result = sub(N);
                result.sign = 1;
            }
        }
    }
    else {
        result = add(N);
    }
    return result;
}

BigInteger BigInteger::add(const BigInteger& N) {
    BigInteger result;
    result.Size = 0;
    result.sign = 1;
    if (sign == N.sign) {
        result.sign = sign;
        int carry = 0;
        for (int i = 0; i != Size || i != N.Size; i++) {
            int sum = digits[i] + N.digits[i] + carry;
            result.digits[result.Size] = sum % 10;
            result.Size++;
            carry = sum / 10;
        }
        if (carry != 0) {
            result.digits[result.Size] = carry;
            result.Size++;
        }
    }
    else {
        if (sign == 1) {
            result = sub(*this);
        }
        else {
            result = sub(N);
        }
    }
    return result;
}



void BigInteger::PrependZeros(const BigInteger& N) {
    for (int i = Size; i != N.Size; i++) {
        digits[i] = 0;
    }
    Size = N.Size;
}

void BigInteger::Negate(const BigInteger& N) {
    sign = -1;
    for (int i = 0; i != N.Size; i++) {
        digits[i] = N.digits[i];
    }
    Size = N.Size;
}

BigInteger operator+ (const BigInteger& N1, const BigInteger& N2) {
    BigInteger result;
    result = result.add(N1);
    result = result.add(N2);
    return result;
}

BigInteger operator+= (BigInteger& N1, const BigInteger& N2) {
    N1 = N1.add(N2);
    return N1;
}

BigInteger operator- (const BigInteger& N1, const BigInteger& N2) {
    BigInteger result;
    result = result.sub(N1);
    result = result.sub(N2);
    return result;
}

BigInteger operator-= (BigInteger& N1, const BigInteger& N2) {
    N1 = N1.sub(N2);
    return N1;
}

bool operator== (const BigInteger& N1, const BigInteger& N2) {
    if (N1.compare(N2) == 0) {
        return true;
    }
    else {
        return false;
    }
}

bool operator< (const BigInteger& N1, const BigInteger& N2) {
    if (N1.compare(N2) == -1) {
        return true;
    }
    else {
        return false;
    }
}

bool operator> (const BigInteger& N1, const BigInteger& N2) {
    if (N1.compare(N2) == 1) {
        return true;
    }
    else {
        return false;
    }
}

bool operator<= (const BigInteger& N1, const BigInteger& N2) {
    if (N1.compare(N2) == -1 || N1.compare(N2) == 0) {
        return true;
    }
    else {
        return false;
    }
}

bool operator>= (const BigInteger& N1, const BigInteger& N2) {
    if (N1.compare(N2) == 1 || N1.compare(N2) == 0) {
        return true;
    }
    else {
        return false;
    }
}
