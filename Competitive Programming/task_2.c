#include<stdio.h>
#include<string.h>
int main()
{
	char a[10],b[10];
	int i,m,l1,l2,n1=0,n2=0;

	scanf("%s",&a);
	scanf("%s",&b);
	l1 = strlen(a);
	l2 = strlen(b);

	for(i=0;i<l1;i++)
	{
	    n1 = n1 + a[i];

	}
	for(i=0;i<l2;i++)
	{
	    n2 = n2 + b[i];
	}

	m = n2 - n1;
	printf("%c\n",m);
    return 0;
}
