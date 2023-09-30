#include <bits/stdc++.h>
using namespace std;

const int MX = 1000000;

int n;
int a[MX + 1];
int b, c;

// 총감독관 오직 1명, B명 감시 가능
// 부감독관 여러명 가능, C명 감시 가능

int main(void) {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }
    cin >> b >> c;

    long long ans = 0;

    for (int i = 0; i < n; i++) {
        if (a[i] <= b) {
            ans += 1;
            continue;
        }
        if (a[i] - b <= c) {
            ans += 2;
            continue;
        }
        int tmp = (a[i] - b) % c == 0 ? (a[i] - b) / c : (a[i] - b) / c + 1;
        ans += (tmp + 1);
    }

    cout << ans;

    return 0;
}