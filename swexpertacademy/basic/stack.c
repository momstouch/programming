#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define STACK 10
int top;

typedef struct item {
	int data;
} item;
item stack[STACK];

static inline int empty(void) {
	return !top;
}

static inline int size(void) {
	return top;
}

static inline void push(int value) {
	if (top == STACK) {
		fprintf(stderr, "out of STACK(%d) range\n", STACK);
		return;
	}

	stack[top++].data = value;
}

static inline int pop(void) {
	if (empty()) {
		fprintf(stderr, "empty stack\n");
		return -1;
	}

	return stack[--top].data;
}

static inline int on_top(void) {
	if (empty()) {
		fprintf(stderr, "empty stack\n");
		return -1;
	}

	return stack[top - 1].data;
}

int main(void) {
	srand(time(NULL));

	for (int i = 0; i < 10; i++) {
		push(rand() % 100);
		fprintf(stdout, "%d ", on_top());
	}
	putchar('\n');

	while (!empty())
		fprintf(stdout, "%d ", pop());
	putchar('\n');

	return EXIT_SUCCESS;
}
