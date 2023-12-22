#include "complex_number.h"
#include <sstream>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <math.h>

using namespace std;
#define M_PI  3.1415926535f 
 
Complex::Complex() : real{ 0.0f }, imag{ 0.0f }
{}

Complex::Complex(float r, float i) {
    real = r;
    imag = i;
}



Complex Complex::add(const Complex& c) {
    Complex sum;
    sum.real = c.real + real;
    sum.imag = c.imag + imag;
    return sum;
}

Complex Complex::substract(const Complex& c) {
    Complex diff;
    diff.real = c.real - real;
    diff.imag = c.imag - imag;
    return diff;
}

Complex Complex::multiply(const Complex& c) const{
    Complex prod;
    prod.real = c.real * real - c.imag * imag;
    prod.imag = c.real * imag + c.imag * real;
    return prod;
}

void Complex::multiply(float s) {
    real *= s;
    imag *= s;
}

bool Complex::equals(const Complex& c) const {
    return c.real == real && c.imag == imag;
}



Complex Complex::conjugate() {
    Complex c;
    c.real = real;
    c.imag = -imag;
    return c;
}



float Complex::phase() const {
    return atan2(imag, real);
}

float Complex::magnitude() const {
    return sqrt(real * real + imag * imag);
}



void Complex::setImag(float i) {
    imag = i;
}

void Complex::setReal(float r) {
    real = r;
}

float Complex::getImag() const {
    return this->imag;
}

float Complex::getReal() const{
    return this->real;
}



Complex Complex::operator+(const Complex &other) {
    return Complex(real + other.real, imag + other.imag);
}

Complex Complex::operator-(const Complex &other) {
    return Complex(real - other.real, imag - other.imag);
}

Complex operator*(const Complex& c1, const Complex& c2) {
    Complex prod;
    prod.real = c1.real * c2.real - c1.imag * c2.imag;
    prod.imag = c1.real * c2.imag + c1.imag * c2.real;
    return prod;
}



/*
 float complex_mag(Complex c) {
    return sqrt(c.real * c.real + c.imag * c.imag);
}

float complex_phase(Complex c) {
    return atan2(c.image, c.real);
}
*/

void Complex::toPolar(float* r, float* theta) const {
    *r = Complex::magnitude();
    *theta = Complex::phase();
}


/*
void complex_display(Complex c) {
    printf("%f + %fi", c.real, c.image);
}
*/
