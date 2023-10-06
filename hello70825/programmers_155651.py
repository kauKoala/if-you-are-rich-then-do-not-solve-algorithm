'''
24 * 60 = 1440분
최대 1000 이므로 O(1,440,000)
'''

from heapq import *

def solution(book_time):
    book = []
    for i in range(len(book_time)):
        start, end = book_time[i]
        s_hour, s_minute = map(int, start.split(':'))
        e_hour, e_minute = map(int, end.split(':'))
        book.append([s_hour * 60 + s_minute, e_hour * 60 + e_minute + 9])
    answer = 0
    for i in range(0, 1440):
        val = 0
        for s, e in book:
            if s <= i <= e:
                val += 1
        answer = max(answer, val)
    return answer