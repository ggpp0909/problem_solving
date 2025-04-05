#include <iostream>
using namespace std;

int main() {
    // 입력 받아서 배열 생성
    int N, M;
    cin >> N >> M;
    
    int arr[310][310]; // 일부러 한칸 크게, 1행, 1열 0처리
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            cin >> arr[i][j];
        }
    }
    
    // 프리픽스 배열 만들기
    int prefix[310][310] = {};
    for (int i = 1; i <= N; i++) {
        for (int j = 1; j <= M; j++) {
            prefix[i][j] = arr[i][j] +  prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1];
        }
    }
    
    // 답 내기
    int K, a, b, c, d;
    cin >> K;
    for (int i = 0; i < K; i++) {
        cin >> a >> b >> c >> d;
        cout << prefix[c][d] - prefix[a - 1][d] - prefix[c][b - 1] + prefix[a - 1][b - 1] << endl;
    }
    
    return 0;
}
