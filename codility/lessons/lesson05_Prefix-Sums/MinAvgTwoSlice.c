#include <stdio.h>
#include <stdlib.h>

int solution_brute_force(int A[], int N) {
    // write your code in C99 (gcc 6.2.0)
	// timeout, 60%

	int i, j;
	float min = 10001.0;
	int answer;

	for (i = 0; i < N - 1; i++) {
		int sum = A[i];
		float mean;
		for (j = i + 1; j < N; j++) {
			sum += A[j];
			mean = (float)sum / (float)(j - i + 1);

			if (min > mean) {
				min = mean;
				answer = i;
			}
		}
	}

	return answer;
}

int solution(int A[], int N) {
    // write your code in C99 (gcc 6.2.0)
	// get 100%

	int i;
	float min = 10001.0;
	int answer;

	for (i = 0; i < N - 1; i++) {
		float mean = (float)(A[i] + A[i + 1]) / 2.0;

		if (i + 2 < N) {
			if (mean > (float) A[i + 2]) {
				mean = (mean * 2.0 + (float)A[i + 2]) / 3.0;
			}
		}

		if (mean < min) {
			min = mean;
			answer = i;
		}

	}

	return answer;
}

int main(void) {
	int A[] = {4, 2, 2, 5, 1, 5, 8};
	int N = sizeof(A) / sizeof(int);

	printf("%d\n", solution(A, N));

	return EXIT_SUCCESS;
}
