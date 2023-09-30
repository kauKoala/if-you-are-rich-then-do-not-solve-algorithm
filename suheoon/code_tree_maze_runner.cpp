#include <bits/stdc++.h>
using namespace std;

struct Person {
    int x;
    int y;
    bool finish;
};

int n, m, k;

int maze[11][11]; // 미로의 내구도
int temp[11][11];
vector<Person> v; // 사람의 정보
pair<int, int> e; // 출구의 좌표
int sx, sy, square_size; // 정사각형 정보
int cnt; // 탈출한 사람 수
int dist; // 총 움직인 거리

// 상, 하, 좌, 우
int dx[] = {-1, 1, 0, 0};
int dy[] = {0, 0, -1, 1};

void move() {
    for (int i = 0; i < v.size(); i++) {
        if (v[i].finish) {
            continue;
        }
        int cx = v[i].x;
        int cy = v[i].y;
        int dist1 = abs(cx - e.first) + abs(cy - e.second);
        // 움직일 방향 찾기
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

void find_square() {
    // 한 명 이상의 참가자와 출구를 포함한 가장 작은 정사각형
    for (int sz = 2; sz <= n; sz++) {
        for (int x = 0; x < n; x++) {
            for (int y = 0; y < n; y++) {
                // 출구가 포함 돼 있는지 확인
                if (!(x <= e.first && e.first < x + sz && y <= e.second && e.second < y + sz)) {
                    continue;
                }
                
                bool flag = false;

                for (int i = 0; i < v.size(); i++) {
                    if (v[i].finish) {
                        continue;
                    }
                    if (x <= v[i].x && v[i].x < x + sz && y <= v[i].y && v[i].y < y + sz) {
                        flag = true;
                    }
                }

                if (flag) {
                    sx = x;
                    sy = y;
                    square_size = sz;
                    return;
                }
            }
        }
    }


}

void rotate() {
    // 미로회전, 내구도 1 감소
    for (int i = sx; i < sx + square_size; i++) {
        for (int j = sy; j < sy + square_size; j++) {
            if (maze[i][j]) {
                maze[i][j]--;
            }
        }
    }

    for (int i = sx; i < sx + square_size; i++) {
        for (int j = sy; j < sy + square_size; j++) {
            int ox = i - sx;
            int oy = j - sy;
            
            int rx = oy;
            int ry = square_size - ox - 1;

            temp[rx + sx][ry + sy] = maze[i][j];
        }
    }

    for (int i = sx; i < sx + square_size; i++) {
        for (int j = sy; j < sy + square_size; j++) {
            maze[i][j] = temp[i][j];
        }
    }

    // 사람 회전
    for (int i = 0; i < v.size(); i++) {
        if (v[i].finish) {
            continue;
        }

        int cx = v[i].x;
        int cy = v[i].y;
        
        if (!(sx <= cx && cx < sx + square_size && sy <= cy && cy < sy + square_size)) {
            continue;
        }

        int ox = cx - sx;
        int oy = cy - sy;

        int rx = oy;
        int ry = square_size - ox - 1;

        v[i].x = rx + sx;
        v[i].y = ry + sy;
    }

    // 출구 회전 (항상 회전)
    int ox = e.first - sx;
    int oy = e.second - sy;

    int rx = oy;
    int ry = square_size - ox - 1;

    e.first = rx + sx;
    e.second = ry + sy;
}

bool is_finish() {
    if (cnt == m) {
        return true;
    }
    return false;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

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

    cin >> e.first >> e.second;
    e.first -= 1;
    e.second -= 1;

    for (int i = 0; i < k; i++) {        
        move();
        if (is_finish()) {
            break;
        }
        find_square();
        rotate();
    }
    cout << dist << '\n';
    cout << e.first + 1 << ' ' << e.second + 1 << '\n';

    return 0;
}