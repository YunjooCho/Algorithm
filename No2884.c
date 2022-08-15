#include <stdio.h>

int main(void)
{
    int hours;
    int minutes;

    scanf("%d %d", &hours, &minutes);

    if (hours == 0)
    {
        hours = 24;
    }
    minutes = hours * 60 + minutes - 45;
    hours = minutes / 60;
    minutes = minutes % 60;
    if (hours == 24)
    {
        hours = 0;
    }

    printf("%d %d", hours, minutes);
    return (0);
}