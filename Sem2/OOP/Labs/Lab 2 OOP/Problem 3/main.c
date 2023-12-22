#include <stdio.h>
#include <limits.h>
#include <string.h>
#include "tests.h"

// Using the function that you wrote for problem 2, write a function that computesand returns an array with all the positions of the occurrences of a character in a string.
void find_all( const char * str, char character, int*  positions, unsigned int cap, unsigned int * l) {
    memset(positions, -1, cap * sizeof(int));
    int i = 0, j = 0;
    while (str[i] != '\0') {
        if (str[i] == character) {
            positions[j] = i;
            j++;
        }
        i++;
    }
    *l = j;
 }

int main()
{
#if  ENABLE_TESTS > 0
    run_tests(true);
#endif

    return 0;
}
