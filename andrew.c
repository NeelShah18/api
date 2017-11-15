#include <stdio.h>
#define NDATA 6
#define DIM 5
int f(void);
void pr(int x[DIM][NDATA]);
void compare(int row, int x[DIM][NDATA],int *nSmaller,int *nLarger);

int main()
{
    int a[DIM][NDATA];
    int i,j;
    int nS,nL;
    int row;
    printf("lab 4 Problem 1 solution by <Xiaoyi Xia>\n");
    for (j=0;j<NDATA;j++)
    {
        for(i=0;i<DIM;i++)
        { 
            a[i][j]=f();
        }
    }
    printf("Data array is\n");
    pr(a);
    printf("enter index of row to compare with\n");
    scanf("%d",&row);
    compare(row,a,&nS,&nL);
    printf("nS=%3d, nL=%3d \n",nS,nL);
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
    for(j=0;j<NDATA;j++)
    {
        for(i=0;i<DIM;i++)
        {
            printf("      %d      ",x[i][j]);
        }
        printf("\n");
    }
}

void compare(int r, int x[][NDATA],int *nSmaller,int *nLarger)
{
    int i,j;
    int sum,isum;
    int sm=0,lg=0;
    sum=0;
    for(j=0;j<NDATA;j++)
    {
        sum+= x[r][j];
    }
    printf("Sum for row index = %d is %d\n",r,sum);

    for(i=0;i<DIM;i++)
    {
        isum = 0;
        if(i!=r)
        {
            for(j=0;j<NDATA;j++)
            {
                isum+= x[i][j];
            }   
            //clear printf("isum = %d",isum);
            if(isum>sum)
            {
                lg++;
            }
            else
            {
                sm++;
            }
        }
        else
        {
        
        }
    }
    *nSmaller = sm;
    *nLarger = lg;
    //printf("larger = %d smaller = %d",lg,sm);
}