#include <string>
#include <vector>

#define MAXN 100010
using namespace std;

int fibo[MAXN];

int solution(int n) {
    fibo[1] = 1;
    fibo[2] = 1;
    for (int i = 3; i <= n; i++) {
        fibo[i] = (fibo[i - 1] + fibo[i - 2]) % 1234567;
    }
    
    return fibo[n];
}
