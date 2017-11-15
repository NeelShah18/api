#include <stdio.h>

int lookup(char grade);

int main(void)
{
   printf("part2 problem 3");
   printf("Xiaoyi Xia");
   int val[]={5,-5,9,-9,3,-3,0};
   //A,a,B,b,C,c
   int total[100];
   int grade;
   int i=0; // one grade 
   int temp; 
   // loop until user types end-of-file key sequence
   while ((grade = getchar()) != '.')
    {
      
      // determine which grade was input
      if(i>0)
      {
        temp = val[lookup(grade)];
        total[i] = total[i-1] + temp;
        //printf("in if");
        //printf("Total: %d, %d, %d, %d",total[i],i,val[lookup(grade)],lookup(grade));
      }
      else
      {
        temp = val[lookup(grade)];
        total[i] = temp;
        //printf("in else");
        //printf("Total: %d, %d, %d, %d",total[i],i,val[lookup(grade)],lookup(grade));
      }
      i++;
   } // end while

   // output summary of results
   puts("\nTotalsc:\n");
   int j;
   for(j==0;j<28;j++)
   {
       printf(" %d \n",total[j]);
   }

} 

int lookup(char grade)
{
    switch (grade) { // switch nested in while

         case 'A': // grade was uppercase A
            return 0;
            //printf("Here - %d\n",total);
            //break;

         case 'a': // or lowercase a
            return 1;
            //printf("Here - %d",total);
            //break;

         case 'B': // grade was uppercase B
            return 2;
            //printf("Here - %d",total);
            //break;

         case 'b': // or lowercase b
            return 3;
            //printf("Here - %d",total);
            //break;

         case 'C': // grade was uppercase C
            return 4;
            //printf("Here - %d",total);
            //break;

         case 'c': // or lowercase c
            return 5;
            //printf("Here - %d",total);
            //break;

         case 'X' :
         return 6;
            //break;
            //nothing

         case '\n': // ignore newlines,
         case '\t': // tabs,
         case ' ': // and spaces in input
            return 6;
            //break; 

         default: // catch all other characters
            printf("%s", "Incorrect letter grade entered."); 
            puts(" Enter a new grade."); 
            return 6;
            //break; // optional; will exit switch anyway
      } 
}