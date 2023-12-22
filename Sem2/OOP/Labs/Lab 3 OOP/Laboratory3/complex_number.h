#pragma once
#include <stdbool.h>

struct Complex{
    float real;
    float image;
};

Complex complex_create(float real, float image);

float get_real(Complex c);
float get_imag(Complex c);

void set_real(Complex* c, float real);
void set_imag(Complex* c, float image);

Complex complex_conjugate(Complex c);
Complex complex_add(Complex c1, Complex c2);
Complex complex_subtract(Complex c1, Complex c2);
Complex complex_multiply(Complex c1, Complex c2);
Complex complex_division(Complex c1, Complex c2);
void complex_scalar_mult(Complex* c, float s);

bool complex_equals(Complex c1, Complex c2);

float complex_mag(Complex c);
float complex_phase(Complex c);
void complex_to_polar(Complex c, float* r, float* theta);

void complex_display(Complex c);
