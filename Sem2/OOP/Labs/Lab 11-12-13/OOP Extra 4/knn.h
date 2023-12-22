//
// Created by noiem on 5/31/2023.
//

#ifndef BONUS_4_KNN_H
#define BONUS_4_KNN_H

#pragma once
#include <vector>

using namespace std;

class KnnClassifier {
public:
    KnnClassifier(int k_ = 3, bool normalize_ = false);
    void fit(vector<vector<double>> & trainset, vector<int> & label);
    vector<int> test(vector<vector<double>> & testset);
private:
    int k;
    bool normalize;
    vector<vector<double>> data;
    vector<int> labels;
};

#endif //BONUS_4_KNN_H
