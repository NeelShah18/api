//lab 4, Problem 1 solution by<Tu Jingyu> 
#include<stdio.h>
#define DIM 5
#define NDATA 6
int f(void);
void pr(int x[DIM][NDATA]);
void compare(int rows, int x[DIM][NDATA],int *ns,int *nl);

int main()
{
    int a[DIM][NDATA];
    int i,j;
    int ns,nl;
    int rows;
    printf("lab 4 Problem 1 solution by <Tu Jingyu>\n");
    for (i=0;i<=4;i++)
    {
        for(j=0;j<=5;j++)
        { 
            a[i][j]=f();
            
        }
    }
    printf("Array\n");
    pr(a);
    printf("enter index of row to compare with\n");
    scanf("%d",&rows);
    compare(rows,a,&ns,&nl);
    printf("nS=%3d, nL=%3d \n",ns,nl);
    return 0;
}
int f(void)
{
    static int val=19331;
    val=-val*353 % 41;
    return val;
}

void pr(int x[DIM][NDATA])
{
    int i,j;
    for (i=0;i<=4;i++)
    {
        for(j=0;j<=5;j++)
        {
            printf("        %d      ",x[i][j]);
        }
        printf("\n");
    }
}
void compare(int r, int x[DIM][NDATA],int *ns,int *nl)
{
    int i,j;
    int sum,isum;
    int small=0,large=0;
    sum=0;
    for(j=0;j<=5;j++)
    {
        sum+= x[r][j];
    }
     printf("Sum for row index = %d is %d\n",r,sum);

    for(i=0;i<DIM;i++)
    {
        isum = 0;
        if(i!=r)
        {
            for(j=0;j<=5;j++)
            {
                isum+= x[i][j];
            }   
            if(isum>sum)
            {
                large++;
            }
            else
            {
                small++;
            }
        }
        else
        {
        
        }
    }
    *ns = small;
    *nl = large;
}