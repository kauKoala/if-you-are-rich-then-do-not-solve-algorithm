#include <bits/stdc++.h>
using namespace std;

unordered_set<string> s;

bool solution(vector<string> phone_book) {
    for (auto e : phone_book) {
        s.insert(e);
    }
    
    for (auto e : s) {
        string tmp = "";
        for (int i = 0; i < (int) e.size() - 1; i++) {
            tmp += e[i];
            if (s.find(tmp) != s.end()) {
                return false;
            }
        }
    }
    
    return true;
}