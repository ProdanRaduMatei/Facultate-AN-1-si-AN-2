#include <stdio.h>
#include <limits.h>
#include "tests.h"
#include <math.h>

// Write a function that takes as an input an array of integer numbers (both positive and negative numbers and returns the value of the triplet with the maximum product, as well as the elements that form this triplet (in increasing order).
// Use pass by pointer/address to return the elements that form that triplet.
// Think about the appropriate data type for the result. If the size of the array is less than 3, you should return the minimum
// representable value of the data type and the elements that form the triplet should be set to 0.
long long computeMaxTriplet(int arr[], unsigned int sz, int *t1, int* t2, int* t3){
    if (sz < 3)
    {
        t1 = 0;
        t2 = 0;
        t3 = 0;
    }
    long long max_prod = LONG_MIN;
    for (int i = 0; i < sz - 2; ++i)
        for (int j = i + 1; j < sz - 1; ++j)
            for (int k = j + 1; k < sz; ++k)
            {
                long long prod = arr[i] * arr[j] * arr[k];
                if (prod > max_prod)
                {
                    max_prod = prod;
                    *t1 = fmin(arr[i], fmin(arr[j], arr[k]));
                    *t3 = fmax(arr[i], fmax(arr[j], arr[k]));
                    if (*t1 == arr[i])
                    {
                        if (*t3 == arr[j])
                            *t2 = arr[k];
                        else
                            *t2 = arr[j];
                    }
                    else if (*t1 == arr[j])
                    {
                        if (*t3 == arr[i])
                            *t2 = arr[k];
                        else
                            *t2 = arr[i];
                    }
                    else if (*t1 == arr[k])
                    {
                        if (*t3 == arr[i])
                            *t2 = arr[j];
                        else
                            *t2 = arr[i];
                    }
                }
            }
    return max_prod;
}

int main()
{
#if ENABLE_TESTS > 0
    run_tests(true);
#endif
    
    return 0;
}
