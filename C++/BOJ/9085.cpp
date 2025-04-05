#include <iostream>
using namespace std;

int main() {
    
    int T;
    cin >> T;
    for (int _ = 0; _ < T; _++) {
        int N, res = 0;
        cin >> N;
        int temp = 0;
        for (int i = 0; i < N; i++) {
            cin >> temp;
            res += temp;
        }
        cout << res << '\n';
    }
    
    return 0;
}
