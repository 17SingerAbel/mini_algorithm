#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

#define USAGE "Usage: Please input one integer \n"

// The input is assumed to be a 32-bit signed integer. 
// return 0 when the reversed integer overflows.
// Example1: x = 123, return 321
// Example2: x = -123, return -321

int main(int argc, char *argv[]) {
    if(argc != 2) {
        fprintf(stderr,USAGE);
        exit(1);
    }

    int x = strtol(argv[1], NULL, 10);
    int sum = 0;
    do {
        if (sum  > INT_MAX / 10 || sum < INT_MIN / 10) { // can never compute the int over INT MAX
            return 0;
        }
        sum = sum * 10 + x % 10;
        printf("sum : %d\n", sum);
        x = x / 10;

    } while (x);
    
    return sum;
    
}