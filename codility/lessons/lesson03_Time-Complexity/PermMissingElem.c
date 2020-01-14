#include <stdio.h>
#include <stdlib.h>

// you can write to stdout for debugging purposes, e.g.
// printf("this is a debug message\n");

int solution(int A[], int N) {
    // write your code in C99 (gcc 6.2.0)
	long n = N + 1;
	long ideal = (n * (n + 1l)) / 2l;
	long real;
	int i;

	for (real = 0, i = 0; i < N; i++) {
		real += (long)(A[i]);
	}

	return (int)(ideal - real);
}

int solution2(int A[], int N) {
    // write your code in C99 (gcc 6.2.0)
	long n = N + 1;
	long ideal = (n * (n + 1l)) / 2l;
	int i;

	for (i = 0; i < N; i++) {
		ideal -= (long)(A[i]);
	}

	return (int)(ideal);
}

int main(void) {
	int N = 100000;
	int A[100000];
	int i;

	for (i = 0; i < N; i++) {
		A[i] = i + 2;
	}

	printf("%d\n", solution2(A, N));

	return EXIT_SUCCESS;
}
