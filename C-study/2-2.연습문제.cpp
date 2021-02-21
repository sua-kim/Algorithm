#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	// 두 수 중 작은 값
	/*int a, b;
	scanf("%d %d", &a, &b);
	if (a < b) printf("%d\n", a);
	else printf("%d\n", b);*/

	// 짝수인가?
	/*int a;
	scanf("%d", &a);
	if (a % 2 == 0) printf("YES");
	else printf("NO");*/

	// 홀수, 짝수, 제로
	/*int a;
	scanf("%d", &a);
	if (a == 0) printf("zero\n");
	else if (a % 2 == 0) printf("even\n");
	else printf("odd\n");*/

	// 놀이기구 키제한
	/*int height;
	scanf("%d", &height);
	if (height >= 120 && height <= 150) printf("YES\n");
	else printf("NO\n");*/

	// 세 수 중 최소값
	/*int A, B, C, min;
	scanf("%d %d %d", &A, &B, &C);
	if (A < B) min = A;
	else min = B;

	if (min < C) min = min;
	else min = C;

	printf("%d\n", min);*/

	// 삼각형 판별하기
	int A, B, C, max;
	scanf("%d %d %d", &A, &B, &C);
	if (A < B) max = B;
	else max = A;
	if (max < C) max = C;
	else max = max;
	if (A + B + C > max * 2) printf("YES\n");
	else printf("NO\n");

	return 0;
}