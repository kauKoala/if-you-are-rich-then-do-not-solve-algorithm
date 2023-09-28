'''
targets: 모든 미사일
1 <= len(targets) <= 500_000

0. 일단 첫 번째 점 기준으로 정렬
1. 끝나는 점 바로 앞에서 쏘기

*** 요격을 끝 점 기준으로 삼아야 할 듯? 4 ~ 5 범위의 것도 요격하려면 4.9999.. 에서 쏴야 함

'''

def solution(targets):
    targets = sorted(targets, key=lambda x: x[1])
    endpoint = targets[0][1]
    answer = 1
    for i in range(len(targets)):
        if targets[i][0] < endpoint <= targets[i][1]:
            continue
        endpoint = targets[i][1]
        answer += 1

    return answer


'''
처음엔 visited[][]가 필요하다고 생각했지만, 오히려 visited를 사용하면 2중 for문을 돌아야 함.
'''