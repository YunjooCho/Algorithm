#include <stdio.h>

int gcd(int a, int b)
{
	if (b == 0)
		return a; //재귀함수 탈출
	else
		return gcd(b, a % b);
}

int main(void)
{
	int a, b, tmp;

	scanf("%d %d", &a, &b);
	if (a < b)
	{
		tmp = a;
		a = b;
		b = tmp;
	}

	printf("%d\n%d", gcd(a, b), (a * b) / gcd(a, b));
	return (0);
}
