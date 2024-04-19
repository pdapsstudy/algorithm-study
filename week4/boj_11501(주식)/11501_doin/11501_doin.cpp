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
        val[0]=x;
        for(int j=1;j<n;j++){
            cin >>x;
            val[j]=x;
        }
        for(int j=n-1;j>=0;j--){
            if(val[j]>max_v){
                max_v=val[j];
            }
            maxValueUntilIndex[j]=max_v;
        }
        for(int j=0;j<n;j++){
            ans=ans+maxValueUntilIndex[j]-val[j];
        }
        cout<<ans<<"\n";
    }
    
    return 0;
}
