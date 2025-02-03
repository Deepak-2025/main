#include<stdio.h>
#include<conio.h>
#include<string.h>
#include<stdlib.h>

void calculate();
void end();

main(){

 system("color 0a");
 calculate();
 getch();

}

void end(){
     system("cls");
     printf("\n\n\n\n\n\n\n\t\t------ Thanks to use this software------\n");
     printf("\n\n press any key to exit:");
}
void calculate(){
    float a,c,d;
    char b;
    char n;

      printf("\n\n Enter Your numbers for calculation \n ");
  printf(" Ex:- a + b = ANS \n\n");

    printf(" first number:- ");
    scanf("%f",&a);
    fflush(stdin);
    printf("\n arithmetic op.:- ");
    scanf("%c",&b);

    printf("\n second number:- ");
    scanf("%f",&c);


        system("cls");
     printf("\n Enter Your numbers for calculation \n ");
     printf(" Ex:- a + b = ANS \n\n");
     printf("\n\n number \t number \tANS\n\n\n");

 if(b == '+'){
  d=a+c;
  printf(" %.2f  \t   %c \t %.2f \t=      %.2f",a,b,c,d);

  printf("\n\n Do you want to continue:[y/n]\t");
  fflush(stdin);
  scanf("%c",&n);

    if(n == 'y'){
        system("cls");
       calculate();
    }
    else{
        end();
    }
 }
else{
if(b == '-'){
        d=a-c;
        printf(" %.2f  \t   %c \t %.2f \t=      %.2f",a,b,c,d);
        printf("\n\n Do you want to continue:[y/n]\t");
        fflush(stdin);
        scanf("%c",&n);

        if(n == 'y'){
            system("cls");
        calculate();
        }
        else{
            end();
        }
}
else{
if(b == '*'){
    d=a*c;
    printf(" %.2f  \t   %c \t %.2f \t=      %.2f",a,b,c,d);

     printf("\n\n Do you want to continue:[y/n]\t");
    fflush(stdin);
    scanf("%c",&n);

    if(n == 'y'){
        system("cls");
       calculate();
    }
    else{
        end();
    }
    }
else{
if(b == '/'){
    d=a/c;
    printf(" %.2f  \t   %c \t %.2f \t=      %.2f",a,b,c,d);

     printf("\n\n Do you want to continue:[y/n]\t");
  fflush(stdin);
  scanf("%c",&n);

    if(n == 'y'){
        system("cls");
       calculate();
    }
    else{
        end();
    }
    }
else{
        end();
                }
            }
        }
    }
 }










