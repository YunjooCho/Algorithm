#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    int  idx, len, max = -1;
    int  arr[26] = { 0, };
    char res = '?';
    char str[1000001];   

    scanf("%[^\n]s", str);
    len = strlen(str);
    if (len == 0)
    {
        printf("?");
        return (0) ;
    }
    for (int i = 0; i < len; i++)
    {
        str[i] = toupper(str[i]);
        idx = str[i] - 'A';
        arr[idx]++;
    }
    for (int j = 0; j < 26; j++)
    {
        if (arr[j] > max)
        {
            max = arr[j];
            res = j;
        }
        else if (arr[j] == max)
        {
            res = '?';
        }
    }
    if (res != '?')
    {
        printf("%c", res + 'A');
    }
    else
    {
        printf("%c", res);
    }
    return (0);
}