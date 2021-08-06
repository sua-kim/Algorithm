#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	// 정수형 변수
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
	printf("두수의 합 = %d\n", c);*/

	// 정수형 변수를 정수형 변수로 나누면 정수형태의 몫만 저장
	/*int a, b, c;
	a = 7;
	b = 2;
	c = a / b;
	printf("%d\n", c);*/

	// bit: -2^n ~ 2^n-1 (해당되지 않으면 회전)
	/*int a = 2147483648;
	printf("%d\n", a);*/


	// 실수형 변수
	//float a; // float의 경우 8자리 이상에선 오차 발생
	//a = 23.567;
	//printf("%f\n", a);

	//double b; // double을 사용하는 것이 더 유리
	// double 형은 lf!
	//b = 123456789;
	//printf("%lf\n", b);

	/*double a, b, c;
	a = 7, b = 2;
	c = (int)(a / b);
	printf("%f\n", c);*/

	// 실수형과 정수형이 같이 있을 경우 사칙연산 결과는 실수형으로 반환
	/*int a = 35, b = 3;
	float c;
	c = (float)(a / b);
	printf("%0.1f\n", c);*/

	// 문자형 변수
	/*char str;
	str = 'A';
	printf("%c\n", str);*/

	/*int a, b = 3;
	a = b + 2;
	a = a * 2;
	a = a - 3;
	a = a / 3;
	printf("%d\n", a);*/

	// 문자형 변수: 8bit(1byte)
	// 아스키코드: A~Z(65~90), a~z(97~122)
	// 문자형 변수를 %d 사용하면 아스키코드 출력
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
	printf("혼합 연산의 결과 = %d\n", k);*/

	//scanf()문
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

	// 나머지 연산자와 증감 연산자
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
