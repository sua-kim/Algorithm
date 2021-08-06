#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int main() {
	// 정수형 
	/*int a[5] = { 7, 3, 6, 12, 15 };
	printf("%d\n", a[3]);
	return 0;*/

	/*int eng[5] = { 80, 87, 97, 88, 99 };
	int i, sum = 0;
	for (i = 0; i < 5; i++) {
		sum += eng[i];
	}
	printf("%d\n", sum);
	return 0;*/

	/*int a[5] = { 12, 23, 15, 8, 3 };
	int i, cnt = 0;
	for (i = 0; i < 5; i++) {
		if (a[i] % 2 == 1) cnt++;
	}
	printf("%d\n", cnt);
	return 0;*/

	/*int a[7] = { 12, 23, 15, 8, 3, 9, 11 };
	int i, max = -2147000000;
	for (i = 0; i < 7; i++) {
		if (a[i] >= max) {
			max = a[i];
		}
	}
	printf("%d\n", max);
	return 0;*/


	// 문자열 처리
	/*char a[10] = "KOREA";
	printf("%s\n", a);
	return 0;*/

	/*char a[20];
	int n;
	scanf("%s", &a);
	n = strlen(a);
	printf("문자열 길이 = %d\n", n);
	return 0; */

	/*char a[20];
	int n, i, cnt = 0;
	printf("input string? ");
	scanf("%s", &a);
	n = strlen(a);
	for (i = 0; i < n; i++) {
		if (a[i] == 'e') cnt++;
	}
	printf("%d\n", cnt);
	return 0;*/

	char a[10] = "SEOUL";
	int i, j, n;
	n = strlen(a);
	for (i = 0; i < n; i++) {
		for (j = 0; j <= i; j++) {
			printf("%c", a[j]);
		}
		printf("\n");
	}
	return 0;
}
