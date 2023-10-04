#include <bits/stdc++.h>
using namespace std;

vector<int> v;
int t, ans;

void solve(int cnt, int sum) {
    if (cnt == (int) v.size()) {
        if (sum == t) {
            ans += 1;
            return;
        } else {
            return;
        }
    }
    solve(cnt + 1, sum + v[cnt]);
    solve(cnt + 1, sum - v[cnt]);
}

int solution(vector<int> numbers, int target) {
    v = numbers;
    t = target;
    
    solve(0, 0);
    
    return ans;
}