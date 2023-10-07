#include <bits/stdc++.h>
using namespace std;

bool vis[1000001];
vector<string> ans;

bool solve(vector<vector<string>> &t, int idx, string airport) {
    if (idx == (int) t.size()) {
        return true;
    }
    
    for (int i = 0; i < (int) t.size(); i++) {
        if (t[i][0] != airport) continue;
        if (vis[i]) continue;
        ans.push_back(t[i][1]);
        vis[i] = true;
        if (solve(t, idx + 1, t[i][1])) {
            return true;
        }
        ans.pop_back();
        vis[i] = false;
    }
    
    return false;
}

vector<string> solution(vector<vector<string>> tickets) {
    sort(tickets.begin(), tickets.end());
    ans.push_back("ICN");
    solve(tickets, 0, "ICN");
    
    return ans;
}