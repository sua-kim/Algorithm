#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

//int a[3][4];
//int main() {
//	int i, j, k = 1;
//	for (i = 0; i < 3; i++) {
//		for (j = 0; j < 4; j++) {
//			a[i][j] = k;
//			k++;
//		}
//	}
//	for (i = 0; i < 3; i++) {
//		for (j = 0; j < 4; j++) {
//			printf("%3d", a[i][j]);
//		}
//		printf("\n");
//	}
//	return 0;
//}


int a[6][6];
int main() {
	int i, j, k = 1;
	for (i = 0; i < 5; i++) {
		for (j = 4; j >= 0; j--) {
			a[i][j] = k;
			k++;
		}
	}
	for (i = 0; i < 5; i++) {
		for (j = 0; j < 5; j++) {
			printf("%3d", a[i][j]);
		}
		printf("\n");
	}
	return 0;
}
