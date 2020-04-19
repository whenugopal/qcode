#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');
    string o[10]={"Grater than 9","one","two","three","four","five","six","seven","eight","nine"};
    if(n>9)
        cout<<"Greater than 9";
    else
        cout<<o[n];
    return 0;
}
