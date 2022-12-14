#include <stdio.h>

int main(void)
{
    int n[8] = { 0 , };
    int cnt = 0;

    for (int i = 0; i < 8; i++)
    {
        scanf("%d", &n[i]);
    }

    for (int i = 0; i < 8; i++)
    {
        if (n[0] == 1 || n[0] == 8)
        {
            i++;
            cnt++;
            if ((n[0] == 1 && n[i] == n[i - 1] + 1) || (n[0] == 8 && n[i] == n[i-1] - 1))
            {
                cnt++;
            }
        }
        else
        {
            break;
        }
    }
    if (n[0] == 1 && cnt == 8)
    {
        printf("ascending");
    }
    else if(n[0] == 8 && cnt == 8)
    {
        printf("descending");
    }
    else
    {
        printf("mixed");
    }
    return (0);
}