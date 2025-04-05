#include <iostream>
#include <cmath>

using namespace std;

int T, x1, x2, y_1, y2, n, cx, cy, r;

int main() {
    
    cin >> T;
    for(int _ = 0; _ < T; _++) {
        cin >> x1 >> y_1 >> x2 >> y2 >> n;
        int ans = 0;
        
        for(int i = 0; i < n; i++) {
            cin >> cx >> cy >> r;
            // 둘다 원 내부에 있거나 둘다 원 외부에 있으면 경계 안지나므로 무시
            if (pow(cx - x1, 2) + pow(cy - y_1, 2) > pow(r, 2)
                && pow(cx - x2, 2) + pow(cy - y2, 2) > pow(r, 2)) continue;
            
            if (pow(cx - x1, 2) + pow(cy - y_1, 2) < pow(r, 2)
                && pow(cx - x2, 2) + pow(cy - y2, 2) < pow(r, 2)) continue;
            
            ans++;
        }
        
        cout << ans << '\n';
    }
    
    return 0;
}
