#include <stdio.h>

int main(void)
{
    int n = 0;
    int max = 0;
    double sum = 0;
    double arr[1000];
    
    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        scanf("%lf", &arr[i]);
    }
    max = arr[0];
    for (int i = 1; i < n; i++)
    {
        if (max < arr[i])
        {
            max = arr[i];
        }
    }
    for (int i = 0; i < n; i++)
    {
        arr[i] = arr[i] / max * 100.0;
        sum += arr[i];
    }
    printf("%f", sum / n);
}