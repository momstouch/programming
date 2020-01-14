#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Results {
	int *A;
	int M;
};

struct Results solution_brute_force(char *S, int P[], int Q[], int M) {
    struct Results result;
    // write your code in C99 (gcc 6.2.0)
	// O(N*M)
	// occurs timeover error

	int imp['T' + 1]; // impact factors
	int i;

	int *A = (int *)malloc(sizeof(int) * M);

	imp['A'] = 1;
	imp['C'] = 2;
	imp['G'] = 3;
	imp['T'] = 4;

	for (i = 0; i < M; i++) {
		int p = P[i];
		int q = Q[i];
		char min = 'T' + 1;

		for (; p <= q; p++) {
			if (min > S[p]) {
				min = S[p];
			}
		}
		A[i] = imp[(int)min];
	}

	result.A = A;
	result.M = M;
	return result;
}

struct Results solution(char *S, int P[], int Q[], int M) {
	struct Results result;
    // write your code in C99 (gcc 6.2.0)

	struct _factors {
		int A;
		int C;
		int G;
		int T;
	};

	int imp['T' + 1]; // impact factors
	int i;

	int *A = (int *)malloc(sizeof(int) * M);
	int len = strlen(S);

	struct _factors *f = (struct _factors *)malloc(
			sizeof(struct _factors) * (len + 2)
			);
	memset(f, 0x00, sizeof(struct _factors) * (len + 2));


	imp['A'] = 1;
	imp['C'] = 2;
	imp['G'] = 3;
	imp['T'] = 4;

	for (i = 0; i < len + 1; i++) {
		char ch = S[i];

		f[i + 1].A = f[i].A;
		f[i + 1].C = f[i].C;
		f[i + 1].G = f[i].G;
		f[i + 1].T = f[i].T;

		switch (ch) {
			case 'A':
				f[i + 1].A += 1;
				break;
			case 'C':
				f[i + 1].C += 1;
				break;
			case 'G':
				f[i + 1].G += 1;
				break;
			case 'T':
				f[i + 1].T += 1;
				break;
		}
	}

	// test code
	//for (i = 0; i < len + 1; i++) {
	//	printf("%d %d %d %d\n", f[i].A, f[i].C, f[i].G, f[i].T);
	//}

	for (i = 0; i < M; i++) {
		int p = P[i];
		int q = Q[i];

		if (p == q) {
			A[i] = imp[(int)S[p]];
			continue;
		}
		q++;

		if (f[q].A != f[p].A) {
			A[i] = imp['A'];
			continue;
		}
		else if (f[q].C != f[p].C) {
			A[i] = imp['C'];
			continue;
		}
		else if (f[q].G != f[p].G) {
			A[i] = imp['G'];
			continue;
		}
		else if (f[q].T != f[p].T) {
			A[i] = imp['T'];
		}
	}

	free(f);

	result.A = A;
	result.M = M;
	return result;
}

int main(void) {
	char S[] = "CAGCCTA";
	int P[] = {2,5,0};
	int Q[] = {4,5,6};
	int M = sizeof(P) / sizeof(int);

	struct Results r = solution(S, P, Q, M);
	int i;

	printf("answer: ");
	for (i = 0; i < r.M; i++) {
		printf("%d ", r.A[i]);
	}
	putchar('\n');

	return EXIT_SUCCESS;
}
