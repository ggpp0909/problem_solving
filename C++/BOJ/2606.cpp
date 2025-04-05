#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define MAX 101

bool visited[MAX];
vector<int> v[MAX];
int cnt = 0;

void dfs(int cur) {
    visited[cur] = true;
    cnt++;

    for (auto x: v[cur]) {
        if (visited[x]) continue;
        dfs(x);
    }
}

int main() {
    int N, M;
    cin >> N >> M;

    for (int i = 0; i < M; i++) {
        int a, b;
        cin >> a >> b;
        v[a].push_back(b);
        v[b].push_back(a);
    }

    dfs(1);

    cout << cnt - 1;
    return 0;
}