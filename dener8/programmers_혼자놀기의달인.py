'''
카드 100장: 1~100 적혀 있음

| 열어야 하는 상자가 이미 열려있을 때까지 반복

temp에 요소를 담다가, visited가 True인 부분을 만나면 멈추고 answer_list에 temp 넣기
len(cards)만큼 전부 돌았을 때 (visited 확인하면서) answer_list를 확인하여 가장 길이가 긴 2개의 len(temp)를 곱하면 됨!

=> 원본을 temp에 담지 않고 cnt로만 가져가는 게 효율적일 것 같아서 cnt 사용.

'''

def go(num, cnt, cards, visited):
    if visited[num - 1]:
        return cnt
    visited[num - 1] = True
    return go(cards[num - 1], cnt + 1, cards, visited)


def solution(cards):
    answer = 0
    answer_list = []
    visited = [False] * len(cards)

    for i in range(len(cards)):
        if not visited[i]:
            visited[i] = True
            answer_list.append(go(cards[i], 1, cards, visited))

    answer_list = sorted(answer_list, reverse=True)
    if len(answer_list) == 1:
        return 0
    return answer_list[0] * answer_list[1]
