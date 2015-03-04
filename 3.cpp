//The prime factors of 13195 are 5, 7, 13 and 29.
//What is the largest prime factor of the number 600851475143 ?

#include <stdio.h>
#include <stdlib.h>

const unsigned long Value = 600851475143;

int isPrime(unsigned long someVal)
{
	unsigned long newDiv=2;
	while (someVal % newDiv != 0)
		newDiv++;
	//if (newDiv == someVal) printf("Prime=%ld, ", someVal);
	if (newDiv == someVal) return 1; //yes, it is
	return 0; // no
}

int main()
{
	unsigned long dividor=3;
		
	//if (isPrime(dividor)) printf("%ld is prime\n",dividor);

	while (dividor<=Value) {
		dividor++;
		//printf("%ld\n", dividor);
		if (isPrime(dividor)) {
			//printf("is prime %ld\n", dividor);
			if (Value%dividor == 0) printf("\nWhat we need = %ld\n", dividor);
		}
	}
	return 0;
}