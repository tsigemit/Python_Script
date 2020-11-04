#include <stdio.h>
#if INT_MAX < 1000
printf("error type is too small");
#endif
char *returnString(char text[]){
return text;
}
int main(int argc, char *argv[]){
      char text[] ="This is to check";
      printf("%10s\n", returnString(text));
     int twoDArray[5][5];
     int *p=&twoDArray[0][0];

     for (int i = 0; i <3; i++){
     	for (int j = 0; j < 3; j++){
     		*p=5;
     		p++;
      	}
     }

     for (int i = 0; i <3; i++){
     	for (int j = 0; j <3; j++){
     		printf("%d", twoDArray[i][j]);
      	}
      	printf("\n");
     }

     printf("\n");
     printf("\n");
     int count = 0;
     for(int *q = &twoDArray[0][0]; q < &twoDArray[2][2]; q++){
     	count++;
     	printf("%d", *q);
     }
     printf("\n%d\n", count);
	return 0;
}