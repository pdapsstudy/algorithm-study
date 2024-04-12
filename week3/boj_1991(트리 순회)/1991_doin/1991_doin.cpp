#include <iostream>
#include <vector>
using namespace std;
vector<int> par[27];
int num;
void firstfirst(int n){
    if(n==0)return;
    int a=par[n].at(0);
    int b=par[n].at(1);
    
    char root='A'+n-1;
    cout<<root;
    firstfirst(a);
    firstfirst(b);
    
}
void firstmiddle(int n){
    if(n==0)return;
    int a=par[n].at(0);
    int b=par[n].at(1);
        firstmiddle(a);
    char root='A'+n-1;
    cout<<root;

    firstmiddle(b);
    
}
void firstlast(int n){
    if(n==0)return;
    int a=par[n].at(0);
    int b=par[n].at(1);
    firstlast(a);
    firstlast(b);
    char root='A'+n-1;
    cout<<root;

    
}
int main()
{
    cin >>num;
    for(int i=0;i<num;i++){
        char x,y,z;
        cin >>x>>y>>z;
        int a=x-'A'+1;
        int b,c;
        if(y=='.'){b=0;}
        else b=y-'A'+1;
        if(z=='.'){c=0;}
        else c=z-'A'+1;
        par[a].push_back(b);
        par[a].push_back(c);
    }
    firstfirst(1);
    cout<<"\n";
    firstmiddle(1);
    cout<<"\n";
    firstlast(1);
    return 0;
}
