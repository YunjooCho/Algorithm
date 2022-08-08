#include <stdio.h>

int main(void)
{
	int n = 0;
	int max = 0;
	int min = 0;
	int arr[1000000];

	scanf("%d", &n);
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &arr[i]);
	}
	max = arr[0];
	min = arr[0];
	for (int i = 0; i < n; i++)
	{
		if (max < arr[i])
		{
			max = arr[i];
		}
		if (min > arr[i])
		{
			min = arr[i];
		}
	}
	printf("%d %d", min, max);
	return (0);
}
