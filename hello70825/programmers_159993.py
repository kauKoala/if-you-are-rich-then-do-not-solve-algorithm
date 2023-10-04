'''
문은 레버를 당겨서만 열 수 있음
출발 -> 레버 -> 문
'''
from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def solution(maps):
    n, m = len(maps), len(maps[0])
    sx, sy = -1, -1
    lx, ly = -1, -1
    ex, ey = -1, -1

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S': sx, sy = i, j
            if maps[i][j] == 'L': lx, ly = i, j
            if maps[i][j] == 'E': ex, ey = i, j

    q = deque([[sx, sy]])
    visited = [[-1] * m for _ in range(n)]
    visited[sx][sy] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])

    answer = visited[lx][ly]
    if visited[lx][ly] == -1:
        return -1

    visited = [[-1] * m for _ in range(n)]
    visited[lx][ly] = 0
    q = deque([[lx, ly]])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X' and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])

    if visited[ex][ey] == -1:
        return -1
    answer += visited[ex][ey]

    return answer