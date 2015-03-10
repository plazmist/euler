/*Perfect Square Collection
Problem 142
Find the smallest x + y + z with integers x > y > z > 0 such that x + y, x − y, x + z, x − z, y + z, y − z are all perfect squares.
*/


#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define count 100000

int perfectSquare(unsigned long n)
{
	if (n < 0)
        return 0;
  	int h = n & 0xF;  // h is the last hex "digit"
    if (h > 9)
        return 0;
  	if (h != 2 && h != 3 && h != 5 && h != 6 && h != 7 && h != 8)
    {
        int t = (int) floor( sqrt((double) n) + 0.5 );
        if  (t*t == n) return 1; // Oh, YES!
    }
	return 0; // definatley NO
}

int main(int argc, char const *argv[])
{
	FILE * f1;
	f1 = fopen("142.out","wt");
	int sqSum=0;
	unsigned long x,y,z;
	for (z = 1; z < count; ++z, printf("%lu\n",z))
		for (y = z+1; y < count; ++y)
			for (x = y+1; x < count; ++x){
				//sqSum = perfectSquare(x + y) + perfectSquare(x − y) + perfectSquare(x + z) + perfectSquare(x − z) + perfectSquare(y + z) + perfectSquare(y − z);
				sqSum = perfectSquare(x+y) + perfectSquare(x-y) + perfectSquare(x+z) + perfectSquare(x-z) + perfectSquare(y+z) + perfectSquare(y-z);
				if (sqSum == 6) {printf("Result = %lu + %lu + %lu = %lu\n", x,y,z,x+y+z);fprintf(f1,"Result = %lu + %lu + %lu = %lu\n", x,y,z,x+y+z);}
			}
	fclose(f1);
	return 0;
}