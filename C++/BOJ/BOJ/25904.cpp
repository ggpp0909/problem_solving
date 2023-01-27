#include <iostream>
#include <vector>
using namespace std;


int main() {
    int N, X;
    cin >> N >> X;
    
    vector<int> arr;
    for (int i = 0; i < N; i++) {
        int temp;
        cin >> temp;
        arr.push_back(temp);
    }
    
    int idx = 0;
    while (true) {
        if (arr[idx] < X) {
            cout << idx + 1;
            break;
        }
        idx = (idx + 1) % N;
        X++;
    }
    
    return 0;
}
