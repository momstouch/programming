#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int solution(int A[], int N) {
	int i;
	long sum;
	long acc;
	long min = INT_MAX;

	for (sum = 0, i = 0; i < N; i++) {
		sum += (long)(A[i]);
	}

	for (acc = 0, i = 0; i < N - 1; i++) {
		long diff;

		acc += (long)(A[i]);
		sum -= (long)(A[i]);
		//printf("%ld - %ld\n", sum, acc);
		diff = sum - acc;
		if (diff < 0) {
			diff *= -1l;
		}

		if (diff < min) {
			min = diff;
		}
	}

	return (int)min;
}

int main(void) {
	int A[] = {3, 1, 2, 4, 3};

	printf("%d\n", solution(A, 5));

	return EXIT_SUCCESS;
}
