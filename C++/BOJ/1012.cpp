#include <iostream>
#include <queue>

using namespace std;

int T;
int di[4] = {1, 0, -1, 0};
int dj[4] = {0, 1, 0, -1};

int main() {
    
    cin >> T;
    for (int _ = 0; _ < T; _++) {
        int M, N, K;
        cin >> M >> N >> K;
        int arr[50][50] = {0};
        
        for (int i = 0; i < K; i++) {
            int x, y;
            cin >> x >> y;
            arr[x][y] = 1;
        }
        
        int visited[50][50] = {0};
        int ans = 0;
        for (int i = 0; i < 50; i++) {
            for (int j = 0; j < 50; j++) {

                if (arr[i][j] == 0 || visited[i][j]) continue;
                ans++;
                
                queue<pair<int, int>> que;
                pair<int, int> temp = make_pair(i, j);
                que.push(temp);
                visited[i][j] = 1;
                while (!que.empty()) {
                    int x = que.front().first;
                    int y = que.front().second;
                    que.pop();
                    
                    for (int dir = 0; dir < 4; dir++) {
                        int ni = x + di[dir];
                        int nj = y + dj[dir];
                        
                        if ((0 <= ni && ni < M) && (0 <= nj && nj < N) && !visited[ni][nj] && arr[ni][nj]) {
                            visited[ni][nj] = 1;
                            que.push(make_pair(ni, nj));
                        }
                    }
                }
            }
        }
        
        cout << ans << '\n';
    }
    return 0;
}
