'''
- 각 곡괭이를 0개 ~ 5개 가지고 있음
- 곡괭이에 따라 캐는 광물의 피로도는 왼쪽 표와 같음
- 각 곡괭이는 광물 5개를 캐면 사용할 수 없음
- 곡괭이 아무거나 하나 선택하여 광물을 캠 - 못사용할 때까지 사용해야함
- 최소의 피로도 구하기

###########
picks = [dia 개수, iron 개수, stone 개수]
minerals = [diamond, iron, stone]

===========
순열? -> 최대 10개 곡괭이, 15P10 = 100억 -> 불가능
백트래킹? -> 3^(minerals / 5) -> 최대 3^10 -> 가능
'''

answer = 25 * 50
score = [[1, 1, 1], [5, 1, 1], [25, 5, 1]]

def solution(picks, minerals):
    global answer

    picks_len = sum(picks)
    minerals_len = len(minerals)

    for i in range(len(minerals)):
        minerals[i] = 0 if minerals[i] == 'diamond' else 1 if minerals[i] == 'iron' else 2

    if picks_len * 5 < minerals_len:
        for i in range(minerals_len - picks_len * 5):
            minerals.pop()

    for i in range(3):
        if picks[i] != 0:
            picks[i] -= 1
            go(1, i, score[i][minerals[0]], picks, minerals)
            picks[i] += 1

    return answer

def go(m_idx, p_idx, n_val, pick, mine):
    global answer

    if m_idx >= len(mine):
        answer = min(answer, n_val)
        return

    if m_idx % 5 != 0:
        go(m_idx + 1, p_idx, n_val + score[p_idx][mine[m_idx]], pick, mine)
    elif sum(pick) == 0:
        go(m_idx + 1, -1, n_val, pick, mine)
    else:
        for i in range(3):
            if pick[i] != 0:
                pick[i] -= 1
                go(m_idx + 1, i, n_val + score[i][mine[m_idx]], pick, mine)
                pick[i] += 1