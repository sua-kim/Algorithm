#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	// ������ ����
	/*int a;
	a = 7;
	printf("%d\n", a);

	int b = 11, c = 23;
	printf("%d %d\n", b, c);*/

	/*int num;
	num = 3;
	printf("%d\n", num);*/

	/*int a = 3, b = 4, c;
	c = a + b;
	printf("�μ��� �� = %d\n", c);*/

	// ������ ������ ������ ������ ������ ���������� �� ����
	/*int a, b, c;
	a = 7;
	b = 2;
	c = a / b;
	printf("%d\n", c);*/

	// bit: -2^n ~ 2^n-1 (�ش���� ������ ȸ��)
	/*int a = 2147483648;
	printf("%d\n", a);*/


	// �Ǽ��� ����
	//float a; // float�� ��� 8�ڸ� �̻󿡼� ���� �߻�
	//a = 23.567;
	//printf("%f\n", a);

	//double b; // double�� ����ϴ� ���� �� ����
	// double ���� lf!
	//b = 123456789;
	//printf("%lf\n", b);

	/*double a, b, c;
	a = 7, b = 2;
	c = (int)(a / b);
	printf("%f\n", c);*/

	// �Ǽ����� �������� ���� ���� ��� ��Ģ���� ����� �Ǽ������� ��ȯ
	/*int a = 35, b = 3;
	float c;
	c = (float)(a / b);
	printf("%0.1f\n", c);*/

	// ������ ����
	/*char str;
	str = 'A';
	printf("%c\n", str);*/

	/*int a, b = 3;
	a = b + 2;
	a = a * 2;
	a = a - 3;
	a = a / 3;
	printf("%d\n", a);*/

	// ������ ����: 8bit(1byte)
	// �ƽ�Ű�ڵ�: A~Z(65~90), a~z(97~122)
	// ������ ������ %d ����ϸ� �ƽ�Ű�ڵ� ���
	/*char str;
	str = 'A';
	printf("%d\n", str);
	printf("%c\n", str);
	str = str + 1;
	printf("%d\n", str);
	printf("%c\n", str);*/

	/*int a, b, c, k;
	a = b = c = 3;
	k = a + 3 * b - 6 / c;
	printf("ȥ�� ������ ��� = %d\n", k);*/

	//scanf()��
	/*int a;
	scanf("%d", &a);
	printf("input value = %d\n", a);*/

	/*int a, b;
	scanf("%d %d", &a, &b);
	printf("input value = %d %d\n", a, b);*/

	/*float a;
	printf("input float number?: ");
	scanf("%f", &a);
	printf("input value = %.2f", a);*/

	// ������ �����ڿ� ���� ������
	/*int a = 17, b = 5, k;
	k = a % b;
	printf("%d\n", k);*/

	/*int a = 234, b = 46, k, m;
	k = a % 10;
	m = b % 10;
	printf("%d %d\n", k, m);*/
	
	/*int a, b, k, m;
	a = b = 2;
	a++;
	++b;
	printf("%d %d\n", a, b);*/

	/*int a, b, k, m;
	a = 3;
	b = 2;
	k = a--;
	m = ++b;
	printf("%d %d\n", k, m);*/

	return 0;
}
