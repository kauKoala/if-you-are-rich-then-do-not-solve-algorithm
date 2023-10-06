'''
최단거리 => 보통 bfs로 푼다.
min(answer)을 구해야 함
'''
from collections import deque

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def solution(maps):
    answer = 10001
    n, m = len(maps), len(maps[0])
    visited = [[False] * m for _ in range(n)]
    dq = deque()
    dq.append((0, 0))
    answer += 1

    while dq:
        x, y = dq.popleft()

        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                if nx == n - 1 and ny == m - 1:
                    answer = min(answer, maps[nx][ny])
                visited[nx][ny] = True
                dq.append((nx, ny))

    if answer == 10002:
        answer = -1

    return answer