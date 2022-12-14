#include <stdio.h>
#include <string.h>

int main(void)
{
    int n, sum, cnt;
    char arr[100];

    scanf("%d", &n);
    for (int i = 0; i < n; i++)
    {
        sum = 0;
        cnt = 1;
        scanf("%s", arr);
        for (int j = 0; j < strlen(arr); j++)
        {
            if (arr[j] == 'O')
            {
                sum += cnt;
                cnt++;
            }
            else if (arr[j] == 'X')
            {
                cnt = 1;
            }
        }
        printf("%d\n", sum); 
    }  
    return (0);
}