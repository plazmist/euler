// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#include <stdio.h>
#include <stdlib.h>



int main(int argc, char const *argv[])
{
	int value=20, dividor=2;
	while (dividor<20) {
		value+=20;
		dividor=2;
		while (value%dividor == 0) dividor++;
	}
	printf("Value = %d\n", value);
	return 0;
}