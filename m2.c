#include<stdio.h>
#define NR 5
#define NC 6
void cc(char a[NR][NC],char ch);
int main()
{
    
    char a[NR][NC];
    char ch;
    int i,j;
    a[0][0]='2',a[0][1]='3',a[0][2]='1',a[0][3]='x',a[0][4]='5',a[0][5]='6',a[1][0]='s',a[1][1]='3',a[1][2]='f',a[1][3]='g',a[1][4]='t',a[1][5]='r',a[2][0]='w',a[2][1]='x',a[2][2]='r',
    a[2][3]='5',a[2][4]='6',a[2][5]='t',a[3][0]='1',a[3][1]='2',a[3][2]='x',a[3][3]='3',a[3][4]='x',a[3][5]='x',a[4][0]='x',a[4][1]='f',a[4][2]='3',a[4][3]='f',a[4][4]='3',a[4][5]='e';
    printf("Lab 4 problem 2 solution by XXX\n");
    printf("Character array is:\n");
    for(i=0;i<NR;i++)
    {
        for(j=0;j<NC;j++)
        {
            printf("%c",a[i][j]);
        }
        puts("");
    }
    printf("Enter charater to end row strings\n");
    scanf("%c",&ch);
    printf("Trimed rows are: \n");
    cc(a,ch);
    return 0;
}

void cc(char a[NR][NC], char ch)
{
    int i,j;
    for(i=0;i<NR;i++)
    {
        for(j=0;j<NC;j++)
        {
            if(a[i][j]==ch)
            {
                j=NC;
            }
            else
            {
                printf("%c",a[i][j]);
            }
        }
        puts(" ");
    }
}