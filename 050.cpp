//cc -O2 050.cpp -lprimesieve
#include <primesieve.h>
#include <stdio.h>

#define GRT 1000000

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

int main()
{
  primesieve_iterator it;
  primesieve_init(&it);
  uint64_t prime;

// count how many primes are below GRT
  int PrCnt = 0;
  while ((prime = primesieve_next_prime(&it)) < GRT)
    PrCnt++;
    //printf("%lu\n", prime);
  printf("Cnt = %d\n", PrCnt);

  int X,cnt,Sum,cntMax;
	for (int i = 0; i < PrCnt-21; ++i)
	{
		primesieve_free_iterator(&it);
		primesieve_init(&it);
		for (int pass=0; pass < i; ++pass)
			 primesieve_next_prime(&it);
		cnt = 1;
		Sum = primesieve_next_prime(&it);
		while (Sum < GRT) {
			Sum += primesieve_next_prime(&it);
			cnt++;
			if (isPrime(Sum)){
				if (cntMax < cnt) {cntMax = cnt; X = Sum; printf("Found %d from %d\n",Sum,cnt);}
			}
		}
	}


  return 0;
}