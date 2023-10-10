#include <bits/stdc++.h>
using namespace std;

string num_to_binary(long long num) {
    string result = "";
    while (num > 0) {
        result += '0' +(num % 2);
        num /= 2;
    }
    reverse(result.begin(), result.end());
    return result;
}

bool check(string tree, int st, int en) {
    if (tree.size() == 1) return true;
    
    int mid = (st + en) / 2;
    int left = (st + mid - 1) / 2;
    int right = (mid + 1 + en) / 2;
    
    if (tree[mid] == '0' && (tree[left] == '1' || tree[right] == '1')) return false;
    
    string left_tree = "";
    string right_tree = "";
    for (int i = 0; i < mid; i++) left_tree += tree[i];
    for (int i = mid + 1; i < tree.size(); i++) right_tree += tree[i];
    
    return check(left_tree, 0, left_tree.size() - 1) && check(right_tree, 0, right_tree.size() - 1);
}

bool divide(int length) {
    while (length > 1) {
        if (length % 2 == 1) return false;
        length /= 2;
    }
    return true;
}

bool solve(string binary) {
    // 포화 이진트리 만들기
    while(!divide(binary.size() + 1)) {
        binary = "0" + binary;
    }
    // 하나의 이진트리로 해당 수를 표현할 수 있는지 체크
    if (check(binary, 0, binary.size() - 1)) return true;
    return false;
}


vector<int> solution(vector<long long> numbers) {
    vector<int> answer;
    for (auto num : numbers) {
        string binary = num_to_binary(num);
        if (solve(binary)) answer.push_back(1);
        else answer.push_back(0);
    }
    
    return answer;
}