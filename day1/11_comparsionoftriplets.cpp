#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include<string.h>
using namespace std;

int main()
{
    // stringstream sa,sb;
    // string stra,strb;
    // getline(cin, stra);
    // getline(cin, strb);
    // replace( stra.begin(), stra.end(), ',', ' ');
    // replace( strb.begin(), strb.end(), ',', ' ');
    // sa << stra;
    // sb << strb;

    // int x = 0;
    // while (sa >> x)
    // {
    //     cout << x << endl;
    // }
    // x = 0;
    // while (sb >> x)
    // {
    //     cout << x << endl;
    // }
    string str;
    getline(cin, str); // For reading complete line with spaces
    
    stringstream ss(str);
    
    vector<int>arr;
    int x;
    while(ss >> x){
        arr.push_back(x);
        
        if(ss.peek() == ' ')ss.ignore();
    }
    
    for(int val : arr)cout<<arr<<" ";
}

