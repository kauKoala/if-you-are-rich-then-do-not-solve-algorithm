#include <bits/stdc++.h>
using namespace std;

int board[102][102];

vector<int> solution(int rows, int columns, vector<vector<int>> queries) {
    vector<int> answer;
    for (int i = 1; i <= rows; i++) {
        for (int j = 1; j <= columns; j++) {
            board[i][j] = (i - 1) * columns + j;
        }
    }
    
    for (auto q : queries) {
        int r1 = q[0]; int c1 = q[1];
        int r2 = q[2]; int c2 = q[3];
        int mini = board[r1][c1];
        int temp = board[r1][c1];
        for (int i = r1; i < r2; i++) {
            board[i][c1] = board[i + 1][c1];
            mini = min(mini, board[i][c1]);
        }
        for (int i = c1; i < c2; i++) {
            board[r2][i] = board[r2][i + 1];
            mini = min(mini, board[r2][i]);
        }
        for (int i = r2; i > r1; i--) {
            board[i][c2] = board[i - 1][c2];
            mini = min(mini, board[i][c2]);
        }
        for (int i = c2; i > c1; i--) {
            board[r1][i] = board[r1][i - 1];
            mini = min(mini, board[r1][i]);
        }
        board[r1][c1 + 1] = temp;
        answer.push_back(mini);
    }
    
    return answer;
}