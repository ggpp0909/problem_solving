#include <iostream>
#include <map>

using namespace std;

int main() {
    int N, M, ans = 0;
    map<string, bool> dic;
    cin >> N >> M;
    for (int i = 0; i < N; i++) {
        string temp;
        cin >> temp;
        dic.insert({temp, true});
    }
    
    for (int i = 0; i < M; i++) {
        string temp;
        cin >> temp;
        if (dic.find(temp) != dic.end()) {
            ans++;
        }
    }
    
    cout << ans;
    return 0;
}
