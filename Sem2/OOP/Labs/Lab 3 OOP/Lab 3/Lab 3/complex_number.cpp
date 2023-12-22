#include <math.h>
#include <stdio.h>
#include <cmath>

#include "complex_number.h"

Complex complex_create(float real, float image) {
    struct Complex c;
    c.real = real;
    c.image = image;
    return c;
}

float get_real(Complex c) {
    return c.real;
}

float get_imag(Complex c) {
    return c.image;
}

void set_real(Complex* c, float real) {
    c->real = real;
}

void set_imag(Complex* c, float image) {
    c->image = image;
}

Complex complex_conjugate(Complex c) {
    Complex conj;
    conj.real = c.real;
    conj.image = -c.image;
    return conj;
}

Complex complex_add(Complex c1, Complex c2) {
    Complex sum;
    sum.real = c1.real + c2.real;
    sum.image = c1.image + c2.image;
    return sum;
}

Complex complex_subtract(Complex c1, Complex c2) {
    Complex diff;
    diff.real = c1.real - c2.real;
    diff.image = c1.image - c2.image;
    return diff;
}

Complex complex_multiply(Complex c1, Complex c2) {
    Complex prod;
    prod.real = c1.real * c2.real - c1.image * c2.image;
    prod.image = c1.real * c2.image + c1.image * c2.real;
    return prod;
}

Complex complex_division(Complex c1, Complex c2) {
    Complex quot;
    float den = c2.real * c2.real + c2.image * c2.image;
    quot.real = (c1.real * c2.real + c1.image * c2.image) / den;
    quot.image = (c1.image * c2.real - c1.real * c2.image) / den;
    return quot;
}

void complex_scalar_mult(Complex* c, float s) {
    c->real *= s;
    c->image *= s;
}

bool complex_equals(Complex c1, Complex c2) {
    return c1.real == c2.real && c1.image == c2.image;
}

float complex_mag(Complex c) {
    return sqrt(c.real * c.real + c.image * c.image);
}

float complex_phase(Complex c) {
    return atan2(c.image, c.real);
}

void complex_to_polar(Complex c, float* r, float* theta) {
    *r = complex_mag(c);
    *theta = complex_phase(c);
    //set_real(*c, *r * cos(*theta));
    //set_image(*c, *r * sin(*theta));
}

void complex_display(Complex c) {
    printf("%f + %fi", c.real, c.image);
}
