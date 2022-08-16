#include <stdio.h>
#define ARR_LEN 10

int main(void)
{
	int  a, b, c, mul, idx;
	int  arr[ARR_LEN] = { 0, };

	scanf("%d %d %d", &a, &b, &c);
	mul = a * b * c;
	for (; mul > 0; mul /= 10)
	{
		idx = mul % 10;
		arr[idx]++;
	}
	for (int j = 0; j < ARR_LEN; j++)
	{
		printf("%i\n", arr[j]);
	}
	return (0);
}
