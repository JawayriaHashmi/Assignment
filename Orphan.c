#include<stdio.h>
#include<sys/types.h>
#include <unistd.h>

int main()
{

	int cpid=fork();
	if(cpid==0)
	{
		sleep(5);
		printf ("I am child\n");
	}
	else if(cpid>0)
	{
		printf ("I am Parent\n");
	}
}
