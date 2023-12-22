#include "Tests.h"
#include "Song.h"
#include <string>
#include <iostream>
#include <vector>
using namespace std;


int main_1() {
    if (testAll() == 0) {
        cout << "\n \n \n \n \n \n ";
        cout << "TESTS PASSED!" << endl;
        cout << "WOOHOOO, YOU'RE A DJ !!!" << endl;
        cout << "\n \n \n \n \n \n ";
        //system("pause");
    }
    else {
        cout << "\n \n \n \n \n \n ";
        cout << "SOME TESTS FAILED !!!!." << endl;
        cout << "Try again :(" << endl;
        cout << "\n \n \n \n \n \n ";
        //system("pause");
    }
    return 0;
}


#include <QApplication>
#include "mainwindow.h"

int main(int argc, char **argv)
{
    QApplication app(argc, argv);

    MainWindow window;
    window.show();

    return app.exec();
}

