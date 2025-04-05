#include <string>
#include <vector>
#include <algorithm>
#include <iostream>

using namespace std;

int solution(vector<int> A, vector<int> B) {
    // A 정렬, B 정렬 (오름차순)
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());

    int Bidx = 0, ans = 0;
    for (int i = 0; i < A.size(); i++) {
        if (Bidx < B.size() && A[i] < B[Bidx]) { // 이길 수 있으면
            ans++;
            Bidx++;
        } else {
            // 못이기면 다음 이길 수 있는 Bidx까지 땡겨오기
            while (1) {
                Bidx++;
                if (Bidx >= B.size()) break;
                if (A[i] < B[Bidx]) {
                    ans++;
                    Bidx++;
                    break;
                }
            }
        }
    }
    
    return ans;
}
