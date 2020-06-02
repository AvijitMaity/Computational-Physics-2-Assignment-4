#include<stdio.h>
#include<stdlib.h>
#include<math.h>
int main()
{
double x,RANDOM[10000];
int i;
FILE *random;
random=fopen("Assignment 4 Problem 4.txt","w");   //creating a file
printf("the random numbers are :\n");  
for(i=0;i<10000;i++)
{

x=(double)rand()/(double)RAND_MAX;     //creating a uniform variate between 0 an 1

x=-0.5*log(x);                        //applying transformation method

RANDOM[i]=x;
printf("%f",RANDOM[i]);
fprintf(random,"%f\n",RANDOM[i]);
}

fclose(random);

}
