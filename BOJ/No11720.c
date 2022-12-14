#include <stdio.h>

int main(void)
{
	int n = 0;
	int sum = 0;

	scanf("%d", &n);
	char str[n];
	scanf("%s", &str[0]);
	for(int i = 0; i < n; i++)
	{
		sum += str[i] - '0';
	}
	printf("%d", sum);
	return (0);
}
