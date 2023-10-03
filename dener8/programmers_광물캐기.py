'''
특이사항)
    각 곡괭이는 종류에 상관없이 광물 5개를 캔 후에는 더 이상 사용할 수 없습니다.
    한 번 사용하기 시작한 곡괭이는 사용할 수 없을 때까지 사용합니다.
    광물은 주어진 순서대로만 캘 수 있습니다. ***


picks: 곡괭이 [dia, iron, stone]
minerals:
return: 최소 피로도

'''

'''
완전한 그리디 같지만, 1개가 아닌 5개 단위로 가져가야 손해가 적을 듯!
ex. [d, i] => [d, i, i, i, i, d, d, d, d, i]; d가 먼저 나왔다고 해서 d 곡괭이를 먼저 쓰면 안되고, 뒤를 생각해서 i를 먼저 써야함

1.
 1-1. minerals가 더 많은 경우: len(picks) * 5까지만 하고 나머지는 버리기
 1-2. picks가 더 많은 경우: 그냥 그대로

.. 그냥 완전 탐색으로 해도 되겠는데??

'''
import math

def solution(picks, minerals):
    answer = 0
    cnt_list = []
    for i in range(min(sum(picks), math.ceil(len(minerals) / 5))):
        part = minerals[i * 5: i * 5 + 5]
        cnt = [0, 0, 0]
        for j in range(len(part)):
            if part[j] == 'diamond':
                cnt[0] += 1
            elif part[j] == 'iron':
                cnt[1] += 1
            else:
                cnt[2] += 1
        cnt_list.append(cnt)
    cnt_list = sorted(cnt_list, key=lambda x: [-x[0], -x[1], -x[2]])

    for i in range(len(cnt_list)):
        if picks[0]:
            answer += cnt_list[i][0] + cnt_list[i][1] + cnt_list[i][2]
            picks[0] -= 1

        elif picks[1]:
            answer += cnt_list[i][0] * 5 + cnt_list[i][1] + cnt_list[i][2]
            picks[1] -= 1

        else:
            answer += cnt_list[i][0] * 25 + cnt_list[i][1] * 5 + cnt_list[i][2]
            picks[2] -= 1

    return answer