# include <stdio.h>
int main()
{
    int max(int x,int y,int z);
    int a,b,c,result;
    scanf("%d,%d,%d",&a,&b,&c);
    result=max(a,b,c);
    printf("max=%d\n",result);
}

int max(int x,int y,int z)
{
    int temp;
    if (x>y)
        if (x>z) temp=x;
        else temp=z;
    else if (y>z) temp=y;
    else temp=z;
    return temp;
}
