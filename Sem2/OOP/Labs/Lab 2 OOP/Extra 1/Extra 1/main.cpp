#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>

std::vector<double> read_distribution(const std::string& filename) {
    std::vector<double> freq;
    std::ifstream file(filename);
    double line;
    while (file >> line) {
        freq.push_back(line);
    }
    file.close();
    return freq;
}

std::vector<double> compute_histogram(const std::string& text) {
    std::vector<int> histogram(26, 0);
    for (char c : text) {
        if (isalpha(c)) {
            int index = tolower(c) - 'a';
            histogram[index]++;
        }
    }
    int total = 0;
    for (int count : histogram) {
        total += count;
    }
    std::vector<double> freq(26, 0.0);
    for (int i = 0; i < 26; i++) {
        freq[i] = static_cast<double>(histogram[i]) / total;
    }
    return freq;
}

double chi_squared_distance(const std::vector<double>& histogram1, const std::vector<double>& histogram2) {
    double distance = 0.0;
    for (int i = 0; i < 26; i++) {
        double expected = histogram2[i];
        double observed = histogram1[i];
        double diff = observed - expected;
        distance += diff * diff / expected;
    }
    return distance;
}

std::pair<int, double> caesar_cipher_break(const std::string& text, const std::vector<double>& freq) {
    std::vector<std::pair<double, int>> distances;
    for (int shift = 0; shift < 26; shift++) {
        std::string shifted_text = "";
        for (char c : text) {
            if (isalpha(c)) {
                if (isupper(c)) {
                    shifted_text += static_cast<char>((c - 'A' + shift) % 26 + 'A');
                } else {
                    shifted_text += static_cast<char>((c - 'a' + shift) % 26 + 'a');
                }
            } else {
                shifted_text += c;
            }
        }
        std::vector<double> histogram = compute_histogram(shifted_text);
        double distance = chi_squared_distance(histogram, freq);
        distances.emplace_back(distance, shift);
    }
    std::sort(distances.begin(), distances.end());
    return std::make_pair(distances[0].second, distances[0].first);
}

std::string caesar_cipher_decrypt(const std::string& ciphertext, int shift) {
    std::string plaintext = "";
    for (char c : ciphertext) {
        if (isalpha(c)) {
            if (isupper(c)) {
                int shifted = (c - shift + 2 < 'A') ? c + 26 - shift + 2 : c - shift + 2;
                plaintext += static_cast<char>(shifted);
            } else {
                int shifted = (c - shift + 2 < 'a') ? c + 26 - shift + 2 : c - shift + 2;
                plaintext += static_cast<char>(shifted);
            }
        } else {
            plaintext += c;
        }
    }
    return plaintext;
}

void menu() {
    std::cout << "1. Decrypt a message" << std::endl;
    std::cout << "2. Quit" << std::endl;
    std::cout << "Enter your choice: ";
    std::string choice;
    std::cin >> choice;
    if (choice == "1") {
        std::string message;
        std::cout << "Enter the message: ";
        std::cin.ignore();
        std::getline(std::cin, message);
        std::vector<double> freq = read_distribution("distribution.txt");
        int shift;
        double distance;
        std::tie(shift, distance) = caesar_cipher_break(message, freq);
        std::string decrypted_message = caesar_cipher_decrypt(message, shift);
        std::cout << "Decrypted message: " << decrypted_message << std::endl;
        std::cout << "Shift: " << shift << std::endl;
        std::cout << "Distance: " << distance << std::endl;
    }
    else if (choice == "2") {
        std::cout << "Goodbye!" << std::endl;
    }
    else {
        std::cout << "Invalid choice. Please try again." << std::endl;
    }
}

int main() {
    menu();
    return 0;
}
