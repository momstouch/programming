#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define LEN(x) ((int)(sizeof(x) / sizeof(*x)))

void swap(int *a, int *b) {
	int tmp = *a;
	*a = *b;
	*b = tmp;
}

void quick_sort(int *arr, int start, int end, int reverse) {
	if (start >= end)
		return;

	int pivot = start;
	int i = start + 1;
	int j = end;

	while (i <= j) {
		if (reverse == 0) {
			while (arr[i] <= arr[pivot] && i <= end)
				i++;
			while (arr[j] >= arr[pivot] && j > start)
				j--;
		}
		else {
			while (arr[i] >= arr[pivot] && i <= end)
				i++;
			while (arr[j] <= arr[pivot] && j > start)
				j--;
		}

		if (i > j)
			swap(&arr[pivot], &arr[j]);
		else
			swap(&arr[i], &arr[j]);
	}

	quick_sort(arr, start, j - 1, reverse);
	quick_sort(arr, j + 1, end, reverse);
}

int main(void) {
	int data[30];

	srand(time(NULL));

	for (int i = 0; i < LEN(data); i++) {
		data[i] = rand() % 100;
	}

	quick_sort(data, 0, LEN(data) - 1, 0);

	for (int i = 0; i < LEN(data); i++) {
		fprintf(stdout, "%d ", data[i]);
	}
	putchar('\n');

	return EXIT_SUCCESS;
}
