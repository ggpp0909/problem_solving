#include <iostream>
#include <vector>
using namespace std;

int N;
vector<int> vec;

int bs(int num) {
    int s = 0;
    int e = (int) vec.size() - 1;
    int mid;
    
    while (s < e) {
        mid = (s + e) / 2;
        if (num > vec[mid]) {
            s = mid + 1;
        } else {
            e = mid;
        }
    }
    return e;
}

int main() {
    cin >> N;
    int first;
    cin >> first;
    vec.push_back(first);
    
    int temp;
    for (int i = 1; i < N; i++) {
        cin >> temp;
        if (vec.back() < temp) {
            vec.push_back(temp);
        } else {
            int idx = bs(temp);
            vec[idx] = temp;
        }
    }
    
    cout << vec.size();
    return 0;
}
