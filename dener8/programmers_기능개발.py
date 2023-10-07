'''
인자 두 개 모두 max_len = 100
ex. 95% -> 99%(1일) -> 104%(2일) : 2일 걸리는 경우

return은 한 묶음으로 배포되는 개수를 쌓으면 됨
'''
from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)

    while len(progresses) != 0 and len(speeds) != 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        sum = 0
        for i in range(len(progresses)):
            if progresses[i] >= 100:
                sum += 1
            else:
                break
        for i in range(sum):
            progresses.popleft()
            speeds.popleft()
        if sum != 0:
            answer.append(sum)

    return answerㅎ