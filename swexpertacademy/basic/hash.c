#include <stdio.h>
#include <stdlib.h>

#define MAX_TABLE 1024
#define MAX_NODES 2048

typedef struct _node {
	char key[20];
	int value;
	char del;
	struct _node *next;
} node;

node nodes[MAX_NODES];
int np;

node *table[MAX_TABLE];

int hash(char *str) {
	int h = 401;

	while (*str != '\0') {
		h = ((h << 4) + (int)(*str)) % MAX_TABLE;
		str++;
	}

	return h % MAX_TABLE;
}

void _strcpy(char *dst, const char *src) {
	while (*src != '\0') {
		*dst = *src;
		dst++;
		src++;
	}
}

int _strcmp(char *str1, char *str2) {
	while (*str1 && *str1 == *str2) {
		str1++;
		str2++;
	}

	return *str1 - *str2;
}

void add(char *key, int value) {
	if (np == MAX_NODES) {
		fprintf(stderr, "out of MAX_NODES(%d) range\n", MAX_NODES);
		return;
	}

	node *added = &nodes[np++];
	int h = hash(key);

	_strcpy(added->key, key);
	added->del = 0;
	added->next = NULL;
	added->value = value;

	if (table[h] == NULL)
		table[h] = added;
	else {
		node *cur = table[h];
		while (cur->next) {
			cur = cur->next;
		}
		cur->next = added;
	}
}

int search(char *key) {
	int h = hash(key);
	node *cur = table[h];

	while (cur) {
		if (_strcmp(cur->key, key) == 0 && cur->del == 0)
			return cur->value;
		cur = cur->next;
	}
	return 0;
}

void remove_key(char *key) {
	int h = hash(key);
	node *cur = table[h];

	while (cur) {
		if (_strcmp(cur->key, key) == 0) {
			cur->del = 1;
			return;
		}
	}
}

void debug_print(void) {
	for (int i = 0; i < MAX_TABLE; i++) {
		node *n = table[i];
		while (n) {
			if (n->del == 0)
				fprintf(stdout, "%d (%s): %d\n", i, n->key, n->value);
			n = n->next;
		}
	}
}

int main(void) {
	char str[20] = {'\0',};

	for (int i = 0; i < 10; i++) {
		for (int j = 0; j < 19; j++) {
			str[j] = rand() % 10 + 'a';
		}
		add(str, rand() % 100);

		fprintf(stdout, "%s: %d\n", str, search(str));

		if (i % 2 == 0) {
			remove_key(str);
		}

		for (int j = 0; j < 19; j++) {
			str[j] = '\0';
		}
	}

	debug_print();

	return EXIT_SUCCESS;
}
