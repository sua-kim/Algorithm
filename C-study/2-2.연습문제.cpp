#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	// �� �� �� ���� ��
	/*int a, b;
	scanf("%d %d", &a, &b);
	if (a < b) printf("%d\n", a);
	else printf("%d\n", b);*/

	// ¦���ΰ�?
	/*int a;
	scanf("%d", &a);
	if (a % 2 == 0) printf("YES");
	else printf("NO");*/

	// Ȧ��, ¦��, ����
	/*int a;
	scanf("%d", &a);
	if (a == 0) printf("zero\n");
	else if (a % 2 == 0) printf("even\n");
	else printf("odd\n");*/

	// ���̱ⱸ Ű����
	/*int height;
	scanf("%d", &height);
	if (height >= 120 && height <= 150) printf("YES\n");
	else printf("NO\n");*/

	// �� �� �� �ּҰ�
	/*int A, B, C, min;
	scanf("%d %d %d", &A, &B, &C);
	if (A < B) min = A;
	else min = B;

	if (min < C) min = min;
	else min = C;

	printf("%d\n", min);*/

	// �ﰢ�� �Ǻ��ϱ�
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