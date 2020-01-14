#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
	int aa = *((int *)a);
	int bb = *((int *)b);

	if (aa > bb) {
		return 1;
	}
	else if (aa == bb) {
		return 0;
	}
	else
		return -1;
}

int solution(int A[], int N) {
    // write your code in C99 (gcc 6.2.0)

	int ans1, ans2;

	qsort(A, N, sizeof(A[0]), compare);

	ans1 = A[N - 1] * A[N - 2] * A[N - 3];
	ans2 = A[0] * A[1] * A[N - 1];

	/*
	 * There are only cases,
	 * 1. all elements in A are positive, then product top 3-element after sort
	 * 2. all elemetns in A are negative, then product top 3-element after sort
	 * 3. A consists of a combination of neg. and pos. numbers, then
	 *    we should check out whether ans1 is bigger than ans2 which may have
	 *    two negative value.
	 * 1 and 2 are covered by ans1
	 */

	return (ans1 > ans2 ? ans1 : ans2);
}

int main(void) {
	//int A[] = {-3, 1, 2, -2, 5, 6};
	int A[] = {-5, 5, -5, 4};

	printf("%d\n", solution(A, sizeof(A) / sizeof(A[0])));

	return EXIT_SUCCESS;
}
