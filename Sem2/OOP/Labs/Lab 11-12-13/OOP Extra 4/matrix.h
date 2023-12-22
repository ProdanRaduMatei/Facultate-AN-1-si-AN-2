//
// Created by noiem on 5/31/2023.
//

#ifndef BONUS_4_MATRIX_H
#define BONUS_4_MATRIX_H

#include <iostream>
#include <vector>
#include <fstream>
#include <cassert>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <array>
#include <climits>

using namespace std;

class Matrix {
private:
    double ** m;
    int rows;
    int cols;
    void clearMatrix();
public:
    // constructors
    Matrix();
    Matrix(int rows, int cols, double num=0);
    Matrix(double ** lhs, int r, int c);
    Matrix(const Matrix & lhs);
    Matrix(vector<vector<double>> & lhs);
    Matrix(double * vec, int n, string type = "column", bool remove_vec = true);

    // getters
    int getRows()const { return rows; };
    int getCols()const { return cols; };
    double* return_row(int i)const;

    // operators
    Matrix operator+(const Matrix & rhs)const;
    Matrix operator-(const Matrix & rhs)const;
    Matrix operator*(const Matrix & rhs)const;

    Matrix operator*(double rhs)const;
    Matrix operator+(double rhs)const;
    Matrix operator-(double rhs)const;
    Matrix operator/(double rhs)const;

    bool operator==(const Matrix & rhs)const;
    bool operator!=(const Matrix & rhs)const;

    const Matrix & operator=(const Matrix & rhs);
    double* operator[](int i)const { return m[i]; }

    ~Matrix(); //destructor
};


#endif //BONUS_4_MATRIX_H
