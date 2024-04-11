/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <map>
#include <string>
#include <queue>
#include <vector>
using namespace std;
int n,m;
map<string,int> memo;

int slice(string s){
    int a =0;
    string temp ="";
    // cout<<s.length()<<"\n";
    for(int i=0;i<s.length();i++){
        if(s[i]==','){
            if(memo[temp]){
                memo[temp]=false;
                a++;
            }
            temp="";
            continue;
        }
        temp = temp+s[i];
    }
            if(memo[temp]){
                memo[temp]=false;
                a++;
            }

            temp="";
            
  
    return a;
}
int main()
{
   cin.tie(NULL);
   ios_base::sync_with_stdio(false);
    cin >>n>>m;
    // cout<<n<<" "<<m<<"\n";
    for(int i=0;i<n;i++){
        string word;
        cin >>word;
        memo.insert({word,1});
    }
    string s;
    for(int j=0;j<m;j++){
        
        cin >>s;
        
        int a = slice(s);
        // cout<<used.size()<<"\n";
        n= n-a;
        cout<<n<<"\n";
    }
    return 0;
}
