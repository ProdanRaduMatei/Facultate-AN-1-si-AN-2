#include "Tests.h"
#include "Song.h"
#include <string>
#include <iostream>
#include <vector>
using namespace std;

int main() {
    if (testAll() == 0) {
        cout << "All tests passed!" << endl;
        system("pause");
    }
    else {
        cout << "Some tests failed." << endl;
        system("pause");
    }
    return 0;
}
