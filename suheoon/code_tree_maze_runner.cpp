#include <bits/stdc++.h>
using namespace std;

// 빈칸, 벽, 출구
// 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형
// r 작은것, c 작은 것
// 모든 참가자들의 이동 거리 합과 출구 좌표 출력
// 미로, 내구도, 사람들

struct Person {
    int x;
    int y;
    bool finish;
};

int n, m, k;
int maze[11][11]; // 0빈칸, 1이상 내구도
vector<Person> v;
pair<int, int> e; // 출구의 좌표
int cnt; // 탈출한 사람 수
int dist; // 총 움직인 거리

int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

void move() {
    for (int i = 0; i < v.size(); i++) {
        if (v[i].finish) continue;
        int cx = v[i].x;
        int cy = v[i].y;
        int dist1 = abs(cx - e.first) + abs(cy - e.second);
        // 움직일 방향 찾기 (상, 하, 좌, 우)
        for (int dir = 0; dir < 4; dir++) {
            int nx = cx + dx[dir];
            int ny = cy + dy[dir];
            int dist2 = abs(nx - e.first) + abs(ny - e.second);
            // 빈칸이고, 출구 방향으로 가까워 지는 방향이면 이동
            if (maze[nx][ny] == 0 && dist2 < dist1) {
                v[i].x = nx;
                v[i].y = ny;
                dist++;
                if (nx == e.first && ny == e.second) {
                    v[i].finish = true;
                    cnt++;
                }
                break;
            }
        }
    }
}

vector<pair<int, int>> find_rectangle() {
    Person mn_p;
    int mn = 987654321;
    for (int i = 0; i < v.size(); i++) {
        if (v[i].finish) continue;
        int tmp = abs(e.first - v[i].x) + abs(e.second - v[i].y);
        if (tmp < mn) {
            mn_p = v[i];
            mn = tmp;
        }
    }

    int length = max(abs(mn_p.x - e.first), abs(mn_p.y - e.second));

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            if (i <= e.first && e.first <= i + length && j <= e.second && e.second <= j + length) {
                int cnt = 0;
                for (int k = 0; k < v.size(); k++) {
                    if (v[k].finish) continue;
                    if (i <= v[k].x && v[k].x <= i + length && j <= v[k].y && v[k].y <= j + length) cnt++; 
                }
                if (cnt) return {{i, j}, {i + length, j + length}};
            }
        }
    }
}

void rotate() {
    vector<pair<int, int>> t = find_rectangle();

    int sx = t[0].first;
    int sy = t[0].second;
    int ex = t[1].first;
    int ey = t[1].second;

    // 회전, 내구도 1 깎기
    int l = ex - sx + 1;

    int temp[11][11] = {0, };
    for (int i = sx; i <= ex; i++) {
        for (int j = sy; j <= ey; j++) {
            temp[j - sy + sx][l - i + sx - 1 + sy] = maze[i][j];
        }
    }

    for (int i = sx; i <= ex; i++) {
        for (int j = sy; j <= ey; j++) {
            if (temp[i][j] > 0) {
                temp[i][j] -= 1;
            }
            maze[i][j] = temp[i][j];
        }
    }

    // 사람 회전
    for (int i = 0; i < v.size(); i++) {
        int cx = v[i].x;
        int cy = v[i].y;
        if (sx <= cx && cx <= ex && sy <= cy && cy <= ey) {
            v[i].x = cy - sy + sx;
            v[i].y = l - cx + sx -1 + sy;
        }
    }

    // 출구 회전
    int i = e.first;
    int j = e.second;
    e.first = j - sy + sx;
    e.second = l - i + sx - 1 + sy;
}

bool is_finish() {
    if (cnt == m) return true;
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // 입력 부분
    cin >> n >> m >> k;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            cin >> maze[i][j];
        }
    }
    for (int i = 0; i < m; i++) {
        int x, y;
        cin >> x >> y;
        v.push_back({x - 1, y - 1, false});
    }
    int x, y;
    cin >> x >> y;
    e.first = x - 1;
    e.second = y - 1;
    
    while(k--) {
        move();
        if (is_finish()) break;
        rotate();
    }
    cout << dist << '\n';
    cout << e.first + 1 << " " << e.second + 1 << '\n';

    return 0;
}