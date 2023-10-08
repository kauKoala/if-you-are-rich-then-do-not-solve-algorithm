'''
DP
파이썬 탑다운 시간초과 에러 나옴
바텀업으로 풀기
-> 곱하기는 나누기, 더하기는 빼기
'''


def solution(x, y, n):
    MAX = 1000000
    visited = [float('inf')] * 1000001
    visited[y] = 0

    for i in range(y, x - 1, -1):
        if i - n > 0:
            visited[i - n] = min(visited[i - n], visited[i] + 1)
        if i % 2 == 0:
            visited[i // 2] = min(visited[i // 2], visited[i] + 1)
        if i % 3 == 0:
            visited[i // 3] = min(visited[i // 3], visited[i] + 1)

    answer = visited[x]
    if answer == float('inf'): return -1
    return answer