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

	int i;

	if (N < 3)
		return 0;

	qsort(A, N, sizeof(A[0]), compare);

	for (i = 0; i < N - 2; i++) {
		long a = A[i];
		long b = A[i + 1];
		long c = A[i + 2];

		if (!(a + b > c)) {
			continue;
		}

		/* on sorted list, all we  have to is check below out.
		 * a + b > c, where a < b < c
		 */

		return 1;
	}

	return 0;
}

int main(void) {
	//int A[] = {10, 2, 5, 1, 8, 20};
	int A[] = {10, 50, 5, 1};

	printf("%d\n", solution(A, sizeof(A) / sizeof(A[0])));

	return EXIT_SUCCESS;
}
