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

	// 구구단 출력하기

	// 지수연산

	// 최솟값 구하기

	// 홀수(정올 기출)

	// 동물의 수 구하기

	// 10부제(정올 기출)

	// 사과(정올 기출)

	return 0;
}
