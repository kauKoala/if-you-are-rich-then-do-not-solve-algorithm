'''
scoville: 모든 음식의 스코빌 지수를 담은 리스트[]
len(scoville) = 1_000_000

K: 원하는 스코빌 지수
max(K) 1_000_000_000

일단 최소치 두 개를 계산하기 위해서는,
정렬된 리스트를 가지고 있어야 한다.
=> 처음에만 sorting하고 그 후에는 heap으로 관리하면 효율적일 듯

"모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는
-1
을 return 합니다."

'''

from heapq import heappop, heappush

def solution(scoville, K):
    cnt = 0
    scoville = sorted(scoville)

    while True:
        first = heappop(scoville)

        if first >= K:
            break
        cnt += 1

        if len(scoville) == 0:
            return -1

        second = heappop(scoville)

        new = first + (second * 2)
        heappush(scoville, new)

    return cnt
