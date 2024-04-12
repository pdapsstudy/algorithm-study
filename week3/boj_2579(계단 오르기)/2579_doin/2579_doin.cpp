#include <iostream>
using namespace std;
int max_1[301]; // oo 
int max_2[301]; // xo
int main(){
    int n;
    cin >>n;
    int score;
    cin >>score;
    if(n==1) {cout<<score;return 0;}
    max_1[1]=score;
    max_2[1]=score;
    cin >>score;
    max_1[2]=max_1[1]+score;
    max_2[2]=score;
    if(n==2) {cout<<max_1[2];return 0;}
    int max_hubo;
    for(int i=3;i<=n;i++){
        cin >>score;
        max_2[i]=max(max_1[i-2],max_2[i-2])+score;
        max_1[i]=max_2[i-1]+score;
        
    }
    
    cout<<max(max_2[n],max_1[n]);
}