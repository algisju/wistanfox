//Eratosthenes sieve for generating prime numbers
#include <stdio.h>
#include <malloc.h>
#include <stdlib.h>
#include <time.h>
#include <sys/time.h>
 
void sieve(int *a, int n)
{
    int i=0, j=0;
    for(i=2; i<=n; i++) {
        a[i] = 1;
    }
    for(i=2; i<=n; i++) {
        if(a[i] == 1) {
            for(j=i; (i*j)<=n; j++) {
                a[(i*j)] = 0;
            }
        }
    }
    printf("\nEratosthenes Sieve\n");
/*    printf("Primes numbers from 1 to %d are : ", n);
    for(i=2; i<=n; i++) {
        if(a[i] == 1)
            printf("%d, ", i);
    }
    */
    int ticks=clock(); 
    printf("\nTiming (Seconds):  %f ", (float)ticks/CLOCKS_PER_SEC);
    printf("\n\n");
}

int main(int argc, char **argv)
{
    int *array, n=atoi(argv[1]);
    array =(int *)malloc((n + 1) * sizeof(int));
    sieve(array,n);
    return 0;
}
