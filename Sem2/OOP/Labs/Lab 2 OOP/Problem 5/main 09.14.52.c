#include <math.h>
#include <stdio.h>
#include <limits.h>
#include <stdlib.h>
#include <time.h>
#include "tests.h"

void generateAllCombinations(int** numbers, char** operators) {
    double result = 0;
    int cifra[9] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
    char operatii[4] = { '+', '-', '*', '/' };
    int linie = 0, coloana = 0;
    for (int k = 0; k <= 9; k++) {
        for (int l = 0; l <= 9; l++) {
            for (int m = 0; m <= 9; m++) {
                for (int n = 0; n <= 9; n++) {
                    for (int i = 0; i <= 3; i++) {
                        for (int j = 0; j <= 3; j++) {
                            for (int p = 0; p <= 3; p++) {
                                result = cifra[k];
                                if (operatii[i] == '+') {
                                    result += cifra[l];
                                }
                                else if (operatii[i] == '-') {
                                    result -= cifra[l];
                                }
                                else if (operatii[i] == '*') {
                                    result *= cifra[l];
                                }
                                else if (operatii[i] == '/') {
                                    result /= cifra[l];
                                }
                                if (operatii[j] == '+') {
                                    result += cifra[m];
                                }
                                else if (operatii[j] == '-') {
                                    result -= cifra[m];
                                }
                                else if (operatii[j] == '*') {
                                    result *= cifra[m];
                                }
                                else if (operatii[j] == '/') {
                                    result /= cifra[m];
                                }
                                if (operatii[p] == '+') {
                                    result += cifra[n];
                                }
                                else if (operatii[p] == '-') {
                                    result -= cifra[n];
                                }
                                else if (operatii[p] == '*') {
                                    result *= cifra[n];
                                }
                                else if (operatii[p] == '/') {
                                    result /= cifra[n];
                                }
                                if (result == 24) {
                                    numbers[linie][coloana] = cifra[k];
                                    coloana++;
                                    numbers[linie][coloana] = cifra[l];
                                    coloana++;
                                    numbers[linie][coloana] = cifra[m];
                                    coloana++;
                                    numbers[linie][coloana] = cifra[n];
                                    coloana = 0;
                                    operators[linie][coloana] = operatii[i];
                                    coloana++;
                                    operators[linie][coloana] = operatii[j];
                                    coloana++;
                                    operators[linie][coloana] = operatii[p];
                                    coloana = 0;
                                    linie++;
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

void print_menu() {
    int nrpick[7][4] = {
        {1, 1, 4, 6},
        {1, 1, 3, 8},
        {1, 2, 2, 6},
        {1, 2, 3, 4},
        {1, 1, 3, 9},
        {4, 4, 4, 6},
        {1, 8, 8, 8},
    };
    int result = 0;
    printf("Welcome to the 24 game!\n");
    printf("Use each of the 4 numbers shown below exactly once, combining them somehow with the basic mathematical operators (+, -, *, /) to yield the value of 24.\n");
    char answer = 'y';
    while(answer == 'y') {
        srand(time(NULL));
        int picking = rand() % 7;
        printf("The numbers to use are: %d %d %d %d\n", nrpick[picking][0], nrpick[picking][1], nrpick[picking][2], nrpick[picking][3]);
        printf("Enter the three operators to use: ");
        char operators[3];
        scanf("%c %c %c", &operators[0], &operators[1], &operators[2]);
        result += nrpick[picking][0];
        for (int i = 1; i < 4; i++) {
            if (operators[i - 1] == '+') {
                result += nrpick[picking][i];
                printf("%d + %d = %d\n", result - nrpick[picking][i], nrpick[picking][i], result);
            }
            else if (operators[i - 1] == '-') {
                result -= nrpick[picking][i];
                printf("%d - %d = %d\n", result + nrpick[picking][i], nrpick[picking][i], result);
            }
            else if (operators[i - 1] == '*') {
                result *= nrpick[picking][i];
                printf("%d * %d = %d\n", result / nrpick[picking][i], nrpick[picking][i], result);
            }
            else if (operators[i - 1] == '/') {
                result /= nrpick[picking][i];
                printf("%d / %d = %d\n", result * nrpick[picking][i], nrpick[picking][i], result);
            }
        }
        if (result == 24) {
            printf("Well done!\n");
        }
        else {
            printf("You lost! The result is not 24.\n");
        }
        result = 0;
        answer = 'n';
        printf("Do you want to play again? (y/n): ");
        getchar();
        scanf("%c", &answer);
        getchar();
    }
    printf("Thank you for playing!\n");
}

int main()
{

 #if ENABLE_TESTS > 0
    //run_tests(true);
 #endif
    int** numbers = (int**)malloc((3188 * 4) * sizeof(int*));
    char** operators = (char**)malloc((3188 * 3) * sizeof(char*));
    print_menu();
    free(numbers);
    free(operators);
    return 0;
}
