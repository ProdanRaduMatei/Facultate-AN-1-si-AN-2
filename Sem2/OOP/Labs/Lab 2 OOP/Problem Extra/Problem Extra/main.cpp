#include <iostream>
#include <cstring>

using namespace std;

char s[100001];
int freq[26], S;
float ChiFreq[26] = {8.2, 1.5, 2.8, 4.3, 12.7, 2.2, 2.0, 6.1, 7.0, 0.2, 0.8, 4.0, 2.4, 6.7, 7.5, 1.9, 0.1, 6.0, 6.3, 9.1, 2.8, 1.0, 2.4, 0.2, 2.0, 0.1};

void reading() {
    cin.get(s, 100001);
    S = strlen(s);
}

void determineFreq() {
    for (int i = 0; i < S; ++i) {
        if (s[i] >= 'A' && s[i] <= 'Z')
            freq[s[i] - '0' - 65]++;
        if (s[i] >= 'a' && s[i] <= 'z')
            freq[s[i] - '0' - 97]++;
    }
}

int Distance() {
    float dMin = 100000, s = 0;
    int d = 0, D = 0;
    while (d < 25) {
        s = 0;
        for (int i = 0; i <= 25; ++i) {
            int j = i + d;
            if (j > 25)
                j = j % 25 - 1;
            float dist =(float) ((freq[i] - ChiFreq[j]) * (freq[i] - ChiFreq[j])) / (ChiFreq[j] * ChiFreq[j]);
            s =(float) s + dist;
        }
        if (s < dMin) {
            dMin =(float) s;
            D = d;
        }
        ++d;
    }
    return D;
}

int main() {
    reading();
    determineFreq();
    cout << "The Chi Squared distance is " << Distance() << endl;
    return 0;
}
