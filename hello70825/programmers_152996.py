'''
weights에서 중복된 몸무게는 따로 구함
나머지는 x2, x3, x4으로 설정
그러면 중복된 몸무게는 나중에 개수 따로 구하기 (중복된걸 같이 구하면 중복된 경우를 더함)

완전탐색: O(N^2)로 각각 x2, x3, x4로 찾아봄 (N = 100,000이라 불가)
'''

def solution(weights):
    answer = 0
    value = [0] * (1001)
    all_weight = [0] * (4001)

    for w in weights:
        value[w] += 1

    for i in range(1001):
        if value[i]:
            answer += (all_weight[i * 2] + all_weight[i * 3] + all_weight[i * 4]) * value[i]
            all_weight[i * 2] += value[i]
            all_weight[i * 3] += value[i]
            all_weight[i * 4] += value[i]

    for i in range(len(value)):
        if value[i] > 0:
            x = value[i]
            answer += x * (x - 1) // 2

    return answer

'''
[100, 100, 100, 200, 200, 200, 300, 300, 300, 400, 400, 400]
(100 * 4, 200 * 2) -> 9개
(200 * 3, 300 * 2) -> 9개
(200 * 4, 400 * 2) -> 9개
(300 * 4, 400 * 3) -> 9개
중복값 = 3 * 4 = 12개
36 + 12 = 48개
'''