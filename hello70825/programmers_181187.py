'''
방법 1. x = 0, 1`000`000 * 4 브루트포스
x 값에 따라 y값을 자동으로 구할 수 있음
y = root(r^2 - x^2)

문제점1) root()를 신뢰할 수 없음

대안점1) y^2 = r^2 - x^2를 구하고, 특정 완전제곱수 사이에 있는 수인지 확인
ex) y = 27이라면 25와 36 사이에 있으니 y = 5.x로 6부터 점의 개수를 구하면 댐 -> 이진 탐색
이렇게 해서 한 개의 사분면만 구해서 * 4를 해주기
O(NlogN)으로 풀 수 있음

문제점2) 브루트포스 + 이진탐색이 레벨2 문제가 맞나?

대안점2)
print(1234567891234567**2)
print(math.sqrt(1524157878067365654031415677489))
를 해보니 값을 정확하게 반환함
'''

import math

def solution(r1, r2):
    arr = []
    for i in range(1, 1000000 + 1):
        arr.append(i * i)

    answer = (r2 - r1 + 1) * 4

    for x in range(1, r2):
        y2 = int(math.sqrt(r2 * r2 - x * x))
        if r1 * r1 - x * x <= 0 : y1 = 0
        else: y1 = int(math.ceil(math.sqrt(r1 * r1 - x * x)))

        if y1 == 0: y1 += 1
        answer += (y2 - y1 + 1) * 4

    return answer