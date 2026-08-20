#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {
	
    int n,t,sum;
    scanf("%d", &n);
    //Complete the code to calculate the sum of the five digits on n.
    
    while(n>0)
    {
       t=n%10;
       sum=sum+t;
       n=n/10;
    }
    printf("%d",sum);
    return 0;
}
