'''
k: 현재 피로도
len(dungeons) = 8
return: 탐험할 수 있는 최대 던전 수

피로도 소모가 낮은 곳부터 탐험
 ["최소 필요 피로도", "소모 피로도"]

 소모 피로도가 낮은 것들 중, 최소 필요 피로도가 낮은 것부터 탐색

 완전탐색 할 것 없이 일단 정렬하고 들어가면 되지 않나? -> 안된다!
'''

# from itertools import permutations as pm

# def solution(k, dungeons):
#     answer = -1
#     for part in pm(dungeons, len(dungeons)):
#         part_answer = 0
#         hp = k
#         for i in part: # 2차원 배열 part, [x, y] => i
#             if i[0] <= hp and hp - i[1] >= 0:
#                 hp -= i[1]
#                 part_answer += 1

#             # else:
#             #     break # 탐색 못하는 순간 멈추는 건지 아닌지를 모르겠다.

#         answer = max(answer, part_answer)

#     return answer

# 2. permutations 사용하지 않고 풀기
answer = -1

def go(k, dungeons, cnt, visited):
    global answer
    answer = max(answer, cnt)
    for i in range(len(dungeons)):
        if visited[i] == False and dungeons[i][0] <= k and k - dungeons[i][1] >= 0:
            visited[i] = True
            go(k - dungeons[i][1], dungeons, cnt + 1, visited)
            visited[i] = False

def solution(k, dungeons):
    global answer
    visited = [False] * len(dungeons)
    go(k, dungeons, 0, visited)
    return answer