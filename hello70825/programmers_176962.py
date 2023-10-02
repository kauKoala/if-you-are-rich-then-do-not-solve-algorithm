'''
- 과제를 해야하는 시각이 되면 시작
- 새로운 과제를 시작해야하면, 기존 과제를 멈추고, 새로운 과제 시작
- 과제를 끝냈을 때, 멈춘 과제가 있으면 멈춘 과제를 이어서 진행 (새로운 과제 시간이랑 겹치면 새로운 과제부터)
- 멈춘 과제를 시작하는건 가장 최근에 멈춘 과제부터 → 스택

##################
plan = [name, start, playtime]
start = 00:00 ~ 23:59 (모든 과제 시작 시간은 다름)
playtime = 0 ~ 100
시간순으로 정렬되지 않음

==================

23:59 이후의 내용은 없으므로 모든 과제는 끝낼 수 있음
그래서 stack에 저장한 순서대로 정답에 저장하면 될 듯
hh:mm은 계산하기 어려우므로 분단위로 변경하기
'''


def solution(plans):
    # hh:mm -> 분 단위로 변경
    for i in range(len(plans)):
        hour, minute = map(int, plans[i][1].split(':'))
        plans[i][1] = hour * 60 + minute
        plans[i][2] = int(plans[i][2])

    # 정렬
    plans = sorted(plans, key=lambda x: [x[1]])

    # 과제 저장공간
    stack = []  # 이름, 남은 시간만
    answer = []  # 이름만

    # 과제 진행
    now_time = 0
    for name, start, playtime in plans:
        while stack:
            if now_time == start: break
            old_name, old_playtime = stack.pop()
            left_time = start - now_time
            if old_playtime > left_time:
                stack.append([old_name, old_playtime - left_time])
                now_time = start
                break
            else:
                answer.append(old_name)
                now_time += old_playtime
        now_time = start
        stack.append([name, playtime])

    # 마지막은 정답에 모두 붙이면 끝
    while stack:
        answer.append(stack.pop()[0])

    return answer