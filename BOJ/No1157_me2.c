#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    int  idx, len, max = -1, flag = 1; //flag : 1, 2(?를 출력)
    int  arr[26] = { 0, };
    char result;
    char str[1000001];   

    scanf("%[^\n]s", str);
    len = strlen(str);
    // if (len == 0)
    // {
    //     printf("?");
    //     return (0) ;
    // }
    for (int i = 0; i < len; i++)
    {
        str[i] = toupper(str[i]);
        idx = str[i] - 'A';
        arr[idx]++;
    }
    idx = -1; //다른 반복문에서 사용하기 위해 0으로 다시 초기화
    for (int j = 0; j < 26; j++)
    {
        if (arr[j] > max)
        {
            max = arr[j];
            idx = j;
        }
        else if (arr[j] != 0 && arr[j] == max && idx != j)
        {
            flag = 2;
            break;
        }
    }
    if (flag == 1 && len != 0)
    {
        printf("%c", idx + 'A');
    }
    else
    {
        printf("?");
    }
    return (0);
}