#include<bits/stdc++.h>
using namespace std;

int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

bool vis[101][101];
int dist[101][101];

int solution(vector<vector<int> > maps)
{   
    int n = (int) maps.size();
    int m = (int) maps[0].size();
    
    queue<pair<int, int> > q;
    
    q.push({0, 0});
    vis[0][0] = true;
    dist[0][0] = 1;
    
    while(!q.empty()) {
        pair<int, int> cur = q.front(); q.pop();
        int cx = cur.first;
        int cy = cur.second;
        
        for (int dir = 0; dir < 4; dir++) {
            int nx = cx + dx[dir];
            int ny = cy + dy[dir];
            if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;
            if (vis[nx][ny] || maps[nx][ny] == 0) continue;
            
            q.push({nx, ny});
            vis[nx][ny] = true;
            dist[nx][ny] = dist[cx][cy] + 1;
        }
    }
    
    int min = dist[n - 1][m - 1];
    
    if (min) return min;
    return -1;

}