#include <stdio.h>
int main()
{
    char a[5][6];
    int i,j;

    for (i=0;i<5;i++)
    {
        for(j=0;j<6;j++)
        {
            scanf("%c",&a[i][j]);
        }
        printf("\n");
    }
      for (i=0;i<5;i++)
    {
        for(j=0;j<6;j++)
        {
            printf("%c",a[i][j]);
        }
        printf("\n");
    }
    
    return 0;
}