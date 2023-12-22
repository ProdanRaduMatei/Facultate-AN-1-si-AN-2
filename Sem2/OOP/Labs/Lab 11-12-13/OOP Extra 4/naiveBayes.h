//
// Created by calina on 5/31/2023.
//

#ifndef BONUS_4_NAIVEBAYES_H
#define BONUS_4_NAIVEBAYES_H

#include "matrix.h"

class NaiveBayes {
public:
    NaiveBayes() {};
    void fit(Matrix & train_X, Matrix & train_y);
    Matrix predict(Matrix & test_X);

private:
    double calculate_likelihood(double mean, double var, double x);
    double calculate_prior(double c);
    double classify(const Matrix & x);
    vector<vector<pair<double, double>>> parameters; // first is mean, second is variance
    Matrix X;
    Matrix y;
    Matrix classes;

};

#endif //BONUS_4_NAIVEBAYES_H
