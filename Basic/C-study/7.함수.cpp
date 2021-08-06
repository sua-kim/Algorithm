#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int add(int x) {
	int t;
	t = x + x;
	return t;
}

int sub(int x, int y) {
	int t;
	t = x - y;
	return t;
}

int abs(int x);

int main() {
	/*int a = 10, k;
	k = add(a);
	printf("%d\n", k);*/

	/*int a = 30, b = 20, k;
	k = sub(a, b);
	printf("%d\n", k);*/

	int a;
	a = -3;
	printf("%d\n", abs(a));

	return 0;
}

int abs(int x) {
	if (x < 0) return x * -1;
	else return x;
}
