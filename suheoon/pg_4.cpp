#include <bits/stdc++.h>
using namespace std;

priority_queue<int, vector<int>, greater<int> > pq;

int solution(vector<int> scoville, int K) {
    int ans = 0;
    
    for (int i = 0; i < (int) scoville.size(); i++) {
        pq.push(scoville[i]);
    }
    
    while(true) {
        int t1 = pq.top(); pq.pop();
        if (t1 >= K) break;
        if (pq.empty()) return -1;
        int t2 = pq.top(); pq.pop();
        
        int mix = t1 + (t2 * 2);
        ans++;
        pq.push(mix);
    }
    
    return ans;
}