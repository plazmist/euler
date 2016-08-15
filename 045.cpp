#include <stdio.h>
#include <stdlib.h>
#include <signal.h> 
#include <unistd.h>

volatile sig_atomic_t flag = 0;

void my_function(int sig){
  flag = 1; 
}

int main(){
  signal(SIGTSTP, my_function);  // Ctrl + Z
  unsigned long long int T,P,H;
  unsigned long long int Tn = 1, Pn = 1, Hn = 1;

	T = Tn *(  Tn + 1)/2;
	P = Pn *(3*Pn - 1)/2;
	H = Hn *(2*Hn - 1);

  while(1)  {
  	while (T < H) { 
			Tn++; 
			T = Tn *(Tn+1)/2; 
		}
	 while (P < H) { 
			Pn++; 
			P = Pn *(3*Pn - 1)/2; 
		}
	 if ((T == P) && (P == H)) 
		printf ("\nFound:  T-%llu = P-%llu = H-%llu = %llu\n\n",Tn,Pn,Hn,T);
	 Hn++; 
	 H = Hn *(2*Hn - 1); 
   if(flag){ 
        printf("T-%llu = %llu \nP-%llu = %llu \nH-%llu = %llu\n", Tn,T,Pn,P,Hn,H);
        flag = 0;
   }     
  }
  return 0;
}  