'''
시간 복잡도: 2^20 = 1_000_000
결국 2C1을 20번 하는거니까, "조합"이나 마찬가지네
'''
# from itertools import combinations as cb

answer = 0

def dfs(sum, i, numbers, target):
    global answer

    if i == len(numbers) - 1:
        if sum == target:
            answer += 1
        return

    dfs(sum + numbers[i + 1], i + 1, numbers, target)
    dfs(sum - numbers[i + 1], i + 1, numbers, target)

def solution(numbers, target):
    global answer

    dfs(0, -1, numbers, target)

    return answer