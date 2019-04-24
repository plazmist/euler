#include <stdio.h>
#include <stdlib.h>
#include <math.h>

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

