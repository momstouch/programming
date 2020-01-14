#include <stdio.h>
#include <stdlib.h>

#include <string.h>
struct Results {
	int *C;
	int L;
};

struct Results solution(int N, int A[], int M) {
    struct Results result;
    // write your code in C99 (gcc 6.2.0)

	int max = 0;
	int i;
	int *cnt = (int *)malloc(sizeof(int) * N);
	int max_op = max;

	memset(cnt, 0x00, sizeof(int) * N);

	for (i = 0; i < M; i++) {
		int val = A[i];

		if (val == N + 1) {
			max_op = max;
		}
		else {
			int idx = val - 1;
			int count = cnt[idx];

			if (count < max_op)
				count = max_op;

			cnt[idx] = count + 1;

			if (max < cnt[idx])
				max = cnt[idx];
		}
	}

	for (i = 0; i < N; i++) {
		int val = cnt[i];

		if (val < max_op)
			cnt[i] = max_op;
	}

	result.C = cnt;
	result.L = N;

	return result;
}

int main(void) {
	int A[] = {3,4,4,6,1,4,4};
	int M = sizeof(A) / sizeof(int);
	int N = 5;
	int i;
	struct Results r = solution(N, A, M);

	for (i = 0; i < r.L; i++) {
		printf("%d ", r.C[i]);
	}
	putchar('\n');

	return EXIT_SUCCESS;
}
