#include <stdio.h>
#define NUM_COUNT 10

int main(void)
{
    int arr[10];
    int count;
    int result = 0;

    for (int i = 0; i < NUM_COUNT; i++)
    {
        scanf("%d", &arr[i]);
        arr[i] = arr[i] % 42;
    }
    for (int i = 0; i < NUM_COUNT; i++)
    {
        count = 0;
        for (int j = i + 1; j < NUM_COUNT; j++)
        {
            if (arr[i] == arr[j])
            {
                count++;
                break;
            }
        }
        if (count == 0)
        {
            result++;
        }
    }
    printf("%d\n", result);  
    return (0);
}