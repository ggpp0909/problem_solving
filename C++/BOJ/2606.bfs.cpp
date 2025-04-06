#include <iostream>
#include <vector>
#include <queue>
using namespace std;
#define MAX 101
int N, M, ans;
queue<int> que;
bool visited[MAX];
vector<int> v[MAX];

void bfs() {
    que.push(1);
    visited[1] = true;

    while (!que.empty()) {
        int cur = que.front();
        que.pop();
        ans++;

        for (auto x: v[cur]) {
            if (visited[x]) continue;
            que.push(x);
            visited[x] = true;
        }
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
    bfs();
    cout << ans - 1;

    return 0;
}