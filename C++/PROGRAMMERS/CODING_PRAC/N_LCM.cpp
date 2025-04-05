#include <string>
#include <vector>

using namespace std;

int gcd(int a, int b) {
    int temp;
    while (a % b != 0) {
        temp = a % b;
        a = b;
        b = temp;
    }
    return b;
}

int lcm(int a, int b) {
    return (a * b) / gcd(a, b);
}

int solution(vector<int> arr) {
    int ans = arr[0];
    for (int i = 1; i < arr.size(); i++) {
        ans = lcm(ans, arr[i]);
    }
    return ans;
}
