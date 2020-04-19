#include <bits/stdc++.h>

using namespace std;

int main(){
    int n,sum=0;
    cin>>n;
    int ar[n];
    for(int i=0;i<n;i++){
        cin>>ar[i];
        sum =sum+ar[i];
    }
    cout<<sum;
    return 0;
}