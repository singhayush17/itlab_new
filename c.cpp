#include<bits/stdc++.h>
#include <string>
#include <conio.h>
using namespace std;

int main()
{

char c;
string password;
cout<<"Enter password: ";
while ((c=getch()) != '\r')
{
    password.push_back(c);
    putch('*');
}

// cout<<password;

cout<<"\nEnter your choice: \n1.Change password\n2.Exit\n";
int choice;
cin>>choice;
char w=getchar();
int attempts=3;
if(choice==1)
{
    while(attempts--)
    {
        string temp;
        cout<<"Enter your old password: ";
        while ((c=getch()) != '\r')
        {
            temp.push_back(c);
            putch('*');
        }
        if(temp==password)
        {
        cout<<"\nEnter new password: ";
        while ((c=getch()) != '\r')
        {
            password.push_back(c);
            putch('*');
        }       

        cout<<"\nPassword Changed successfully!";
        break;

        }
        else
        {
            cout<<"\nIncorrect password! "<<attempts<<" attempts left!\n";
        }

    if(attempts==0)
    {
        cout<<"Please try again after 10 mins!\n";
    }
        
    }

    
}




return 0;
}
