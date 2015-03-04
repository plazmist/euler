//What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

#include <stdio.h>
#include <stdlib.h>

#define count 20

int main(int argc, char const *argv[])
{
	int Grid[20][20],tmp,mul,Max=0;
	FILE *input;
	input=fopen("11.in.txt", "rt");
	if (input==NULL) { printf("file not found\n"); return 1;}
	for (int i = 0; i < count; ++i,printf("\n"))
		for (int j = 0; j < count; ++j)
		{
			fscanf(input, "%d", &Grid[i][j]);
			printf("%4d",Grid[i][j]);
		}
	//horizontal && vertical
	for (int i = 0; i < count; ++i)
		for (int j = 0; j < count-4; ++j)
		{
			mul=Grid[i][j]*Grid[i][j+1]*Grid[i][j+2]*Grid[i][j+3];
			if (mul > Max) Max=mul;
			mul=Grid[j][i]*Grid[j+1][i]*Grid[j+2][i]*Grid[j+3][i];
			if (mul > Max) Max=mul;
		}
	//diagonal
	for (int i = 0; i < count-4; ++i)
		for (int j = 0; j < count-4; ++j)
		{
			mul=Grid[i][j]*Grid[i+1][j+1]*Grid[i+2][j+2]*Grid[i+3][j+3];
			if (mul > Max) Max=mul;
		}
	for (int i = 3; i < count; ++i)
		for (int j = 0; j < count-4; ++j)
		{
			mul=Grid[i][j]*Grid[i-1][j+1]*Grid[i-2][j+2]*Grid[i-3][j+3];
			if (mul > Max) Max=mul;
		}	

	printf("Max = %d\n", Max);

	return 0;
}