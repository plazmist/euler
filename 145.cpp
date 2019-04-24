#include <stdlib.h>
#include <stdio.h>
#include <limits>

int isRev(int n){
	if (n %10 == 0) return 0;
	int rn = 0, sum = n;
	while (n > 0) {rn = rn*10 + n%10; n/=10;}
	sum += rn;
	while (sum > 0) {if ((sum%10)%2 == 0) return 0; sum /= 10;}
	return 1;
}


int main(int argc, char const *argv[])
{	
	int cnt = 0;
	for (int i = 11; i < 1000000000; ++i)
		if (isRev(i)) cnt++;
	printf("Cnt = %d\n",cnt);
	return 0;
}
