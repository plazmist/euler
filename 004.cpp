//A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
//Find the largest palindrome made from the product of two 3-digit numbers.

#include <stdio.h>
#include <stdlib.h>

int isPalindrom(int someVal)
{
	int tmp=someVal,digits=0,cnt=0;
	char Digit[10];
	while (tmp > 0){ 
		Digit[digits]=tmp%10;
		digits++;
		tmp/=10;
	}
	while ( (cnt <= digits/2) && (Digit[cnt] == Digit[digits-cnt-1]))  cnt++;
	if (cnt >= digits/2) return 1; //yes, it is Palimdrom
		return 0; // NO!
}

int main()
{
	int res=0;
	for (int i = 999; i >= 100; --i)
		for (int j = 999; j >= 100; --j)
			if ((isPalindrom(i*j)) && (i*j > res)) res=i*j;
	printf("YES! %d\n", res);
	return 0;
}