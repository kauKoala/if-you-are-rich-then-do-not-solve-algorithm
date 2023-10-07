#include <bits/stdc++.h>
using namespace std;

const int MX = 20001;

vector<int> adj[MX];
int dist[MX];
bool vis[MX];

void solve(int node) {
    queue<int> q;
    q.push(node);
    
    while(!q.empty()) {
        int cur = q.front(); q.pop();
        for (auto nxt : adj[cur]) {
            if (vis[nxt]) continue;
            dist[nxt] = dist[cur] + 1;
            vis[nxt] = true;
            q.push(nxt);
        }
    }
}

int solution(int n, vector<vector<int>> edge) {
    int answer = 0;
    
    for (auto v : edge) {
        int node1 = v[0];
        int node2 = v[1];
        
        adj[node1].push_back(node2);
        adj[node2].push_back(node1);
    }
    
    vis[1] = true;
    solve(1);
    
    sort(dist, dist + MX, greater<int>());
    
    int mx = dist[0];
    for (int i = 0; i <= n; i++) {
        if (mx == dist[i]) answer++;
        else {
            break;
        }
    }
    
    return answer;
}