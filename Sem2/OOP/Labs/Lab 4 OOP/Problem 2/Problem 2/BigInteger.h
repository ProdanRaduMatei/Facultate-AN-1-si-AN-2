#pragma once
#include<string>
#include<iostream>


class BigInteger{

public:

    BigInteger();
    BigInteger(std::string D);
    
    int compare(const BigInteger& N) const;
    
    friend bool operator==(const BigInteger& a, const BigInteger& b);
    friend bool operator<(const BigInteger& a, const BigInteger& b);
    friend bool operator<=(const BigInteger& a, const BigInteger& b);
    friend bool operator>(const BigInteger& a, const BigInteger& b);
    friend bool operator>=(const BigInteger& a, const BigInteger& b);

private:

    unsigned long digits[201];
    int sign;
    unsigned long Size;
    
};
