/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
using namespace std;
int n;
int main()
{
    
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin >>n;
    int now =1;
    int depth =0;
    for(int i=0;i<n;i++){
        int par,son1,son2;
        cin >>par>>son1>>son2;
        
        if(par==now){
            if(son2 ==-1){
                break;
            }
            else {
                depth++;
                now =son2;
            }
        }
    }
   cout<<2*(n-1)-depth;

    return 0;
}
