#include <stdio.h>
#include <ctype.h>
#include <string.h>

void chg_upper(char *str);
void input_cnt(char *str, int len);

int main(void)
{
    int idx = 0;
    char str[1000001];
     
    scanf("%[^\n]s", str);
    const int LEN = strlen(str);
    chg_upper(str);
    input_cnt(str, LEN);
    return (0);
}

void chg_upper(char *str)
{
    int i = 0;
    while (str[i])
    {
        if (str[i] >= 97 && str[i] <= 122)
        {
            toupper(str[i]);
        }
        i++;
    }
}

void input_cnt(char *str, const int LEN)
{
    int i = 0;
    int j = ++i;
    int cnt = 1;
    int arr[LEN] = { 0, };

    memset(arr, 0, LEN * sizeof(char));
    printf("%s", arr);
    while (str[i])
    {
        j = i + 1;
        if (!arr[i])
        {
            arr[i] = 1;
        }
        while (str[j])
        {
            if (str[i] == str[j] && arr[j])
            {
                cnt++;
                arr[j] = cnt;
            }
            j++;
        }
        i++;
    }
}