#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main() {
	// 1부터 N까지 출력하기
	//int n, i;
	//scanf("%d", &n);
	///*for (i = 1; i <= n; i++) {
	//	printf("%d ", i);
	//}*/
	//i = 1;
	//while (i <= n) {
	//	printf("%d ", i);
	//	i++;
	//}


	// 1부터 N까지 홀수 출력
	/*int n, i;
	scanf("%d", &n);
	// for (i = 1; i <= n; i+=2) {
	// 	printf("%d ", i);
	// }
	// for (i = 1; i <= n; i++) {
	// 	if (i % 2 == 1)
	// 		printf("%d ", i);
	// }
	i = 1;
	while (i <= n) {
		printf("%d ", i);
		i += 2;
	}*/


	// 1부터 N까지 합 출력
	/*int n, i = 1, sum = 0;
	scanf("%d", &n);
	// for (i = 1; i <= n; i++) {
	// 	sum += i;
	// }
	while (i <= n) {
		sum += i;
		i++;
	}
	printf("%d\n", sum);*/


	// 1부터 N까지 짝수의 개수
	/*int n, i, even = 0;
	scanf("%d", &n);
	for (i = 1; i <= n; i++) {
		if (i % 2 == 0)
			even += 1;
	}
	printf("%d\n", even);*/


	// N의 약수 출력
	/*int n, i;
	scanf("%d", &n);
	for (i = 1; i <= n; i++) {
		if (n % i == 0) {
			printf("%d ", i);
		}
	}*/


	// 소수 판별하기
	/*int n, i, cnt = 0;
	scanf("%d", &n);
	for (i = 1; i <= n; i++) {
		if (n % i == 0) {
			cnt++;
		}
	}
	if (cnt == 2) printf("YES\n");
	else printf("NO\n");

	for (i = 2; i < n; i++) {
		if (n % i == 0) {
			printf("NO\n");
			break;
		}
	}
	if (i == n) {
		printf("YES\n");
	}*/


	// 최대공약수
	/*int a, b, i, max, n = 0;
	scanf("%d %d", &a, &b);
	if (a >= b) max = a;
	else max = b;
	for (i = 1; i <= max; i++) {
		if (a % i == 0 && b % i == 0) n = i;
	}
	printf("%d\n", n);*/
	/*int a, b, i, min;
	scanf("%d %d", &a, &b);
	if (a < b) min = a;
	else min = b;
	for (i = min; i >= 1; i--) {
		if (a % i == 0 && b % i == 0) {
			printf("%d\n", i);
			break;
		}
	}*/


	// 구구단 출력하기
	/*int n, i;
	scanf("%d", &n);
	for (i = 1; i <= 9; i++) {
		printf("%d * %d = %d\n", n, i, n * i);
	}*/


	// 지수연산
	/*int a, b, i, max = 1;
	scanf("%d %d", &a, &b);
	for (i = 1; i <= b; i++) {
		max *= a;
	}
	printf("%d\n", max);*/


	// 최솟값 구하기
	/*int i, a, min = 2147000000;
	for (i = 1; i <= 7; i++) {
		scanf("%d", &a);
		if (min >= a)
			min = a;
		else continue;
	}
	printf("%d", min);*/
	

	// 홀수(정올 기출)
	/*int i, n, k, min = 2147000000, result = 0;
	for (i = 1; i <= 7; i++) {
		scanf("%d", &n);
		if (n % 2 != 0) {
			result += n;
			if (min >= n) min = n;
			else continue;
		}
	}
	printf("%d\n%d\n", result, min);*/
	

	// 동물의 수 구하기
	/*int rabbit, chicken, num, leg, i;
	scanf("%d", &num);
	scanf("%d", &leg);
	for (i = 0; i < num; i++) {
		rabbit = i;
		chicken = num - i;
		if (4 * rabbit + 2 * chicken == leg) break;
	}
	printf("%d %d", rabbit, chicken);*/
	

	// 10부제(정올 기출)
	/*int date, i, car, num = 0;
	scanf("%d", &date);
	for (i = 1; i <= 7; i++) {
		scanf("%d", &car);
		if (car % 10 == date) num += 1;
	}
	printf("%d\n", num);*/

	
	// 사과(정올 기출)
	int school, student, apple, i, cnt = 0;
	scanf("%d", &school);
	for (i = 1; i <= school; i++) {
		scanf("%d %d", &student, &apple);
		cnt += (apple % student);
	}
	printf("%d\n", cnt);

	return 0;
}
