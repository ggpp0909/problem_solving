#include <iostream>
#include <queue>
#include <vector>
using namespace std;
#define MAX 101

vector<int> v[MAX];
bool visited[MAX];

int N, M, ans;

void dfs(int cur) {
    visited[cur] = true;
    ans++;

    for (auto x: v[cur]) {
        if (visited[x]) continue;
        dfs(x);
    }
}

int main() {
    cin >> N >> M;
    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }

    dfs(1);
    cout << ans - 1;
    return 0;
}