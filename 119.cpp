#include "stdio.h"
#include "stdlib.h"
#include "time.h"

int dgtSum(long n){
	int Sum = 0;
	while (n > 0){
		Sum += n % 10;
		n /= 10;
	}
	return Sum;
}

int main(){
	const clock_t begin_time = clock();
	int cnt = 1;
	int ss;
	long x = 50;
	long mul;
	while (cnt < 33) {
		x++;
		ss = dgtSum(x);
		if (ss != 1){
			mul = ss;
			while (mul < x) mul *= ss;
			if (mul == x) {
				printf("Found %d = %ld with %f \n", cnt, x, float( clock () - begin_time ) /  CLOCKS_PER_SEC);
				cnt++;
			}
		}
	}
}

