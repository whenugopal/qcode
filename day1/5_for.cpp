#include<bits/stdc++.h>
using namespace std;
int main(){
    int a,b,c;
    string i[10]={"","one","two","three","four","five","six","seven","eight","nine"};
    cin>>a>>b;
    for(c=a;c<=b;c++){
        cout<<((c<=9)?i[c]:((c%2==0)?"even":"odd"))<<endl;
    }
    return 0;
}