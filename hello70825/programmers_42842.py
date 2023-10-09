def solution(brown, yellow):
    val = brown + yellow
    for i in range(1, val):
        if val % i == 0:
            a, b = i, val // i
            if (a - 2) * (b - 2) == yellow:
                answer = [max(a, b), min(a, b)]
                break
    return answer