#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char a[4], b[4];
    char tmp; 
    int a_i, b_i, max;

    scanf("%s %s", a, b);
    tmp = a[0];
    a[0] = a[2];
    a[2] = tmp;

    tmp = b[0];
    b[0] = b[2];
    b[2] = tmp; 
    
    a_i = atoi(a);
    b_i = atoi(b);
    if (a_i > b_i)
    {
        max = a_i;
    }
    else
    {
        max = b_i;
    }
    printf("%d", max);
    return (0);
}