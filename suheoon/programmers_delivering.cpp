#include <bits/stdc++.h>
using namespace std;

#define X first
#define Y second

const int INF = 1e9 + 10;
const int MX = 51;

vector<pair<int, int> > adj[MX];
int d[MX];
priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int,int> > > pq;

int solution(int N, vector<vector<int> > road, int K) {
    for (auto v : road) {
        int a = v[0];
        int b = v[1];
        int c = v[2];
        
        adj[a].push_back({c, b});
        adj[b].push_back({c, a});
    }
    for (int i = 0; i < MX; i++) d[i] = INF;
    
    d[1] = 0;
    pq.push({0, 1});
    while(!pq.empty()) {
        pair<int, int> cur = pq.top(); pq.pop();
        if (d[cur.Y] != cur.X) continue;
        for (auto nxt : adj[cur.Y]) {
            if (d[nxt.Y] <= d[cur.Y] + nxt.X) continue;
            d[nxt.Y] = d[cur.Y] + nxt.X;
            pq.push({d[nxt.Y], nxt.Y});
        }
    }
    
    int ans = 0;
    for (int i = 0; i < MX; i++) {
        if (d[i] <= K) {
            ans++;
        }
    }
    
    return ans;
}