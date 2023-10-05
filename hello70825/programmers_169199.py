'''
끝날때까지 while문 돌리기
while문이 끝나는 조건: 맵을 벗어나거나, 현재 위치가 벽일 때
이후 방문한 곳인지 체크하기
'''

from collections import deque

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


def solution(board):
    n = len(board)
    m = len(board[0])

    sx, sy = -1, -1
    ex, ey = -1, -1
    q = deque()
    visited = [[[-1] * 4 for __ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R': sx, sy = i, j
            if board[i][j] == 'G': ex, ey = i, j

    q.append([sx, sy, 0])
    visited[sx][sy] = [0, 0, 0, 0]

    while q:
        x, y, z = q.popleft()
        for i in range(4):
            nx, ny = x, y
            while 1:
                nx, ny = nx + dx[i], ny + dy[i]
                if not (0 <= nx < n and 0 <= ny < m) or board[nx][ny] == 'D':
                    nx, ny = nx - dx[i], ny - dy[i]
                    break
            if visited[nx][ny][i] == -1:
                visited[nx][ny][i] = visited[x][y][z] + 1
                q.append([nx, ny, i])

    answer = 10000
    for i in range(4):
        if visited[ex][ey][i] != -1:
            answer = min(answer, visited[ex][ey][i])
    if answer == 10000:
        answer = -1

    return answer