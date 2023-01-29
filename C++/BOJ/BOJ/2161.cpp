#include <stdio.h>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;

int N;
queue<int> que;
vector<int> ans;

int main () {
    
    cin >> N;
    for (int i = 1; i <= N; i++) {
        que.push(i);
    }
    
    while (!que.empty()) {
        ans.push_back(que.front()); // 제일 위에 카드 버리기
        que.pop();
        if (!que.empty()) { // 위에카드 맨 밑에 놓기
            que.push(que.front());
            que.pop();
        }
    }
    
    for (int i = 0; i < ans.size(); i++) {
        cout << ans[i] << " ";
    }
    
    return 0;
}
