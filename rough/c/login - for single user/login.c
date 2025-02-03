#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>


struct signup{

    char username[20];
    char password[20];

}lo;

struct login{
    char username[20];
    char password[20];
}li;

struct check{
        char usern[10];
        char userp[10];
}ch;

void i();
void signup();
void login();


main(){

i();

}

void i(){

char a;

printf("\n\n\n\n   press 'S' for signup or 'L' for login :-   ");
scanf("%c",&a);

if(a == 's'){
 signup();
}
else{
    if(a == 'l'){
       login();
    }
    else{
            system("cls");
    printf("\n\n\n\t\t-----Thanks for using this software-----");
     printf("\n\n\n press any key to exit :  ");
    }
}
}

void signup(){
fflush(stdin);
system("cls");

char a;
printf("\n\n\n  ENTER USERNAME :-   ");
fgets(lo.username,20,stdin);

FILE *ptr = NULL;
ptr = fopen("login.txt","w");
//fprintf(ptr,"%s","username :-  ");
fprintf(ptr,"%s",lo.username);
fclose(ptr);


printf("\n\n  ENTER PASSWORD :-   ");
fgets(lo.password,20,stdin);

FILE *ptt = NULL;
ptt = fopen("login.txt","a");
//fprintf(ptt,"%s","password :-  ");
fprintf(ptt,"%s",lo.password);
fclose(ptt);

printf("\n\n your account is created.");
printf("\n\n press 'L' for login or any key to exit:-   ");
scanf("%c",&a);

if(a == 'l'){
       login();
    }
    else{
            system("cls");
    printf("\n\n\n\t\t-----Thanks for using this software-----");
    printf("\n\n\n press any key to exit :  ");
    }
getch();

}

void login(){
    system("cls");
fflush(stdin);
uname:
     printf("\n\n  ENTER username :-   ");
     fgets(li.username,20,stdin);

FILE *ptr = NULL;
ptr = fopen("login.txt","r");

char user[20];
fgets(ch.usern,20,ptr);
fclose(ptr);

int c,p;
c = strcmp(li.username,ch.usern);


if(c == 0){
    upass:
      printf("\n\n  ENTER PASSWORD :-   ");
      fgets(li.password,20,stdin);

FILE *ptr = NULL;
ptr = fopen("login.txt","r");

char user[20];
int q;
for(q=0;q<=1;++q){
fgets(ch.userp,20,ptr);
}
fclose(ptr);

      p = strcmp(li.password,ch.userp);
       if(p == 0){
        printf("\n\n you are logged in");
        getch();
         }
         else{
            char s;

          printf("\n\n\nPASSWORD DOES NOT MATCH.\n");
          printf("DO YOU WANT TO TRY AGAIN [Y/N] :   ");
          fflush(stdin);
          scanf("%c",&s);

           if(s == 'y'){
                system("cls");
                printf("\n\n  ENTER username :-  %s",li.username);
                fgets(li.username,20,stdin);
               goto upass;

           }else{
             system("cls");
             printf("\n\n\t    -----Thanks for using this software-----");
            printf("\n\n\n press any key to exit :  ");
            getch();

           }

         }
}
        else{
           char z;
          printf("\n\n\n USERNAME NOT FOUND.");
          printf("\n DO YOU WANT TO TRY AGAIN [Y/N] :   ");
          fflush(stdin);
          scanf("%c",&z);

           if(z == 'y'){
                system("cls");
                fgets(li.username,20,stdin);
               goto uname;

           }else{
             system("cls");
             printf("\n\n\t    -----Thanks for using this software-----");
             printf("\n\n\n press any key to exit :  \n\n");
            getch();

           }
                }
}

