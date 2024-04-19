#include <iostream>
#include <vector>
using namespace std;
int N,W;
vector <pair<int,int>> wv;
int val[101][100001];
void getval(){
    for(int i=0;i<=N;i++){
        for(int w=0;w<=W;w++){
            if(i==0 || w==0) {val[i][w]=0;continue;}
            if(w>=wv.at(i-1).first){
                if(val[i-1][w]<=wv.at(i-1).second+val[i-1][w-wv.at(i-1).first])
                    val[i][w]=wv.at(i-1).second+val[i-1][w-wv.at(i-1).first];
                else val[i][w]=val[i-1][w];
                
            }
            else val[i][w]=val[i-1][w];
        }
    }
}

int main(){
    cin >>N>>W;
    
    for(int i=0;i<N;i++){
        int w,v;
        cin >>w>>v;
        wv.push_back({w,v});
    }
    getval();
    for(int i=0;i<=N;i++){
        for(int j=0;j<=W;j++){
            cout<<val[i][j]<<" ";
        }
        cout<<"\n";
    }
    cout<<val[N][W];
    return 0;
}


