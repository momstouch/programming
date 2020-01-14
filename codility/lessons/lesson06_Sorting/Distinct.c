#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
	int aa = *(int *)a;
	int bb = *(int *)b;

	if (aa < bb) {
		return -1;
	}
	else if (aa == bb) {
		return 0;
	}
	else {
		return 1;
	}
}

int solution(int A[], int N) {
    // write your code in C99 (gcc 6.2.0)

	int i, last;
	int cnt;

	if (N == 0)
		return 0;

	qsort(A, N, sizeof(A[0]), compare);

	last = A[0];
	cnt = 1;
	for (i = 1; i < N; i++) {
		if (last != A[i]) {
			cnt++;
			last = A[i];
		}
	}

	/* or we can use xor bit operation
	for (i = 1; i < N; i++) {
		if (A[i] ^ A[i - 1] != 0) {
			cnt++;
		}
	}
	*/

	return cnt;
}

int main(void) {
	int A[] = {2, 1, 1, 2, 3, 1};

	printf("%d\n", solution(A, sizeof(A) / sizeof(A[0])));

	return EXIT_SUCCESS;
}
