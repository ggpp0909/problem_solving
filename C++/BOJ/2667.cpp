#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;
int N;
#define MAX 25

vector<string> arr;
vector<int> ans;
queue<pair<int, int>> que;
bool visited[MAX][MAX];

int di[] = {1, 0, -1, 0};
int dj[] = {0, 1, 0, -1};

void bfs(int tempi, int tempj) {
    que.push({tempi, tempj});
    visited[tempi][tempj] = true;
    int cnt = 0;

    while (!que.empty()) {
        int cur_i = que.front().first;
        int cur_j = que.front().second;
        que.pop();
        cnt++;

        for (int dir = 0; dir < 4; dir++) {
            int ni = cur_i + di[dir];
            int nj = cur_j + dj[dir];

            if (ni < 0 || nj < 0 || ni >= N || nj >= N) continue;
            if (arr[ni][nj] == '0' || visited[ni][nj]) continue;

            visited[ni][nj] = true;
            que.push({ni, nj});
        }
    }
    ans.push_back(cnt);
}

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        string temp;
        cin >> temp;
        arr.push_back(temp);
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (arr[i][j] == '1' && visited[i][j] == false) bfs(i, j);
        }
    }

    sort(ans.begin(), ans.end());
    cout << ans.size() << endl;
    for (auto x: ans) {
        cout << x << endl;
    }


    return 0;
}