#include <iostream>
#include <vector>
#include <queue>
#include <cstring>
#include <algorithm>

using namespace std;
vector<int> v[10001];
queue<int> que;
bool visited[10001];
void dfs(int cur);
void bfs(int V);

int main() {
    int N, M, V;
    cin >> N >> M >> V;

    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }

    for (int i = 0; i < 10001; i++) {
        sort(v[i].begin(), v[i].end());
    }

    dfs(V);
    cout << endl;
    memset(visited, false, sizeof(visited));
    bfs(V);
    
    return 0;
}

void dfs(int cur) {
    visited[cur] = true;
    cout << cur << " ";  

    for (auto x: v[cur]) {
        if (visited[x]) continue;
        dfs(x);
    }
}

void bfs(int V) {
    que.push(V);
    visited[V] = true;

    int cur;
    while (!que.empty()) {
        cur = que.front();
        que.pop();
        cout << cur << " ";
        
        for (auto x: v[cur]) {
            if (visited[x]) continue;
            visited[x] = true;
            que.push(x);
        }
    }
}
