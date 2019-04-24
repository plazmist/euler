#include <stdlib.h>
#include <stdio.h>
#include <limits>

#define LEN 20

int isGoodStr(char *digits){
	for (int i = 0; i < LEN-2; ++i)
		if ( digits[i] + digits[i+1] + digits[i+2] -3*'0' > 9)
				return 0;
	return 1; // it is good
}

int isGoodInt(int *digits){
	for (int i = 0; i < LEN-2; ++i)
		if ( digits[i] + digits[i+1] + digits[i+2] > 9)
				return 0;
	return 1; // it is good
}

void Out(int *digits){
	for (int i = 0; i < LEN; ++i)
		printf("%d",digits[i] );
	printf("\n");	
}

//int next(char *digits, int nextPos)


int main(int argc, char const *argv[])
{	
	//char Str1[]="10000000000000000009";
/*	char Str1[]="00000000000000000000";
	if (isGoodStr(Str1)) printf("Good!\n");
	else  printf("NO!\n");*/

	int a[LEN]={0};
	long long MainCnt=0;
	for (a[0] = 1; a[0] <= 9 ; ++a[0])
	{
		a[1] = 0;
		while (a[0]+a[1] <= 9){
			a[2] = 0;
			while (a[0]+a[1]+a[2] <=9) {
				a[3] = 0;
				while (a[1]+a[2]+a[3] <=9) {
					a[4] = 0;
					while (a[2]+a[3]+a[4] <=9) {
						a[5] = 0;
						while (a[3]+a[4]+a[5] <=9) {
							a[6] = 0;
							while (a[4]+a[5]+a[6] <=9) {
								a[7] = 0;
								while (a[5]+a[6]+a[7] <=9) {
									a[8] = 0;
									while (a[6]+a[7]+a[8] <=9) {
										a[9] = 0;
										while (a[7]+a[8]+a[9] <=9) {
											a[10] = 0;
											while (a[8]+a[9]+a[10] <=9) {
												//Out(a);
												//MainCnt++;
												//if (isGoodInt(a)) intCnt++;
												
												a[11] = 0;
												while (a[9]+a[10]+a[11] <=9) {
													a[12] = 0;
													while (a[10]+a[11]+a[12] <=9) {
														a[13] = 0;
														while (a[11]+a[12]+a[13] <=9) {
															a[14] = 0;
															while (a[12]+a[13]+a[14] <=9) {
																a[15] = 0;
																while (a[13]+a[14]+a[15] <=9) {
																	a[16] = 0;
																	while (a[14]+a[15]+a[16] <=9) {
																		a[17] = 0;
																		while (a[15]+a[16]+a[17] <=9) {
																			a[18] = 0;
																			while (a[16]+a[17]+a[18] <=9) {
																				a[19] = 0;
																				while (a[17]+a[18]+a[19] <=9) {
																					//Out(a);
																					MainCnt++;
																					a[19]++;
																				}
																				a[18]++;
																			}
																			a[17]++;
																		}
																		a[16]++;
																	}
																	a[15]++;
																}
																a[14]++;
															}
															a[13]++;
														}
														a[12]++;
													}
													a[11]++;
												}
												//Out(a);
												a[10]++;
											}
											//Out(a);
											a[9]++;
										}
										//Out(a);
										a[8]++;
									}
									//Out(a);
									a[7]++;
								}
								Out(a);
								a[6]++;
							}

							a[5]++;
						}
						a[4]++;
					}
					a[3]++;
				}
				a[2]++;
			}
			Out(a);
			a[1]++;
		}
	}
	printf("MainCnt = %lld\n",MainCnt);

	return 0;
}
