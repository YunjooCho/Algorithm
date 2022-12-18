#include <stdio.h>

int main(void)
{
    int a, b;

    scanf("%d %d", &a, &b);
    if (a > b)
    {
        if (a % b != 0)
        {
            printf("%d\n", a);
        }
    }
    return (0);
}