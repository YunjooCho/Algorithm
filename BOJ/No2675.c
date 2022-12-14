#include <stdio.h>
#include <string.h>

int main(void)
{
    int  cnt, n;
    char arr[21];

    scanf("%d", &cnt);                        
    for (int i = 0; i < cnt; i++)              //입력받을 횟수만큼 아래 중첩반복문이 실행
    {
        scanf("%d %s", &n, &arr);              //몇 번 문자를 반복하여 출력할지와 출력할 문자열을 받음
        for (int j = 0; j < strlen(arr); j++)  //문자배열의 인덱스를 하나씩 이동하면서 안에 있는 반복문을 통해 여려번 출력   
        {
            for (int k = 0; k < n; k++)
            {
                printf("%c", arr[j]);
            }
        }
        printf("\n");
    }
    return (0);
}