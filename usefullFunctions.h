#include <stdio.h>

int isPrime(unsigned long someVal)
{
	if (someVal < 2) return 0;
	unsigned long newDiv=2;
	while (someVal % newDiv != 0)
		newDiv++;
	//if (newDiv == someVal) printf("Prime=%ld, ", someVal);
	if (newDiv == someVal) return 1; //yes, it is
	return 0; // no
}

int isPalindrom(unsigned long someVal)
{
	unsigned long tmp=someVal;
	int digits=0,cnt=0;
	char Digit[15];
	while (tmp > 0){ 
		Digit[digits]=tmp%10;
		digits++;
		tmp/=10;
	}
	while ( (cnt <= digits/2) && (Digit[cnt] == Digit[digits-cnt-1]))  cnt++;
	if (cnt >= digits/2) return 1; //yes, it is Palimdrom
		return 0; // NO!
}