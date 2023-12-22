#include <stdio.h>
#include <limits.h>
#include "tests.h"


// The strchr function is used to locate a character in a string. 
// More specifically, it returns a pointer to the first occurrence of the character in the string and NULL otherwise. 
// Write a function my_strchr, with the same parametersand return value as strchr.
const char* my_strchr(const char* s, char character){
    while (*s != '\0'){
        if (*s == character)
            return (char *) s;
        ++s;
    }
    return NULL;
}

int main()
{
#if ENABLE_TESTS > 0
    run_tests(true);
#endif

    return 0;
}
