from collections import deque
input = __import__('sys').stdin.readline

n, m = map(int, input().split())
s, e = map(int, input().split())

warp = [[] for _ in range(n + 1)]
for i in range(m):
    x, y = map(int, input().split())
    warp[x].append(y)
    warp[y].append(x)

visited = [-1] * (n + 1)
visited[s] = 0
q = deque([s])

while q:
    x = q.popleft()
    for nx in [x-1, x+1]:
        if 1 <= nx <= n and visited[nx] == -1:
            visited[nx] = visited[x] + 1
            q.append(nx)
    for nx in warp[x]:
        if 1 <= nx <= n and visited[nx] == -1:
            visited[nx] = visited[x] + 1
            q.append(nx)

print(visited[e])