#include <stdio.h>
#include <string.h>
int main() {
	char a[4];
	char b[4];
	char tmp;

	scanf("%s", a);
	scanf("%s", b);

	tmp = a[0];
	a[0] = a[2];
	a[2] = tmp;

	tmp = b[0];
	b[0] = b[2];
	b[2] = tmp;

	if (strcmp(a, b) > 0) { //atoi 대신 strcmp사용, 반환값이 양수면 a가 크고 음수면 b가 큼
		printf("%s", a);
	}
	else {
		printf("%s", b);
	}
}