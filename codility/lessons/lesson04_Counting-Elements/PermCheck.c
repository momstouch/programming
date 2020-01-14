#include <stdio.h>
#include <stdlib.h>

int solution_wrong01(int A[], int N) {
    // write your code in C99 (gcc 6.2.0)

	long n = N;
	long ideal = (n * (n + 1l)) / 2l;
	long real;
	int i;

	for (real = 0l, i = 0; i < N; i++) {
		real += (long)(A[i]);
	}

	if (real == ideal)
		return 1;
	return 0;
}

int solution_wrong02(int A[], int N) {
    // write your code in C99 (gcc 6.2.0)

	long n = N;
	long ideal = (n * (n + 1l)) / 2l;
	long real;
	int i;

	for (real = 0l, i = 0; i < N; i++) {
		int idx = A[i] - 1;
		printf("idx: %d, real: %ld\n", idx, real);

		if (idx > -1 && idx < N) {
			real += (long)(A[idx]);
			A[i] = -1;
		}
		else
			return 0;
	}

	printf("%ld, %ld\n", real, ideal);
	if (real == ideal)
		return 1;
	return 0;
}

int compare(const void *a, const void *b) {
	int num1 = *(int *)a;
	int num2 = *(int *)b;

	if (num1 < num2)
		return -1;

	if (num1 > num2)
		return 1;

	return 0;
}

int solution(int A[], int N) {
    // write your code in C99 (gcc 6.2.0)
	//long n = N;
	//long ideal = (n * (n + 1l)) / 2l;
	int i;

	qsort(A, N, sizeof(int), compare);

	for (i = 0; i < N; i++) {
		if (i + 1 != A[i])
			return 0;
	}

	return 1;
}

int main(void) {
	//int A[] = {4, 1, 3, 2};
	int A[] = {1, 4, 1};
	int N = sizeof(A) / sizeof(int);

	printf("%d\n", solution(A, N));

	return EXIT_SUCCESS;
}
