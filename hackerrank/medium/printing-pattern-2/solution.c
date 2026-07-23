#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() 
{

    int n;
    scanf("%d", &n);
  	// Complete the code to print the pattern.
    int size=(2*n)-1;
    for(int i=0;i<size;i++){
        for(int j=0;j<size;j++){
           int top =i;
           int left=j;
           int right=size-j-1;
           int down=size-i-1;
           int min=top;
           if(left<min)
              min=left;
           if(right<min)
              min=right;
           if(down<min)
               min=down;
           printf("%d ",n-min);       
        }
        printf("\n");
    }
    return 0;
}
