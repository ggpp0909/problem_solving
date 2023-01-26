#include <iostream>
using namespace std;

int a_mom, a_son, b_mom, b_son;

int gcd(int a, int b) {
    int temp;
    while (a % b != 0) {
        temp = a % b;
        a = b;
        b = temp;
    }
    return b;
}

int main () {
    
    cin >> a_son >> a_mom >> b_son >> b_mom;
    int mom = a_mom * b_mom;
    int son = b_mom * a_son + b_son * a_mom;
    int _gcd = gcd(mom, son);
    
    cout << son / _gcd << " " << mom / _gcd;
    
    return 0;
}
