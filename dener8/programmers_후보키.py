'''
결국 '조합' 문제

column이 8개 이하이므로, 조합 완전 탐색 다 돌려도 문제 없음

1. 해당 조합을 고른 후 배열에 넣는다.
2. 부분 배열인 경우에는 제외하고 count 한다.

set을 활용해야겠네

~~candi에 넣는 기준은 맨 처음 값 행 기준으로 해야겠다. (2번에서 걸러낼 원본 리스트가 필요함)~~

위에꺼 아니고, 우선 idx 기준으로 가능한 모든 조합을 뽑아내야 함 -> 그 다음에 2번 째 for문으로 (2중 for문) 값을 걸러내야 함
'''

from itertools import combinations as cb


def solution(relation):
    answer = 0
    candi = []
    idx_list = [i for i in range(len(relation[0]))]

    for i in range(1, len(relation[0]) + 1):  # 모든 원소 다 뽑은 건 문제에서 필요 없다고 나와있음 => 이 부분을 착각했네
        for j in cb(idx_list, i):
            # 예를 들어, j == (0, 3, 4)
            j = list(j)
            set_list = []
            flag = True
            for k in range(len(relation)):
                temp = []
                for l in j:
                    temp.append(relation[k][l])
                # print(temp)
                # for l in temp:
                #     if l not in set_list:
                #         set_list.append(l)
                #     else:
                #         flag = False
                if temp not in set_list:
                    set_list.append(temp)
                else:
                    flag = False
            if flag:  # == 겹치는 게 없으면
                candi.append(j)

    flag_list = [True] * len(candi)
    for i in range(len(candi) - 1):
        for j in range(i + 1, len(candi)):
            if set(candi[i]).issubset(set(candi[j])):  # 작은 것이 큰 것의 부분 집합이면, 큰 것을 False 처리
                flag_list[j] = False

    for i in range(len(flag_list)):
        if flag_list[i]:
            answer += 1

    return answer
