#pragma once
#include<string>
#include<iostream>


class BigInteger{

public:

    BigInteger();
    BigInteger(std::string D);
    BigInteger(const BigInteger& other);
    
    ~BigInteger();
    
    int compare(const BigInteger& N) const;
    
    BigInteger add(const BigInteger& N);
    BigInteger sub(const BigInteger& N);
    
    void PrependZeros(const BigInteger& N);
    void Negate(const BigInteger& N);
    
    
    friend BigInteger operator+(const BigInteger& a, const BigInteger& b);
    friend bool operator+=(const BigInteger& a, const BigInteger& b);
    friend BigInteger operator-(const BigInteger& a, const BigInteger& b);
    friend bool operator-=(const BigInteger& a, const BigInteger& b);
    
    friend bool operator==(const BigInteger& a, const BigInteger& b);
    friend bool operator<(const BigInteger& a, const BigInteger& b);
    friend bool operator<=(const BigInteger& a, const BigInteger& b);
    friend bool operator>(const BigInteger& a, const BigInteger& b);
    friend bool operator>=(const BigInteger& a, const BigInteger& b);

private:

    unsigned long digits[201];
    int sign;
    unsigned long Size;
    unsigned long nr;
    
};
