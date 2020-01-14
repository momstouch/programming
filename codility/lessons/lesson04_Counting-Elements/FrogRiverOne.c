#include <stdio.h>
#include <stdlib.h>

#include <string.h> // for memset
int solution(int X, int A[], int N) {
    // write your code in C99 (gcc 6.2.0)

	char *table = (char *)malloc(sizeof(char) * X);
	long x = X;
	long sum = (long)(x * (x + 1l)) / 2l;
	int i;

	memset(table, 0x00, sizeof(char) * X);

	for (i = 0; i < N; i++) {
		int val = A[i];
		if (!table[val - 1]) {
			table[val - 1] = (char)1;
			sum -= (long)val;

			if (sum == 0)
				return i;
		}
	}

	return -1;
}

int main(void) {
	int X = 5;
	int A[] = {1, 3, 1, 4, 2, 3, 5, 4};
	int N = sizeof(A) / sizeof(int);

	printf("the answer is %d\n", solution(X, A, N));

	return EXIT_SUCCESS;
}
