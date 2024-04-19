/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>
using namespace std;
int main()
{
    int num;
    cin >>num;
    cin.tie(NULL);
    ios_base::sync_with_stdio(false);
    int val[1000000];
    int maxValueUntilIndex[1000000];
    int minValueUntilIndex[1000000];
    for(int i=0;i<num;i++){
        int n;
        cin >>n;
        int max_v;
        int min_v;
        long long ans=0;
        int x;
        cin >>x;
        max_v=0;
        min_v=x;
        // minValueUntilIndex[0]=min_v;
        val[0]=x;
        for(int j=1;j<n;j++){
            cin >>x;
            val[j]=x;
            // if(x<min_v){
            //     minValueUntilIndex[j]=min_v;
            // }
        }
        for(int j=n-1;j>=0;j--){
            if(val[j]>max_v){
                max_v=val[j];
            }
            maxValueUntilIndex[j]=max_v;
        }
        for(int j=0;j<n;j++){
            // cout<<val[j]<<" "<<maxValueUntilIndex[j]<<"\n";
            ans=ans+maxValueUntilIndex[j]-val[j];
        }
        cout<<ans<<"\n";
    }
    
    return 0;
}
