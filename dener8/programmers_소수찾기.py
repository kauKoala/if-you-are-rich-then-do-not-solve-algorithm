'''
한 자리 숫자
찢어서 소수 만들기

일단 후보군 숫자 리스트부터 만들어야 한다.
1자리 ~ n자리 숫자를 set()으로 거를 것

'''
from itertools import permutations as pm

def solution(numbers):
    li = list(numbers)
    candi = set()
    for i in range(1, len(li) + 1):
        for j in pm(li, i):
            j = list(j)
            num = ""
            for k in range(len(j)):
                num += j[k]
            num = int(num)
            candi.add(num)
    candi = list(candi)

    answer = 0
    for i in candi:
        cnt = 0
        for j in range(1, i + 1):
            if i % j == 0:
                cnt += 1
            if cnt > 2:
                break
        if cnt == 2:
            answer += 1

    return answer