#include <stdio.h>
#include <stdlib.h>

#define MAX_HEAP 100

typedef struct heap {
	int arr[MAX_HEAP];
	int size;
} heap;

void insert(heap *h, int value) {
	if (h->size >= MAX_HEAP) {
		fprintf(stderr, "out of MAX_HEAP(%d) range\n", MAX_HEAP);
		return;
	}

	int idx = ++h->size;

	while ( (idx != 1) && (value < h->arr[idx / 2]) ) {
		h->arr[idx] = h->arr[idx / 2];
		idx = idx / 2;
	}
	h->arr[idx] = value;
}

int pop(heap *h) {
	if (!h || h->size == 0) {
		fprintf(stderr, "empty heap!\n");
		return -1;
	}

	int parent = 1;
	int min = h->arr[1];
	h->arr[1] = h->arr[h->size--];

	while (1) {
		int child = parent * 2;
		int tmp;

		if (child + 1 <= h->size && h->arr[child] > h->arr[child + 1])
			child++;

		if (child > h->size || h->arr[parent] < h->arr[child])
			break;

		// swap
		tmp = h->arr[child];
		h->arr[child] = h->arr[parent];
		h->arr[parent] = tmp;

		parent = child;
	}

	return min;
}

int main(void) {
	heap h;
	h.size = 0;

	for (int i = 0; i < 30; i++)
		insert(&h, rand() % 100);

	while (h.size)
		fprintf(stdout, "%d ", pop(&h));
	fprintf(stdout, "\n");

	return EXIT_SUCCESS;
}
