#include<stdio.h>
int main()
{
	int a,b,i=0;
	scanf("%d %d",&a,&b);
	while(a%b!=0)
	{
        i++;
        a++;
	}
	printf("%d\n",i);
}
