#include <iostream>
#include <stack>
using namespace std;

int T;
string str;


int main() {
    cin >> T;
    
    for (int _ = 0; _ < T; _++) {
        cin >> str;
        string ans = "YES\n";
        stack<char> st;
        
        for (int i = 0; i < str.length(); i++){
            if (str[i] == '(') {
                st.push(str[i]);
            } else if (!st.empty() && str[i] == ')' && st.top() == '(') {
                st.pop();
            } else {
                ans = "NO\n";
                break;
            }
        }
        
        if (!st.empty()) ans = "NO\n";
        cout << ans;
    }
    
    return 0;
}
