#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	// 정사각형 출력
	/*int n, i, j;
	scanf("%d", &n);
	for (i = 1; i <= n; i++) {
		for (j = 1; j <= n; j++) {
			printf("*");
		}
		printf("\n");
	}*/


	// 삼각형 출력 1
	/*int n, i, j;
	scanf("%d", &n);
	for (i = n; i >= 1; i--) {
		for (j = 1; j <= i; j++) {
			printf("@");
		}
		printf("\n");
	}*/


	// 삼각형 출력 2
	/*int i, j, k, n;
	scanf("%d", &n);
	for (i = 1; i <= n; i++) {
		for (k = 1; k <= n - i; k++) {
			printf("0");
		}
		for (j = 1; j <= i; j++) {
			printf("@");
		}
		printf("\n");
	}*/
	/*int i, j, k, n;
	scanf("%d", &n);
	for (i = n; i >= 1; i--) {
		for (k = 1; k < i; k++) {
			printf("0");
		}
		for (j = 1; j <= n - i + 1; j++) {
			printf("@");
		}
		printf("\n");
	}*/


	// 삼각형 출력 3
	/*int i, j, k, n;
	scanf("%d", &n);
	for (i = (n + 1) / 2; i >= 1; i--) {
		for (k = i - 1; k >= 1; k--) {
			printf("0");
		}
		for (j = i; j <= (n + 1) / 2; j++) {
			printf("@");
		}
		printf("\n");
	}
	for (i = 1; i < (n + 1) / 2; i++) {
		for (k = 1; k <= i; k++) {
			printf("0");
		}
		for (j = (n + 1) / 2 - i; j >= 1; j--) {
			printf("@");
		}
		printf("\n");
	}*/


	// 주사위 합
	/*int k, i, j;
	scanf("%d", &k);
	for (i = 1; i <= 6; i++) {
		for (j = 1; j <= 6; j++) {
			if (i + j == k) printf("%d %d\n", i, j);
			}
	}*/


	// 두 자리 숫자 만들기 
	/*int i, j, n;
	scanf("%d", &n);
	for (i = 1; i <= n; i++) {
		for (j = 1; j <= n; j++) {
			if (i != j) printf("%d\n", 10 * i + j);
		}
	}*/


	// 특정 두 자리 수 만들기
	int i, j, c, cnt = 0;
	scanf("%d", &c);
	for (i = 1; i < 10; i++) {
		for (j = i + 1; j < 10; j++) {
			if (10 * j + i <= c) {
				printf("%d\n", 10 * j + i);
				cnt += 1;
			}
		}
	}
	printf("%d\n", cnt);

	return 0;
}