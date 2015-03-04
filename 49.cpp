/*Problem 49
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
(i) each of the three terms are prime 
(ii) each of the 4-digit numbers are permutations of one another.
There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
What 12-digit number do you form by concatenating the three terms in this sequence?
*/

#include <stdio.h>
#include <stdlib.h>

#define digitsValue 4

int isPrime(int someVal)
{
	int newDiv=2;
	while (someVal % newDiv != 0)
		newDiv++;
	if (newDiv == someVal) return 1; //yes, it is
	return 0; // no
}

void Sort(int *Arr)
{
	int cnt=0,max,tmp;
	while (Arr[cnt]>0) cnt++;
	for (int i = 0; i < cnt-1; ++i)
	{
		max=i;
		for (int j = i+1; j < cnt; ++j)
			if (Arr[j] < Arr[max]) max=j;
		if (max != i) {tmp=Arr[max]; Arr[max]=Arr[i]; Arr[i]=tmp;}
	}
}

int Primes[30];
int diffsMaxRepeat,rptDiffVal;

int fillEnum(int Value)
{
	char digits[digitsValue];
	for (int i = 0; i < digitsValue; ++i)
	{
		digits[i]=Value%10;
		Value/=10;
	}
	int cnt=0,newVal,present;
	int enumAll[50]={0};
	//printf("\n");
	for (int i = 0; i < digitsValue; ++i)
		for (int j = 0; j < digitsValue; ++j)
			if (j!=i)
			for (int k = 0; k < digitsValue; ++k)
				if ((k!=j) && (k!=i))
				for (int p = 0; p < digitsValue; ++p)
					if ((p != k) && (p != j) && (p != i))
					{
						
						newVal=digits[i]*1000+digits[j]*100+digits[k]*10+digits[p];
						present=0;
						for (int ii = 0; ii < cnt; ++ii)
						{
							if (enumAll[ii] == newVal) { present=1; break;}
						}
						if (!present) enumAll[cnt++]=newVal;
						
					}
	Sort(enumAll);
	int primes=0;
	int i=0;
	while (enumAll[i] != 0) {
		if (isPrime(enumAll[i])) {
			Primes[primes]=enumAll[i]; 
			primes++;
		}
		i++;
	}
	for (int i = 0; i < primes-2; ++i)
		for (int j = i+1; j < primes-1; ++j)
			for (int k = j+1; k < primes; ++k)
			 {
			 	
			 	if ((Primes[i]>1000)&& ((Primes[k] - Primes[j]) == (Primes[j] - Primes[i])))
			 		printf("Here they are! : %d %d %d\n",Primes[i],Primes[j],Primes[k]);
			 } 
	return primes;
}

int main(int argc, char const *argv[])
{
	for (int i = 1001; i <= 9999; ++i)
	{
		fillEnum(i);
	}
	return 0;
}
