#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	/*int a;
	a = 5;
	if (a > 0) {
		printf("양수입니다.");
	} else {
		printf("양수가 아닙니다.");
	};*/
	
	/*int a = 5, b = 3;
	if (a > b) {
		a = a + b;
	}
	else {
		a = a - b;
	}
	printf("%d\n", a);*/
	
	/*int a = 5, b = 5;
	if (a != b) {
		a = a + b;
	}
	printf("%d\n", a);*/

	/*int a = 3, b = 12, k;
	if (a > 0) {
		b++;
		k = a + b;
	}
	else {
		b--;
		k = a + b;
	}
	printf("%d\n", k);*/

	/*int a = 2, b = 7, t;
	if (a >= 1 && b <= 7) t = a + b;
	else t = a - b;
	printf("%d\n", t);*/

	/*int a = 3, b = 7, t;
	if (a > 2 || b > 3) t = a * b;
	else t = a / b;
	printf("%d\n", t);*/

	/*int eng;
	printf("input your english score: ");
	scanf("%d", &eng);
	if (eng >= 90) printf("excellent\n");
	else if (eng >= 80) printf("good\n");
	else if (eng >= 70) printf("just so so \n");
	else printf("you need effort\n");*/

	int eng = 90, k = 0;
	if (eng >= 90) k += 1;
	if (eng >= 80) k += 2;
	if (eng >= 70) k += 3;
	printf("%d\n", k);

	return 0;
}
