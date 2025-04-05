#include <iostream>
#include <vector>
#include <queue>

using namespace std;

vector<string> arr;
int M, N, ans;
int di[] = {1, 0, -1, 0};
int dj[] = {0, 1, 0, -1};
queue<pair<int, int>> que;
bool visited[101][101];
int dist[101][101];

void bfs(int ti, int tj) {
    que.push({ti, tj});
    visited[ti][tj] = true;
    dist[ti][tj] = 1;

    while (!que.empty()) {
        int cur_i, cur_j;
        cur_i = que.front().first;
        cur_j = que.front().second;
        que.pop();
    
        if (cur_i == N - 1 && cur_j == M - 1) return;
    
        for (int dir = 0; dir < 4; dir++) {
            int ni = cur_i + di[dir];
            int nj = cur_j + dj[dir];
    
            if (ni < 0 || nj < 0 || ni >= N || nj >= M || arr[ni][nj] == '0' || visited[ni][nj]) continue;
            visited[ni][nj] = true;
            dist[ni][nj] = dist[cur_i][cur_j] + 1;
            que.push({ni, nj});
        }
    }
}

int main() {
    cin >> N >> M;
    
    for (int i = 0; i < N; i++) {
        string temp;
        cin >> temp;
        arr.push_back(temp);
    }

    bfs(0, 0);
    cout << dist[N-1][M-1];

    return 0;
}