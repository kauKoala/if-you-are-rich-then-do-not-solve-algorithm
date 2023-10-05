#include <bits/stdc++.h>
using namespace std;

const int MX = 201;
vector<int> adj[MX];
bool vis[MX];
int ans;

void solve(int idx) {
    vis[idx] = true;
    for (auto e : adj[idx]) {
        if (vis[e]) continue;
        solve(e);
    }
}

int solution(int n, vector<vector<int>> computers) {
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (computers[i][j] == 0) continue;
            adj[i].push_back(j);
            adj[j].push_back(i);
        }
    }
    
    for (int i = 0; i < n; i++) {
        if (vis[i]) continue;
        solve(i);
        ans++;
    }
    
    return ans;
}