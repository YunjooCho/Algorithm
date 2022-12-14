#include <stdio.h>

int get_gcd(int a, int b)
{
	int tmp = 0;
	while (a > b)
	{
		tmp = b;
		b = a % b;
		a = tmp;
		if (b == 0)
		{
			break;
		}
	}
	while (b > a)
	{
		tmp = a;
		a = b % a;
		b = tmp;
		if (a == 0)
		{
			break;
		}
	}
	return tmp;
}

int main(void)
{
	int a, b, tmp = 0;

	scanf("%d %d", &a, &b);
	if (a == 0 || b == 0)
	{
		printf("%d\n%d", 0, 0);
		return (0);
	}
	tmp = get_gcd(a, b);
	printf("%d\n", tmp);
	printf("%d\n", a * b / tmp);
	return (0);
}
