/*Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
*/

#include <stdio.h>
#include <stdlib.h>

#define lng 500
#define pwr 1000

int main(int argc, char const *argv[])
{
	char res[lng], addition=0; // десятичное поцифровое представление числа
	// clearing array
	for (int i = 0; i < lng; ++i)
		res[i]=0;
	res[0]=1;
	//  step by step multiplication
	for (int p = 0; p < pwr; ++p)
		for (int i = 0; i < lng; ++i)
			{
				res[i]*=2;
				res[i]+=addition;
				addition=0;
				if (res[i] > 9)
				{
					res[i]-=10;
					addition=1;				
				}
			}	

	// for clear output
	printf("\n2^%d = ", pwr);
	int cnt=lng-1;
	while (res[cnt] == 0) cnt--;
	for (int i = cnt; i >=0; --i)
		printf("%d", res[i]);
	// counting digits summ
	int Sum=0;
	for (int i = 0; i < lng; ++i)
		Sum+=res[i];
	printf("\nsum = %d\n",Sum);
	printf("\nThe END\n");
	return 0;
}