#include "stdio.h"
#include "stdlib.h"
#include "time.h"
#include <math.h>
#include <iostream>

#define N 10
//https://projecteuler.net/problem=81
int mat[N][N];
int loadMatrix();
int printMatrix();

int main(){
	loadMatrix();
	printMatrix();
	int curJ[N]={0};
	int J=N-1;
	curJ[J]=N-1;
	long Sum=0,maxSum=0;
	for (int k = 0; k < N*N; ++k)
	{
		if (J == 0) J = N-1;
		Sum = 0;
		for (int j = 0; j <= curJ[0] ; ++j) Sum += mat[0][curJ[0]];
		for (int i = 1; i < N; ++i)
			for (int j = curJ[i-1]; j <= curJ[i]; ++j)
			{
				Sum += mat[i][j];
			}
			
		if (Sum > maxSum) maxSum = Sum; 
		curJ[J]++;
		J--;
		printf("curJ={");
		for (int i = 0; i < N; ++i)
			printf("%d,",curJ[i]);
		printf("\n");

	}
	printf("[ FINAL ] SUM = %ld\n", maxSum);
}

int loadMatrix()
{
	int i;
	int j;
	FILE *file;
	file=fopen("p081_matrix.txt", "r");
	for(i = 0; i < N; i++)
		for(j = 0; j < N; j++)
	    	if (!fscanf(file, "%d,", &mat[i][j])) break;
	fclose(file);
}

int printMatrix()
{
	int i;
	int j;
	for(i = 0; i < N; i++){
		for(j = 0; j < N; j++)
	       	printf("%d,",mat[i][j]); 
	    printf("\n");
	}
}