#include "stdio.h"
#include "stdlib.h"
#include "time.h"
#include <math.h>
#include <iostream>

int isChain(int Sum){
	//printf("%d -> ", Sum);
	int New=Sum, prev=0;
	while (1){
		Sum = 0;
		while (New > 0){
			Sum += (New%10)*(New%10);
			New /= 10;
		}
		
		//printf("%d -> ", Sum);
		if (Sum == 89) return 1;
		if (prev == Sum) return 0;
		New = Sum;
		prev = Sum;
	}
	return 0;
}

int main(int argc, char const *argv[])
{
	int x89=0;
	for (int i = 1; i < 10000000; ++i)
	{
		x89 += isChain(i);
		//printf("\n");
	}
	printf("x89 = %d\n",x89 );
	return 0;
}
