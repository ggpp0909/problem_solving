#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int n, m;
#define MAX 101
vector<int> v[MAX];
queue<pair<int, int>> que;
int ans;
bool visited[MAX];

void bfs(int s, int e) {
    que.push({s, 0});
    visited[s] = true;
;

    while (!que.empty()) {
        int cur = que.front().first;
        int dist = que.front().second;
        que.pop();
        if (cur == e) {
            ans = dist;
            return;
        }

        for (auto x: v[cur]) {
            if (visited[x]) continue;
            que.push({x, dist + 1});
            visited[x] = true;
        }
    }
    ans = -1;
}

int main() {
    int a, b;
    cin >> n >> a >> b >> m;
    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        v[x].push_back(y);
        v[y].push_back(x);
    }

    bfs(a, b);
    cout << ans;

    return 0;
}