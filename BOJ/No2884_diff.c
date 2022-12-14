#include <stdio.h>

int main(void)
{
    int H, M;

    scanf("%d %d", &H, &M);
    if (M < 45) //M이 45보다 작은 경우에만 음수값이 출력되므로 처리해줌
    {
        H = ((H - 1) + 24) % 24;
    }
    M = ((M - 45) + 60) % 60;
    printf("%d %d", H, M);
    return (0);
}