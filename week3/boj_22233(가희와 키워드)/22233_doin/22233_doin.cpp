/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <set>
#include <string>
#include <queue>
#include <vector>
using namespace std;
int n,m;
set<string> memo;
set<string> slice(string s){
    set<string> used2;
    string temp ="";
    // cout<<s.length()<<"\n";
    for(int i=0;i<s.length();i++){
        if(s[i]==','){
            used2.insert(temp);
            temp="";
            // cout<<temp<<"\n";
            continue;
        }
        temp = temp+s[i];
    }
    used2.insert(temp);
    return used2;
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
        memo.insert(word);
    }
    set<string> used;
    string s;
    for(int j=0;j<m;j++){
        
        cin >>s;
        
        used = slice(s);
        // cout<<used.size()<<"\n";
        auto it1 =memo.begin();
        auto it2 = used.begin();
        vector<set<string>::iterator> iters;
        // cout<<memo.size()<<" "<<used.size()<<"\n";
        while(it1!=memo.end()&&it2!=used.end()){
            if(*it1==*it2){
                iters.push_back(it1);
                // cout<<*it1<<*it2<<"\n";
                it1++;
                it2++;
            }
            else if(*it1>*it2){
                it2++;
            }
            else {
                it1++;
            }
        }
        // cout<<"yes\n";
        for(int i=0;i<iters.size();i++){
            auto iter = iters.at(i);
            memo.erase(*iter);
        }
        cout<<memo.size()<<"\n";
    }
    return 0;
}
