/*Double-base palindromes
Problem 36
Published on Friday, 31st January 2003, 08:00 pm; Solved by 52630
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)*/


#include <stdio.h>
#include <stdlib.h>

const int Value = 1000000;

int isPalindrom(int someVal)
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

int isPalindromBin(int someVal)
{
	int tmp=someVal;
	int digits=0,cnt=0;
	char Digit[50];
	while (tmp > 0){ 
		Digit[digits]=tmp%2;
		digits++;
		tmp/=2;
	}
	while ( (cnt <= digits/2) && (Digit[cnt] == Digit[digits-cnt-1]))  cnt++;
	if (cnt >= digits/2) return 1; //yes, it is Palimdrom
		return 0; // NO!
}

int main(int argc, char const *argv[])
{	
	unsigned int Sum=0;
	for (int i = 0; i < Value; ++i)
		if (isPalindrom(i) && isPalindromBin(i)) {printf("%d\n", i); Sum+=i;}
	printf("Sum = %u\n", Sum);
	return 0;
}