/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
#include <vector>
using namespace std;
int n;
vector<pair<int,int>> edges;
int main()
{
  
    cin >>n;
    edges.resize(n);
    for(int i=0;i<n;i++){
        int par,son1,son2;
        cin >>par>>son1>>son2;
        edges[par] = {son1,son2};
    }
    
    int now =1;
    int depth =0;

    while(1){
        if(edges[now].second!=-1){
            now = edges[now].second;
            depth ++;
        }
        else {
             break;
        }
    }
     cout<<2*(n-1)-depth;

    return 0;
}
