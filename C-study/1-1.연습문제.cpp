#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <math.h>

// 1-1-1. �μ��� ��
//int main() {
//	int A, B;
//	scanf("%d %d", &A, &B);
//	printf("%d + %d = %d", A, B, A + B);
//	return 0;
//}

// 1-1-2. �� ���� ��
//int main() {
//	double A, B;
//	scanf("%lf %lf", &A, &B);
//	printf("%0.2lf", A * B);
//	return 0;
//}

// 1-1-3. �� ���� ��� ������
//int main() {
//	int A, B;
//	scanf("%d %d", &A, &B);
//	printf("%d %d", A / B, A % B);
//	return 0;
//}

// 1-1-4. ����� ���Ǳ�
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

// 1-1-5. �ݿø� <X>
//int main() {
//	double a;
//	scanf("%lf", &a);
//	a = (int)(a * 10 + 0.5);
//	a = (double)a / 10;
//	printf("%lf", a);
//	return 0;
//}

// 1-1-6. �� ���� ���
//int main() {
//	double A, B, C, average;
//	scanf("%lf %lf %lf", &A, &B, &C);
//	average = (A + B + C) / 3;
//	average = (int)(average * 100 + 0.5);
//	average = (double)average / 100;
//	printf("%lf", average);
//	return 0;
//}

// 1-1-7. ���� ����
int main() {
	int a;
	double n;
	scanf("%d", &a);
	n = (double)a / 12;
	printf("%d\n", (int)ceil(n));
	return 0;
}