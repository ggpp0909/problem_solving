#include <string>
#include <vector>
#include <queue>
#include <utility>
#include <iostream>

using namespace std;
int di[4] = {1, 0, -1, 0};
int dj[4] = {0, 1, 0, -1};


int solution(vector<string> maps) {
    int si, sj, ei = 0, ej = 0, li = 0, lj = 0;
    int N = (int) maps.size(), M = (int) maps[0].size();
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j ++) {
            if (maps[i][j] == 'S') {
                si = i;
                sj = j;
            }
        }
    }
    int visited[100][100];
    for (int i = 0; i < 100; i++ ) {
        for (int j = 0; j < 100; j++) {
            visited[i][j] = 0;
        }
    }
    
    queue<pair<int, int>> que;
    que.push(make_pair(si, sj));
    visited[si][sj] = 1;
    
    // 레버 찾기
    int cur_i, cur_j, cnt = 0, ans = 0;
    bool flag = false;
    while (!que.empty()) {
        cur_i = que.front().first;
        cur_j = que.front().second;
        cnt = visited[cur_i][cur_j];
        que.pop();
        
        if (maps[cur_i][cur_j] == 'L') {
            ans += cnt - 1;
            flag = true;
            break;
        }
        
        int ni, nj;
        for (int dir = 0; dir < 4; dir ++) {
            ni = cur_i + di[dir];
            nj = cur_j + dj[dir];
            
            if (ni >= 0 && ni < N && nj >= 0 && nj < M && maps[ni][nj] != 'X' && !visited[ni][nj]) {
                visited[ni][nj] = cnt + 1;
                que.push(make_pair(ni, nj));
            }
        }
    }
    if (!flag) return -1;
    
    for (int i = 0; i < 100; i++ ) {
        for (int j = 0; j < 100; j++) {
            visited[i][j] = 0;
        }
    }
    
    que = queue<pair<int, int>>();
    que.push(make_pair(cur_i, cur_j));
    visited[cur_i][cur_j] = 1;
    
    while (!que.empty()) {
        cur_i = que.front().first;
        cur_j = que.front().second;
        cnt = visited[cur_i][cur_j];
        que.pop();
        
        if (maps[cur_i][cur_j] == 'E') {
            return ans + cnt - 1; // 처음 cnt가 1이었으므로
        }
        
        int ni, nj;
        for (int dir = 0; dir < 4; dir ++) {
            ni = cur_i + di[dir];
            nj = cur_j + dj[dir];
            
            if (ni >= 0 && ni < N && nj >= 0 && nj < M && maps[ni][nj] != 'X' && !visited[ni][nj]) {
                visited[ni][nj] = cnt + 1;
                que.push(make_pair(ni, nj));
            }
        }
    }
    return -1;
}
