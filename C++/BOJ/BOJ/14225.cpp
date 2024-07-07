#include<iostream>
#include<algorithm>
#include<cmath>
#include<string>
using namespace std;

int N;
int visited[2000001];
int seq[21];

void dfs(int x, int sum)
{
    visited[sum] = true;
    if (x == N) return;
    else{
        dfs(x + 1, sum);
        dfs(x + 1, sum + seq[x]);
    }
}

int main()
{
    cin >> N;

    for (int i = 0; i < N; i++)
        cin >> seq[i];
    
    dfs(0, 0);

    int j = 1;
    while (visited[j] == true) j++;
    cout << j;
}
