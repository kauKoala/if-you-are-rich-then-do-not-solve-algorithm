'''
범위가 넓어지면 점화식으로 해결할 것
dp[i][j] = max(dp[i-1][:j], dp[i-1][j+1:]) + li[i][j]
'''


def solution(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] += max(land[i - 1][:j] + land[i - 1][j + 1:])

    answer = max(land[-1])
    return answer
