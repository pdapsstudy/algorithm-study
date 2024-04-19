/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <vector>
using namespace std;
/*
10
10 20
10 20 25
10 20 25 50
*/
int main()
{
    int n;
    vector<int> mx;
    cin >>n;
    for(int i=0;i<n;i++){
        int x;
        cin >>x;
        if(mx.size()==0)mx.push_back(x);
        else if(mx.size()==1){
            if(x<mx.at(mx.size()-1)){
                mx.at(mx.size()-1)=x;
            }
            else if(x>mx.at(mx.size()-1)){
                mx.push_back(x);
            }
        }
        else if(mx.size()>1){
            // cout<<i<<"\n";
            if(x<mx.at(mx.size()-1)&&x>mx.at(mx.size()-2)){
                mx.pop_back();
                mx.push_back(x);
            }
            else if(x>mx.at(mx.size()-1)){
                mx.push_back(x);
            }
        }
        
        
    }
    cout<<mx.size();
    return 0;
    
}
