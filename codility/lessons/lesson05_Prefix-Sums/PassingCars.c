#include <stdio.h>
#include <stdlib.h>

int solution_brute_force(int A[], int N) {
    // write your code in C99 (gcc 6.2.0)
	// occurs timeout error
	// time complexity is O(N**2)

	int i, j;
	int answer = 0;

	for (i = 0; i < N - 1; i++) {
		if (A[i] == 1)
			continue;

		for (j = i + 1; j < N; j++) {
			if (A[j] == 0)
				continue;

			answer++;
		}
	}

	return answer;
}

int solution(int A[], int N) {
    // write your code in C99 (gcc 6.2.0)
	// O(N) solution

	int n_ones = 0;
	int i;
	int answer = 0;

	// counting the number of ones
	for (i = 0; i < N; i++) {
		n_ones += A[i];
	}

	for (i = 0; i < N; i++) {
		if (!A[i]) {
			answer += n_ones;

			if (answer >= 1000000000)
				return -1;
		}
		else {
			n_ones--;
		}
	}

	return answer;
}

int main(void) {
	int A[] = {0,1,0,1,1};
	int N = sizeof(A) / sizeof(int);

	printf("%d\n", solution(A, N));

	return EXIT_SUCCESS;
}
