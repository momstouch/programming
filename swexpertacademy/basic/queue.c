#include <stdio.h>
#include <stdlib.h>

#define Q_SIZE 10
int head, tail;

typedef struct item {
	int data;
} item;
item queue[Q_SIZE];

static inline int empty(void) {
	return head == tail;
}

static inline int size(void) {
	return tail - head;
}

static inline void push(int value) {
	if (tail < Q_SIZE)
		queue[tail++].data = value;
}

static inline item *pop(void) {
	if (!empty())
		return &queue[head++];
	return NULL;
}

int main(void) {

	for (int i = 0; i < 100; i += 3) {
		push(i);
	}
	while (!empty()) {
		printf("%d ", pop()->data);
	}
	printf("\n");

	return EXIT_SUCCESS;
}
