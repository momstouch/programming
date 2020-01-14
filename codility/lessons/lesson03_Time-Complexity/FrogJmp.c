#include <stdio.h>
#include <stdlib.h>
// you can write to stdout for debugging purposes, e.g.
// printf("this is a debug message\n");

int solution(int X, int Y, int D) {
    // write your code in C99 (gcc 6.2.0)
    int mod = (Y - X) % D;

    if (mod == 0) {
        return (int)((Y - X) / D);
    }
    return (int)((Y - X) / D) + 1;
}

int main(void) {
	int X = 10;
	int Y = 85;
	int D = 30;

	printf("%d\n", solution(X, Y, D));

	return EXIT_SUCCESS;
}
