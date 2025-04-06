#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int N, M;
#define MAX 1001
int arr[MAX][MAX];
int ans;
vector<pair<int, int>> tmt;
queue<pair<int, int>> que;

int di[] = {0, 1, 0, -1};
int dj[] = {1, 0, -1, 0};

void bfs() {
    for (auto x: tmt) {
        int tempi, tempj;
        tempi = x.first;
        tempj = x.second;
        que.push({tempi, tempj});
    }
    int dist = 0;

    while (!que.empty()) {

        int sz = que.size();

        for (int i = 0; i < sz; i++) {
            int cur_i, cur_j;
            cur_i = que.front().first;
            cur_j = que.front().second;
            que.pop();
    
            for (int dir = 0; dir < 4; dir++) {
                int ni = cur_i + di[dir];
                int nj = cur_j + dj[dir];
    
                if (ni < 0 || nj < 0 || ni >= N || nj >= M) continue;
                if (arr[ni][nj] != 0) continue;
    
                que.push({ni, nj});
                arr[ni][nj] = 1;
            }
        }
        dist++;
    }
    ans = dist - 1;
}

int main() {
    cin >> M >> N;

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            int temp;
            cin >> temp;
            arr[i][j] = temp;
            if (temp == 1) tmt.push_back({i, j});
        }
    }

    bfs();

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (arr[i][j] == 0) ans = -1;
        }
    }
    cout << ans;

    return 0;
}