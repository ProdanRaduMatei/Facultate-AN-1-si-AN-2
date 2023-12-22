#pragma once
#include <string>
#include <istream>
#include <fstream>
#include <ostream>
enum class DisplayType {
	RECTANGULAR_FORM,
    POLAR_FORM,
};

class Complex {
    static DisplayType DISPLAY_TYPE;
    
public:
    Complex(); //done
    Complex(float r, float i); //done
    
    static void setDisplayType(DisplayType dt);
    static DisplayType getDisplayType();
    
    Complex add(const Complex& c); //done
    Complex substract(const Complex& c); //done
    Complex multiply(const Complex& c) const; //done
    void multiply(float c); //done
    bool equals(const Complex& c) const; //done
    
    Complex conjugate(); //done
    
    float phase() const; //done
    float magnitude() const; //done
    
    void setImag(float i); //done
    void setReal(float r); //done
    
    float getImag() const; //done
    float getReal() const; //done
    
    Complex operator+(const Complex& other); //done
    Complex operator-(const Complex& other); //done
    friend Complex operator*(const Complex& c1, const Complex& c2); //done
    
    void toPolar(float* r, float* theta) const; //done
    
    std::string toString() const;
    
    friend std::ostream& operator<<(std::ostream& is, const Complex& c1);
    friend std::istream& operator>>(std::istream& is, Complex& c);

private:
    float real;
    float imag;
};
