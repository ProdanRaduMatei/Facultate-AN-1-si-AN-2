#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
using namespace std;

#include "complex_test.h"
#include "complex_number.h"

using namespace std;

int main(int argc, char** argv) {
	run_complex_tests(true);
    Complex c;
    c = complex_create(1, 2);
    cout << "Complex mag= " << complex_mag(c) << endl;
    cout << "Complex phase= " << complex_phase(c) << endl;
    float r, theta;
    complex_to_polar(c, &r, &theta);
    cout << "Complex to polar r= " << r << endl;
    cout << "Complex to polar theta= " << theta << endl;
    complex_scalar_mult(&c, 2);
    cout << "Complex scalar multiply= " << c.real << " + " << c.image << "i" << endl;
    Complex* c1 = new Complex();
    c1->real = 1;
    c1->image = 2;
    cout << "Complex mag with heap= " << complex_mag(*c1) << endl;
    cout << "Complex phase with heap= " << complex_phase(*c1) << endl;
    complex_to_polar(*c1, &r, &theta);
    cout << "Complex to polar r with heap= " << r << endl;
    cout << "Complex to polar theta with heap= " << theta << endl;
    complex_scalar_mult(c1, 2);
    cout << "Complex scalar multiply with heap= " << c1->real << " + " << c1->image << "i" << endl;
    cout << "Add complex numbers= " << complex_add(*c1, c).real << " + " << complex_add(*c1, c).image << "i" << endl;
    cout << "Multiply complex numbers= " << complex_multiply(*c1, c).real <<
    " + " << complex_multiply(*c1, c).image << endl;
    cout << "Subtract complex numbers= " << complex_subtract(*c1, c).real << " + " << complex_subtract(*c1, c).image << endl;
    cout << "Divide complex numbers= " << complex_division(*c1, c).real << " + " << complex_division(*c1, c).image << endl;
    delete c1;
	return 0;
}
