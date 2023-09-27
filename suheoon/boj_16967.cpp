#include <bits/stdc++.h>
using namespace std;

int h, w, x, y;
int a[1001][1001];
int b[1001][1001];
int vis[1001][1001];

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> h >> w >> x >> y;
    for (int i = 0; i < h + x; i++) {
        for (int j = 0; j < w + y; j++) {
            cin >> b[i][j];
        }
    }
    
    // vis 배열 초기화
    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            vis[i][j] += 1;
        }
    }

    if (x > 0 || y > 0) {
        for (int i = x; i < h + x; i++) {
            for (int j = y; j < w + y; j++) {
                vis[i][j] += 1;
            }
        }
    }

    for (int i = 0; i < h + x; i++) {
        for (int j = 0; j < w + y; j++) {
            if (vis[i][j] == 1) {
                if (i > h - 1 || j > w - 1) {
                    a[i - x][j - y] = b[i][j];
                } else {
                    a[i][j] = b[i][j];
                }
            } else if (vis[i][j] == 2) {
                a[i][j] = b[i][j] - a[i - x][j - y];
            }
        }
    }

    for (int i = 0; i < h; i++) {
        for (int j = 0; j < w; j++) {
            cout << a[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}