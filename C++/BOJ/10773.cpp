#include <iostream>
#include <stack>
using namespace std;

int K;
stack<int> st;

int main() {
    cin >> K;
    int input;
    for (int i = 0; i < K; i++) {
        cin >> input;
        if (input == 0) {
            st.pop();
        } else {
            st.push(input);
        }
    }
    
    int ans = 0;
    while (!st.empty()) {
        ans += st.top();
        st.pop();
    }
    
    cout << ans;
    return 0;
}
