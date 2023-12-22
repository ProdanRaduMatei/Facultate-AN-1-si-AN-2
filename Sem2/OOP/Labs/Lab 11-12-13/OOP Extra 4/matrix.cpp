#include "matrix.h"

Matrix::Matrix() {
    rows = 0;
    cols = 0;
    m = NULL;
}

Matrix::Matrix(int r, int c, double num) { // default->zeros
    rows = r;
    cols = c;
    m = new double*[r];
    for(int i=0; i<r; i++){
        m[i] = new double[c];
    }
    for (int i = 0; i < r; i++) {
        for (int j = 0; j < c; j++) {
            m[i][j] = num;
        }
    }
}

Matrix::Matrix(double ** rhs, int r, int c) { // shallow copy
    rows = r;
    cols = c;
    m = rhs;
}

Matrix::Matrix(vector<vector<double>> & rhs) { // 2d vec -> matrix
    rows = rhs.size();
    cols = rhs[0].size();
    m = new double*[rows];
    for (int i = 0; i<rows; i++) {
        m[i] = new double[cols];
    }
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            m[i][j] = rhs[i][j];
        }
    }
}

Matrix::Matrix(const Matrix & rhs) { // copy constructor
    rows = rhs.getRows();
    cols = rhs.getCols();
    m = new double*[rows];
    for (int i = 0; i<rows; i++) {
        m[i] = new double[cols];
    }
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            m[i][j] = rhs[i][j];
        }
    }
}

//make vector (n,1) or (1,n) matrix
Matrix::Matrix(double * vec, int n, string type, bool remove_vec) {
    if (type == "column") {
        m = new double*[n];
        for (int i = 0; i < n; i++) {
            m[i] = new double[1];
        }
        for (int i = 0; i < n; i++) {
            m[i][0] = vec[i];
        }
        rows = n;
        cols = 1;
    }
    else {
        m = new double*[1];
        m[0] = new double[n];
        for (int i = 0; i < n; i++) {
            m[0][i] = vec[i];
        }
        rows = 1;
        cols = n;
    }
    if (remove_vec) {
        delete[] vec;
        vec = NULL;
    }
}

Matrix::~Matrix() {
    clearMatrix();
}

double* Matrix::return_row(int c)const { // returns cth row
    assert(c < rows);
    double * res = new double[cols];
    for (int i = 0; i < cols; i++) {
        res[i] = m[c][i];
    }
    return res;
}

Matrix Matrix::operator+(const Matrix & rhs) const { // sum two same sized matrices
    assert(rows == rhs.getRows() && cols == rhs.getCols());
    Matrix res(rows, cols);
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            res[i][j] = m[i][j] + rhs[i][j];
        }
    }
    return res;
}

Matrix Matrix::operator-(const Matrix & rhs) const { // subtract two same sized matrices
    assert(rows == rhs.getRows() && cols == rhs.getCols());
    Matrix res(rows, cols);
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            res[i][j] = m[i][j] - rhs[i][j] ;
        }
    }
    return res;
}

Matrix Matrix::operator*(const Matrix & rhs)const { // matrix multiplication mxn * nxk
    assert(cols == rhs.getRows());
    Matrix res(rows, rhs.getCols());
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < rhs.getCols(); j++) {
            for (int k = 0; k < cols; k++) {
                res[i][j] += m[i][k] * rhs[k][j];
            }
        }
    }
    return res;
}

const Matrix & Matrix::operator=(const Matrix & rhs) { // assignment operator
    if (!(rows == rhs.getRows() && cols == rhs.getCols())) {
        clearMatrix();
        rows = rhs.getRows();
        cols = rhs.getCols();
        m = new double*[rows];
        for (int i = 0; i<rows; i++) {
            m[i] = new double[cols];
        }
    }
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            m[i][j] = rhs[i][j];
        }
    }
    return *this;
}

Matrix Matrix::operator*(double rhs)const { // scale vector with a constant
    Matrix temp(*this);
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            temp[i][j] = m[i][j] * rhs;
        }
    }
    return temp;
}

Matrix Matrix::operator+(double rhs)const { // subtract a constant from each element of matrix
    Matrix temp(*this);
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            temp[i][j] = m[i][j] + rhs;
        }
    }
    return temp;
}

Matrix Matrix::operator-(double rhs)const { // subtract a constant from each element of matrix
    Matrix temp(*this);
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            temp[i][j] = m[i][j] - rhs;
        }
    }
    return temp;
}

Matrix Matrix::operator/(double rhs)const { // divide each element of matrix by a constant
    Matrix temp(*this);
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            temp[i][j] = m[i][j] / rhs;
        }
    }
    return temp;
}

bool Matrix::operator==(const Matrix & rhs)const { // checks if two matrices are same
    assert(rows == rhs.getRows() && cols == rhs.getCols());
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            if (m[i][j] != rhs[i][j]) {
                return false;
            }
        }
    }
    return true;
}

bool Matrix::operator!=(const Matrix & rhs)const { // checks if two matrices are different
    return !(*this == rhs);
}

void Matrix::clearMatrix() { // deallocates the dynamic memory
    if (!m) {
        return;
    }
    for (int i = 0; i < rows; i++) {
        delete[] m[i];
    }
    delete[] m;
    m = NULL;
    rows = 0;
    cols = 0;
}