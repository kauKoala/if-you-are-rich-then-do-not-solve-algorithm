# 1. 그리디: 깔끔한 풀이

# from collections import deque

# def solution(people, limit):
#     answer = 0
#     people = deque(sorted(people, reverse = True))

#     while len(people) > 1:
#         if people[0] + people[-1] <= limit:
#             people.pop()
#         people.popleft()
#         answer += 1

#     if people:
#         answer += 1

#     return answer

# 2. 투 포인터
'''
left = 0
right = list_length - 1
mid = (left + right) // 2

내 기억엔 마지막 정답은 mid가 아닌 right였던 것 같다!

1. while left <= right:
        or
2. while left < right:
=> 1명만 있을 경우에도 while문 안에서 판단해야 하기 때문에 '1' 방법이 맞다

'''

def solution(people, limit):
    answer = 0
    people = sorted(people, reverse=True)

    left = 0
    right = len(people) - 1
    while left <= right:
        mid = (left + right) // 2
        if left == right:
            answer += 1
            break
        elif left < right:
            answer += 1
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                left += 1

    return answer