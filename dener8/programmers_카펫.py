'''
해당 숫자의 곱 조합을 생각해내면 됨
ex.
24
= 1 * 24
= 2 * 12
= 3 * 8
= 4 * 6

가로 >= 세로 의 구조
갈색 테두리는 반드시 1줄

yellow 기준으로 가능한 곱 조합을 만들고,
(가로 * 2) + (세로 * 2) + 4 == brown 이라면
정답 처리
'''

def solution(brown, yellow):
    answer = []

    for i in range(1, int(yellow ** 0.5 + 1)):
        if yellow % i == 0:  # i == 4
            if (yellow // i) * 2 + i * 2 + 4 == brown:
                answer.append(yellow // i + 2)
                answer.append(i + 2)
                break

    answer = sorted(answer, reverse=True)

    return answer