#include <stdio.h>

int main(void)
{
	char n;

	scanf("%c", &n);
	if ((n >= 'A' && n <= 'Z') || (n >= 'a' && n <= 'z') || (n >= '0' && n <= '9'))
	{
		printf("%d", n);
	}
	return (0);
}