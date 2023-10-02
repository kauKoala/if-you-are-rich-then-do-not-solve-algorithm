#include <bits/stdc++.h>
using namespace std;

const int MX = 20;

int n, m, k;
int Round;
int board[MX + 1][MX + 1];
int cnt[MX + 1][MX + 1];  // 팀 구분
bool vis[MX + 1][MX + 1];
int ans;

vector<pair<int, int> > v[6];

int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};

void dfs(int x, int y, int team_no) {
    for (int dir = 0; dir < 4; dir++) {
        int nx = x + dx[dir];
        int ny = y + dy[dir];
        if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
        if (vis[nx][ny]) continue;
        if (board[nx][ny] == 0) continue;

        vis[nx][ny] = true;
        cnt[nx][ny] = team_no;
        dfs(nx, ny, team_no);
    }
}

void move() {
    bool trace[MX + 1][MX + 1] = {0, };

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < (int) v[i].size(); j++) {
            int cx = v[i][j].first;
            int cy = v[i][j].second;

            for (int dir = 0; dir < 4; dir++) {
                int nx = cx + dx[dir];
                int ny = cy + dy[dir];

                if (nx < 0 || nx >= n || ny < 0 || ny >= n) continue;
                if (board[nx][ny] == 0 || board[nx][ny] != 4) continue;
                if (board[cx][cy] != 1 && !trace[nx][ny]) continue;
                
                // 이동
                swap(board[cx][cy], board[nx][ny]);
                trace[cx][cy] = true;
                v[i][j].first = nx;
                v[i][j].second = ny;
            }
        }
    }
}

void get_point(int x, int y) {
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < (int) v[i].size(); j++) {
            pair<int, int> idx = v[i][j];
            if (idx.first == x && idx.second == y) {
                ans += ((j + 1) * (j + 1));
                reverse(v[i].begin(), v[i].end());
                swap(board[v[i][0].first][v[i][0].second],
                    board[v[i][v[i].size() - 1].first][v[i][v[i].size() - 1].second]
                );
                return;
            }
        }
    }
}

void throw_ball() {
    int r = (Round - 1) % n;

    if (Round <= n) {
        for (int i = 0; i < n; i++) {
            if (1 <= board[r][i] && board[r][i] <= 3) {
                get_point(r, i);
                break;
            }
        }
    } else if (Round <= 2 * n) {
        for (int i = n - 1; i >= 0; i--) {
            if (1 <= board[i][r] && board[i][r] <= 3) {
                get_point(i, r);
                break;
            }
        }
    } else if (Round <= 3 * n) {
        for (int i = n - 1; i >= 0; i--) {
            if (1 <= board[n - 1 - r][i] && board[n - 1 - r][i] <= 3) {
                get_point(n - 1 - r, i);
                break;
            }
        }
    } else {
        for (int i = 0; i < n; i++) {
            if (1 <= board[i][n - 1 - r] && board[i][n - 1 - r] <= 3) {
                get_point(i, n - 1 - r);
                break;
            }
        }
    }
}

bool cmp(pair<int, int> l, pair<int, int> r) {
    return board[l.first][l.second] < board[r.first][r.second];
}

void print_info() {
    cout << "---" << '\n';
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cout << board[i][j] << " ";
        }
        cout << '\n';
    }
    cout << "---" << '\n';
}

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m >> k;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> board[i][j];
        }
    }

    int team_no = 1;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (board[i][j] == 0) continue;
            if (vis[i][j]) continue;
            vis[i][j] = true;
            cnt[i][j] = team_no;
            dfs(i, j, team_no);
            team_no++;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            int idx = cnt[i][j];
            if (idx && (board[i][j] < 4)) {
                v[idx - 1].push_back({i, j});
            }
        }
    }

    // 팀의 좌표 정보에서 head -> tail 순으로 정렬
    for (int i = 0; i < m; i++) {
        sort(v[i].begin(), v[i].end(), cmp);
    }

    while(k--) {
        Round++;
        move();
        throw_ball();
        // print_info();
    }

    cout << ans;

    return 0;
}