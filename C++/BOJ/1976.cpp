#include <stdio.h>
#include <iostream>
#include <vector>
using namespace std;

int N, M;
int par[210];


int find(int x) {
    if (x == par[x]) return x;
    par[x] = find(par[x]);
    return par[x];
}

void _union(int x, int y) {
    x = find(x);
    y = find(y);
    
    par[x] = y;
}

int main() {
    cin >> N >> M;
    int temp;

    for (int i = 0; i < N; i++ ) {
        par[i] = i;
    }
    
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            cin >> temp;
            if (temp == 1 && find(i) != find(j)) {
                _union(i, j);
            }
        }
    }
    
    string ans = "YES";
    cin >> temp;
    int first_root = find(temp - 1);
    for (int i = 1; i < M; i++){
        cin >> temp;
        if (find(temp - 1) != first_root) {
            ans = "NO";
            break;
        }
    }
    cout << ans;
    return 0;
}
