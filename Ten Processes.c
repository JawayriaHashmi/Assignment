#include<stdio.h>
#include<stdlib.h>
#include<sys/wait.h>
#include<string.h>

int main()
{
	int ar[1000];
	int j=0,cpid,sum=0,fd[10][2];
	char snum[10];

	for(int i=0;i<10;i++)
		pipe(fd[i]);
	
	for(int i=0;i<1000;i++)
		ar[i]=i;

	for(int i=0; i<10;i++)
	{
		cpid=fork();
		if(cpid==0)
		{
			sum=0;
			for(j=i*100;j<100*(i+1);j++)
			{
				sum = sum +ar[j];
			}
			sprintf(snum,"%d",sum); 
			write (fd[i][1],snum,strlen(snum)+1);
		}
		else
			exit(0);
	}
	sum=0;
	for(int i=0;i<10;i++)
		wait(NULL);
	for(int i=0;i<10;i++)
	{	
		read (fd[i][0], snum,10);
		sum+=atoi(snum); 
	}
	printf ("Sum= %i\n", sum);	
}

