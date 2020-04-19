//Digital Root
#include<bits/stdc++.h>

using namespace std;

int digital_root(int n){
    int rem, sum = 0;
    while( n > 0 ){
        rem = n % 10;
        sum = sum + rem;
        n = n / 10;
    }
    return((sum>=10)?digital_root(sum):sum);
}

int main(){
    int n,sum=0;
    cout<<"Enter the number:";
    cin>>n;
    sum = digital_root(n);
    cout<<sum;
}