#include <iostream>
using namespace std;

int main() {
    int t;
    
    cin >> t;
    
    for (int _ = 0; _ < t; _++) {
        int a, b, cnt = 0;
        int temp;
        cin >> a >> b;
        
        temp = 1;
        while (cnt < b) {
            temp = (a * temp) % 10;
            cnt++;
        }
        temp = temp == 0 ? 10 : temp;
        cout << temp << '\n';
    }
    
    return 0;
}
