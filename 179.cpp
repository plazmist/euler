#include "stdio.h"
#include "stdlib.h"
#include "time.h"

int dividors(int n){
	int cnt = 2;
	for (int i = 2; i <= n/2; ++i)
		if (n % i == 0) { cnt++;}
	return cnt;
}

int main(){
	const clock_t begin_time = clock();
	int d1 = 0;
	int d2 = 0;
	int cnt = 0;
	for (int i = 2; i < 10000000; ++i)
	{
		d1 = d2;
		d2 = dividors(i);
		if (d1 == d2) {
			cnt++;
			printf("%d and %d has %d dividors Elasped: %f \n", i-1,i, d2,float( clock () - begin_time ) /  CLOCKS_PER_SEC); 
		}
	}
	printf("all = %d\n", cnt);
	return 0;
}
