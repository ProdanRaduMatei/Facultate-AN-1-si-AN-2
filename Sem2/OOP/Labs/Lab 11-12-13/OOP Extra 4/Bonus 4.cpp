#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>
#include <cmath>
#include <sstream>
#include "matrix.h"
#include "knn.h"
#include "naiveBayes.h"

using namespace std;

class CSVReader {
public:
    std::vector<std::vector<std::string>> readCSV(const std::string& filename) {
        std::ifstream file(filename);
        std::vector<std::vector<std::string>> data;

        if (file.is_open()) {
            std::string line;
            while (std::getline(file, line)) {
                std::vector<std::string> row;
                std::stringstream ss(line);
                std::string cell;

                while (std::getline(ss, cell, ',')) {
                    row.push_back(cell);
                }
                data.push_back(row);
            }

            file.close();
        } else {
            std::cout << "Failed to open file: " << filename << std::endl;
        }

        return data;
    }
};


int main() {
    CSVReader reader;

    std::vector<std::vector<std::string>> data = reader.readCSV("\\Mac\\iCloud\\Facultate\\Sem2\\OOP\\Lab 11-12-13\\OOP Extra 4\\mnist_test.csv");
    // Prepare trainset and labels
    vector<vector<double>> trainset;
    vector<int> labels;

    // Convert data from string to double
    for (const auto& row : data) {
        std::vector<double> rowValues;
        for (const auto& value : row) {
            try {
                double val = std::stod(value);
                rowValues.push_back(val);
            } catch (const std::invalid_argument& e) {
                // Handle the invalid argument exception
                //std::cerr << "Invalid argument: " << e.what() << std::endl;
            }
        }
        trainset.push_back(rowValues);
        labels.push_back(static_cast<int>(rowValues.back()));  // Assuming the last column is the label
    }

        // Initialize and train the KnnClassifier
        KnnClassifier knnClassifier(5, true);  // k = 5, normalize = true
        knnClassifier.fit(trainset, labels);

        // Prepare testset
        vector<vector<double>> testset = {
                {0.1, 0.2, 0.3},
                {0.4, 0.5, 0.6},
                // Add more test samples as needed
        };

        // Perform classification using KnnClassifier
        vector<int> knnPredictions = knnClassifier.test(testset);

        // Initialize and train the NaiveBayes classifier
        Matrix train_X(trainset);  // Convert trainset to Matrix format
        Matrix train_Y(labels.size(), 1);
        for (int i = 0; i < labels.size(); i++) {
            train_Y[i][0] = labels[i];
        }

        NaiveBayes naiveBayes;
        naiveBayes.fit(train_X, train_Y);

        // Perform classification using NaiveBayes classifier
        Matrix test_X(testset);  // Convert testset to Matrix format
        Matrix naiveBayesPredictions = naiveBayes.predict(test_X);

        // Print the predictions
        cout << "KnnClassifier Predictions: ";
        for (int prediction: knnPredictions) {
            cout << prediction << " ";
        }
        cout << endl;

        cout << "NaiveBayes Predictions: ";
        for (int i = 0; i < naiveBayesPredictions.getRows(); i++) {
            cout << naiveBayesPredictions[i][0] << " ";
        }
        cout << endl;
        system("pause");

        return 0;
    }