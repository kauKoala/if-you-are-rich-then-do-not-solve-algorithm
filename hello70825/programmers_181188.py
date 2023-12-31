'''
미사일을 최소로 사용해서 모든 폭격 미사일을 요격
세계는 2차원 공간으로 이루어짐
A미사일 = x축에 평행한 직선 형태의 모양 (s, e)
B미사일 = y축에 수평한 모양 (s, e)
* 개구간이니 s, e에서 요격할 수 없음

targets의 길이 최대 500,000
(s, e) 범위 최대 100,000,000

방법1) 라인 스위핑 (아무리 많아야 중복되지 않는 원소가 100만개이므로 가능할 듯)
방법2) 정렬 (범위를 좁은 값으로하다가 더이상 불가능하면 미사일 새로 쏘기)
2-1) s 기준으로 오름차순 정렬
[1,4], [3,7], [4,5], [4,8], [5,12], [10,14], [11,13]
(1,4), (3,4), (4,5), (4,5), (5,12), (10,12), (11,12)
2-2) e 기준으로 오름차순 정렬
[1,4], [4,5], [3,7], [4,8], [5,12], [11,13], [10,14]
(1,4), (4,5), (4,5), (4,5), (5,12), (11,12), (11,12)
-> 어느것을 기준으로 해도 상관없음
'''
def solution(targets):
    targets = sorted(targets)
    answer = 1
    now_s, now_e = targets[0]
    for s, e in targets[1::]:
        if now_e <= s:
            answer += 1
            now_s, now_e = s, e
        else:
            now_s = max(now_s, s)
            now_e = min(now_e, e)
    return answer