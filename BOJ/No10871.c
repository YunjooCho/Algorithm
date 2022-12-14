#include <stdio.h>

int main(void)
{
    int n;
    int x;
    int arr[10000];

    scanf("%d %d", &n, &x);
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &arr[i]);
        if (x > arr[i])
        {
            printf("%d ", arr[i]);
        }
    }
}