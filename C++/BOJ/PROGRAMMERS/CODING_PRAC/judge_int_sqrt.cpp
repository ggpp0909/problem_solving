#include <string>
#include <vector>
#include <cmath>

using namespace std;

long long solution(long long n) {
    long long ans = sqrt(n);
    if (ans * ans == n) return pow(ans + 1, 2);
    else return -1;
}
