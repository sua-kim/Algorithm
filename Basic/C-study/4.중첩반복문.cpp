#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	/*int i, j;
	for (i = 1; i <= 3; i++) {
		for (j = 1; j <= 3; j++) {
			printf("*");
		}
		printf("\n");
	}
	return 0;*/

	/*int i, j;
	for (i = 1; i <= 3; i++) {
		for (j = 1; j <= i; j++) {
			printf("*");
		}
		printf("\n");
	}
	return 0;*/

	int i, j, k;
	for (i = 1; i <= 3; i++) {
		for (k = i; k < 3; k++) {
			printf(" ");
		}
		for (j = 1; j <= i * 2 - 1; j++) {
			printf("*");
		}
		printf("\n");
	}
	return 0;
}
