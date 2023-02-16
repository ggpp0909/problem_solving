#include <iostream>
#define MAXN 10010
using namespace std;

int par[MAXN] = {};
int visited[MAXN] = {};

int main() {
    
    int T, N;

    cin >> T;
    while (T--) {
        for (int i=0; i<MAXN; i++) {
            par[i] = i;
            visited[i] = 0;
        }
        
        cin >> N;
        int a, b;
        for (int i=0; i<N - 1; i++) {
            cin >> a >> b;
            par[b] = a;
        }
        
        cin >> a >> b; // 타겟 노드 두개
        
        visited[a] = 1;
        while (a != par[a]) { // a 경로 찾기
            a = par[a];
            visited[a] = 1;
        }

        
        // b부터 타고 올라가기
        while (1) {
            if (visited[b]) {
                cout << b << '\n';
                break;
            }
            b = par[b];
        }
    }
    
    return 0;
}
