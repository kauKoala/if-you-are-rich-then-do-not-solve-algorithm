#include <bits/stdc++.h>
using namespace std;

const int MX = 10;

int n, m, k;
int board[MX + 1][MX + 1];
int t[MX + 1][MX + 1];  // 언제 공격했는지
pair<int, int> c[MX + 1][MX + 1];
bool a[MX + 1][MX + 1]; // 이번 턴에 관여한 포탑 여부

pair<int, int> attacker;
pair<int, int> attacked;

int dx[] = {0, 1, 0, -1, -1, -1, 1, 1};
int dy[] = {1, 0, -1, 0, -1, 1, -1, 1};

bool cmp1(pair<int, int> l, pair<int, int> r) {
    int lx = l.first;
    int ly = l.second;
    int rx = r.first;
    int ry = r.second;

    if (t[lx][ly] > t[rx][ry]) {
        return true;
    } else if (t[lx][ly] == t[rx][ry]) {
        if (lx + ly > rx + ry) {
            return true;
        } else if (lx + ly == rx + ry) {
            if (ly > ry) {
                return true;
            }
        }
    }

    return false;
}

bool cmp2(pair<int, int> l, pair<int, int> r) {
    int lx = l.first;
    int ly = l.second;
    int rx = r.first;
    int ry = r.second;
    
    if (t[lx][ly] < t[rx][ry]) {
        return true;
    } else if (t[lx][ly] == t[rx][ry]) {
        if (lx + ly < rx + ry) {
            return true;
        } else if (lx + ly == rx + ry) {
            if (ly < ry) {
                return true;
            }
        }
    }

    return false;
}

void find_attacker() {
    vector<pair<int, int>> tmp;
    int mn = 987654321;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (board[i][j] == 0) {
                continue;
            }
            if (board[i][j] < mn) {
                tmp.clear();
                tmp.push_back({i, j});
                mn = board[i][j];
            } else if (board[i][j] == mn) {
                tmp.push_back({i, j});
            }
        }
    }

    if (tmp.size() >= 2) {
        sort(tmp.begin(), tmp.end(), cmp1);
    }

    attacker = tmp[0];
}

void find_attacked() {
    vector<pair<int, int>> tmp;
    int mx = -1;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (board[i][j] == 0 || (i == attacker.first && j == attacker.second)) {
                continue;
            }
            if (board[i][j] > mx) {
                tmp.clear();
                tmp.push_back({i, j});
                mx = board[i][j];
            } else if (board[i][j] == mx) {
                tmp.push_back({i, j});
            }
        }
    }

    if (tmp.size() >= 2) {
        sort(tmp.begin(), tmp.end(), cmp2);
    }

    attacked = tmp[0];
}

bool lazer_attack() {
    // 좌표 저장 초기화
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            c[i][j] = {0, 0};
        }
    }

    bool vis[MX + 1][MX + 1] = {0, };
    queue<pair<int ,int> > q;

    q.push({attacker.first, attacker.second});
    vis[attacker.first][attacker.second] = true;
    c[attacker.first][attacker.second] = {-1 , -1}; // 시작은 {-1, -1}

    while(!q.empty()) {
        pair<int, int> cur = q.front(); q.pop();
        int cx = cur.first;
        int cy = cur.second;

        if (cx == attacked.first && cy == attacked.second) {
            return true;
        }

        for (int dir = 0; dir < 4; dir++) {
            int nx = cx + dx[dir];
            int ny = cy + dy[dir];
            
            if (nx < 0) {
                nx = n - 1;
            }

            if (nx >= n) {
                nx = 0;
            }

            if (ny < 0) {
                ny = m - 1;
            }

            if (ny >= n) {
                ny = 0;
            }

            if (board[nx][ny] == 0 || vis[nx][ny]) {
                continue;
            }

            q.push({nx, ny});
            vis[nx][ny] = true;
            c[nx][ny] = {cx, cy};
        }
    }

    return false;
}

void shell_attack() {
    int damage = board[attacker.first][attacker.second];

    board[attacked.first][attacked.second] -= damage;
    if (board[attacked.first][attacked.second] < 0) {
        board[attacked.first][attacked.second] = 0;
    }

    for (int dir = 0; dir < 8; dir++) {
        int nx = attacked.first + dx[dir];
        int ny = attacked.second + dy[dir];

        if (nx < 0) {
            nx = n - 1;
        }

        if (nx >= n) {
            nx = 0;
        }

        if (ny < 0) {
            ny = m - 1;
        }

        if (ny >= m) {
            ny = 0;
        }

        // 공격자는 영향을 받지 않는다
        if (nx == attacker.first && ny == attacker.second) {
            continue;
        }

        board[nx][ny] -= (damage / 2);
        a[nx][ny] = true;
    }
}

void attack() {
    if (!lazer_attack()) {
        shell_attack();
    } else {
        // 레이저 공격
        int damage = board[attacker.first][attacker.second];
        board[attacked.first][attacked.second] -= damage;
        a[attacked.first][attacked.second] = true;
        if (board[attacked.first][attacked.second] < 0) {
            board[attacked.first][attacked.second] = 0;
        }

        int cx = attacked.first;
        int cy = attacked.second;

        while(true) {
            int px = c[cx][cy].first;
            int py = c[cx][cy].second;

            if (px == attacker.first && py == attacker.second) {
                break;
            }

            board[px][py] -= (damage / 2);
            a[px][py] = true;
            if (board[px][py] < 0) {
                board[px][py] = 0;
            }

            cx = px;
            cy = py;          
        }
    }
}

void maintain_turret() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (!a[i][j] && board[i][j] != 0) {
                board[i][j] += 1;
            }
        }
    }
}

void print_answer() {
    int ans = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            ans = max(ans, board[i][j]);
        }
    }

    cout << ans;
}

void print_turret() {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cout << board[i][j] << " ";
        }
        cout << '\n';
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    cin >> n >> m >> k;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> board[i][j];
        }
    }
    
    for (int time = 1; time <= k; time++) {
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                a[i][j] = false;
            }
        }
        find_attacker();
        board[attacker.first][attacker.second] += (n + m); // 공격자 공격력 증가
        t[attacker.first][attacker.second] = time; // 공격시간 최신화
        a[attacker.first][attacker.second] = true; // 공격자 공격에 관여
        find_attacked();
        attack();
        maintain_turret();
    }
    print_answer();

    return 0;
}