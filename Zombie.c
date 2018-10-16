#include<stdio.h>
#include<sys/types.h>
#include <unistd.h>
#include<stdlib.h>

int main()
{

	int cpid=fork();
	if(cpid>0)
	{
		sleep(10);
	}
	else if(cpid==0)
	{
		exit(0);
	}
}
