#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

// 1-1-1. 두수의 합
//int main() {
//	int A, B;
//	scanf("%d %d", &A, &B);
//	printf("%d + %d = %d", A, B, A + B);
//	return 0;
//}

// 1-1-2. 두 수의 곱
//int main() {
//	double A, B;
//	scanf("%lf %lf", &A, &B);
//	printf("%0.2lf", A * B);
//	return 0;
//}

// 1-1-3. 두 수의 몫과 나머지
//int main() {
//	int A, B;
//	scanf("%d %d", &A, &B);
//	printf("%d %d", A / B, A % B);
//	return 0;
//}

// 1-1-4. 음료수 자판기
//int main() {
//	int inputNum, price, charge, fiveHundred, oneHundred;
//	scanf("%d", &inputNum);
//	scanf("%d", &price);
//	charge = inputNum - price;
//	fiveHundred = charge / 500;
//	oneHundred = (charge % 500) / 100;
//	printf("%d\n", charge);
//	printf("%d\n", fiveHundred);
//	printf("%d\n", oneHundred);
//	return 0;
//}

// 1-1-5. 반올림 <X>
//int main() {
//	double a;
//	scanf("%lf", &a);
//	a = (int)(a * 10 + 0.5);
//	a = (double)a / 10;
//	printf("%lf", a);
//	return 0;
//}

// 1-1-6. 세 수의 평균
//int main() {
//	double A, B, C, average;
//	scanf("%lf %lf %lf", &A, &B, &C);
//	average = (A + B + C) / 3;
//	average = (int)(average * 100 + 0.5);
//	average = (double)average / 100;
//	printf("%lf", average);
//	return 0;
//}

// 1-1-7. 연필 개수
int main() {
	int a;
	double n;
	scanf("%d", &a);
	n = (double)a / 12;
	printf("%d\n", (int)ceil(n));
	return 0;
}
