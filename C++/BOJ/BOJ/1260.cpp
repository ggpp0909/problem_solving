#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;
vector<int> vec[10010];
vector<int> dfs_res;
vector<int> bfs_res;


int visited[1010];
int N, M, V;

void dfs(int cur) {
    for (int i = 0; i < vec[cur].size(); i++ ){
        if (visited[vec[cur][i]]) continue;
        
        visited[vec[cur][i]] = 1;
        dfs_res.push_back(vec[cur][i]);
        dfs(vec[cur][i]);
    }
}

void bfs(int cur) {
    queue<int> que;
    que.push(cur);
    visited[cur] = 1;
    while (!que.empty()) {
        int now = que.front();
        que.pop();
        
        cout << now << ' ';
        for (int i = 0; i < vec[now].size(); i++) {
            if (visited[vec[now][i]]) continue;
            
            visited[vec[now][i]] = 1;
            que.push(vec[now][i]);
        }
    }
}


int main() {
    cin >> N >> M >> V;
    int x, y;

    for (int i = 0; i < M; i++) {
        cin >> x >> y;
        vec[x].push_back(y);
        vec[y].push_back(x);
    }
    
    for (int i = 1; i <= N; i++) {
        sort(vec[i].begin(), vec[i].end());
    }
    
    visited[V] = 1;
    dfs_res.push_back(V);
    dfs(V);
    for (int i = 0; i < dfs_res.size(); i++ ) {
        cout << dfs_res[i] << ' ';
    }
    cout << '\n';
    fill(visited, visited + 1010, 0);
    bfs(V);
    
    return 0;
}
