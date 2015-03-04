//Problem 13
//Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char const *argv[])
{
	FILE *IN;
	IN=fopen("13.in.txt","rt");
	if (!IN) {printf("Error opening file\n");return 0;}
	int Sum[100]={0};
	int toAdd[100]={0};
	int over=0,res=0;;
	char One[51];
	for (int i = 0; i < 100; ++i)
	{
		fscanf(IN,"%s",One);
		for (int j = 0; j < 50; ++j)
			toAdd[50+j]=One[j]-48;
		for (int j = 99; j >= 0; --j)
		{
			Sum[j]+=toAdd[j]+over;
			if (Sum[j]>9) {
				Sum[j]-=10;
				over=1;
			}
			else over=0;
		}
		for (int j = 0; j < 50; ++j)
			printf("%d",toAdd[50+j]);
		printf("\n");
	}
	fclose(IN);
	printf("The Grand Result is:\n");
	int cnt=0;
	while (Sum[cnt]==0) cnt++;
	for (int i = cnt; i < 100; ++i)
	{
		printf("%d",Sum[i]);
	}

	return 0;
}



