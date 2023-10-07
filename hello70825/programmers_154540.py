from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def solution(maps):
    n = len(maps)
    m = len(maps[0])

    visited = [[0] * m for _ in range(n)]
    answer = []

    for i in range(n):
        for j in range(m):
            if maps[i][j] != 'X' and visited[i][j] == 0:
                val = int(maps[i][j])
                q = deque([[i, j]])
                visited[i][j] = 1

                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 'X' and visited[nx][ny] == 0:
                            visited[nx][ny] = 1
                            q.append([nx, ny])
                            val += int(maps[nx][ny])
                answer.append(val)

    if len(answer) == 0:
        return [-1]
    return sorted(answer)