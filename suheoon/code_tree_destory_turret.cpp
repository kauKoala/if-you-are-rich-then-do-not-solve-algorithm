#include <bits/stdc++.h>
using namespace std;

const int MX = 10;

int n, m, k;
int turn;
int board[MX + 1][MX + 1];
int t[MX + 1][MX + 1];  // 언제 공격했는지
pair<int, int> c[MX + 1][MX + 1];
bool a[MX + 1][MX + 1];  // 이번 턴에 관여한 포탑 여부
bool vis[MX + 1][MX + 1];

pair<int, int> attacker;
pair<int, int> attacked;

int dx[] = {0, 1, 0, -1, -1, -1, 1, 1};
int dy[] = {1, 0, -1, 0, -1, 1, -1, 1};

bool cmp(pair<int, int> l, pair<int, int> r) {
    int lx = l.first;
    int ly = l.second;
    int rx = r.first;
    int ry = r.second;

    if (board[lx][ly] != board[rx][ry]) return board[lx][ly] < board[rx][ry];
    if (t[lx][ly] != t[rx][ry]) return t[lx][ly] > t[rx][ry];
    if (lx + ly != rx + ry) return lx + ly > rx + ry;
    return ly > ry;
}

void find_attacker() {
    vector<pair<int, int>> tmp;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (board[i][j] == 0) {
                continue;
            }
            tmp.push_back({i, j});
        }
    }

    sort(tmp.begin(), tmp.end(), cmp);
    attacker = tmp[0];

    board[attacker.first][attacker.second] += (n + m);  // 공격자 공격력 증가
    t[attacker.first][attacker.second] = turn;          // 공격시간 최신화
    a[attacker.first][attacker.second] = true;          // 공격자 공격에 관여
}

void find_attacked() {
    vector<pair<int, int> > tmp;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (board[i][j] == 0) {
                continue;
            }
            // 공격자 제외
            if (i == attacker.first && j == attacker.second) {
                continue;
            }
            tmp.push_back({i, j});
        }
    }

    sort(tmp.begin(), tmp.end(), cmp);
    attacked = tmp[tmp.size() - 1];
}

bool lazer_attack() {
    queue<pair<int, int> > q;

    q.push({attacker.first, attacker.second});
    vis[attacker.first][attacker.second] = true;

    while (!q.empty()) {
        pair<int, int> cur = q.front();
        q.pop();
        int cx = cur.first;
        int cy = cur.second;

        if (cx == attacked.first && cy == attacked.second) {
            return true;
        }

        for (int dir = 0; dir < 4; dir++) {
            int nx = (cx + dx[dir] + n) % n;
            int ny = (cy + dy[dir] + m) % m;

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
    a[attacked.first][attacked.second] = true;

    for (int dir = 0; dir < 8; dir++) {
        int nx = (attacked.first + dx[dir] + n) % n;
        int ny = (attacked.second + dy[dir] + m) % m;

        // 공격자는 영향을 받지 않음
        if (nx == attacker.first && ny == attacker.second) {
            continue;
        }

        board[nx][ny] -= (damage / 2);
        if (board[nx][ny] < 0) {
            board[nx][ny] = 0;
        }
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
        if (board[attacked.first][attacked.second] < 0) {
            board[attacked.first][attacked.second] = 0;
        }
        a[attacked.first][attacked.second] = true;

        int cx = c[attacked.first][attacked.second].first;
        int cy = c[attacked.first][attacked.second].second;

        while (true) {
            if (cx == attacker.first && cy == attacker.second) {
                break;
            }
            board[cx][cy] -= (damage / 2);
            if (board[cx][cy] < 0) {
                board[cx][cy] = 0;
            }
            a[cx][cy] = true;

            int nx = c[cx][cy].first;
            int ny = c[cx][cy].second;

            cx = nx;
            cy = ny;
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

void init() {
    turn++;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            a[i][j] = false;
        }
    }

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            vis[i][j] = false;
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

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n >> m >> k;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> board[i][j];
        }
    }

    while (k--) {
        int ans = 0;
        for (int x = 0; x < n; x++) {
            for (int y = 0; y < m; y++) {
                if (board[x][y]) {
                    ans++;
                }
            }
        }
        if (ans <= 1) {
            break;
        }
        init();
        find_attacker();
        find_attacked();
        attack();
        maintain_turret();
    }
    print_answer();

    return 0;
}