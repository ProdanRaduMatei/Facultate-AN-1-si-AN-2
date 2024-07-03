#include <stdio.h>
#include <stdlib.h>

int SumaSir(int v[], int start, int end)
{
    if (start == end)
        return v[start];
    else
    {
        int mij = (start + end) / 2;
        int sumaSt = SumaSir(v, start, mij);
        int sumaDr = SumaSir(v, mij + 1, end);
        return sumaSt + sumaDr;
    }
}

int main()
{
    int n;
    printf("Nr. of elements of array.");
    scanf("%d", &n);

    int *v = (int *)malloc(n * sizeof(int));
    if (v == NULL)
    {
        printf("Memory error");
        return 1;
    }

    printf("Enter %d elements:\n", n);
    for (int i = 0; i < n; ++i)
        scanf("%d", &v[i]);

    int suma = SumaSir(v, 0, n - 1);
    printf("Sum of the elements: %d\n", suma);

    free(v);
    return 0;
}