#include <stdio.h>
#include <stdlib.h>

int solution(int A, int B, int K) {
    // write your code in C99 (gcc 6.2.0)

	if (A) {
		return ((B / K) + 1) - (((A - 1) / K) + 1);
	}
	else {
		return (B / K) + 1;
	}
}

int main(void) {

	printf("%d\n", solution(6, 11, 2));
	printf("%d\n", solution(10, 10, 5));
	printf("%d\n", solution(10, 10, 7));
	printf("%d\n", solution(10, 10, 20));

	return EXIT_SUCCESS;
}
