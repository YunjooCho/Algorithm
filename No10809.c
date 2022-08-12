#include <stdio.h>
#include <string.h>

#define RES_LEN 26

int main(void)
{
	int	 idx;
	char str[101];
	int res[RES_LEN];

	memset(res, -1, sizeof(int) * RES_LEN);
	scanf("%s", str);
	for (int i = 0; i < (int)strlen(str); i++)
	{
		idx = str[i] - 'a';
		if (res[idx] != -1)
		{
			continue;
		}
		else
		{
			res[idx] = i;
		}
	}
	for (int i = 0; i < 26; i++)
	{
		printf("%d ", res[i]);
	}
	return (0);
}
