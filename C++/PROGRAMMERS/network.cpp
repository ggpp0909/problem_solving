#include <string>
#include <vector>
#include <algorithm>
using namespace std;

int par[201];

int find(int x) {
    if(par[x] == x)
        return x;
    
    return par[x] = find(par[x]);
}

void _union(int a,int b) {
    a = find(a);
    b = find(b);

    par[a] = b;
}

int solution(int n, vector<vector<int>> computers) {

    for(int i = 0; i < n; i++)
        par[i] = i;
    
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j < n; j++)
        {
            if(computers[i][j]==1)
                _union(i,j);
        }
    }
    for(int i = 0; i < n; i++)
        par[i] = find(i);

    sort(par, par + n);
    
    int temp = par[0], cnt = 1;
    for(int i = 1; i < n; i++) {
        if(par[i] != temp) {
            temp = par[i];
            cnt++;
        }
    }
    
    return cnt;
}