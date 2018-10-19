#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>

int arr[1000];

void* add(void *x)
{
	int sum=0,temp=(int)x;
	for(int i=temp;i<temp+100;i++)
		sum+=arr[i];
	return ((void*) sum);
}


int main()
{

	int status[10],sum=0;
	pthread_t threads[10];

	for(int i=0;i<1000;i++)
		arr[i]=i;

	for(int i=0;i<10;i++)
		pthread_create(&threads[i],NULL,add,(void*)(i*100));

	for(int i=0;i<10;i++)
		pthread_join (threads[i],(void**) &status[i]);

	for(int i=0;i<10;i++)
		sum+=status[i];
	
	printf ("Sum = %i\n",sum);
}
