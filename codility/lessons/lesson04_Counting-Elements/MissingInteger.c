#include <stdio.h>
#include <stdlib.h>

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

	int i;
	int min;

	qsort(A, N, sizeof(int), compare);

	min = 1;

	for (i = 0; i < N; i++) {
		if (A[i] <= 0) {
			;
		}
		else if (A[i] > min) {
			return min;
		}
		else {
			min = A[i] + 1;
		}
	}

	return min;
}

int main(void) {
	//int A[] = {1,3,6,4,1,2};
	int A[] = {2};
	int N = sizeof(A) / sizeof(int);

	printf("%d\n", solution(A, N));

	return EXIT_SUCCESS;
}
