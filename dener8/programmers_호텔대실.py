'''
1. 시작 시간 기준으로 정렬하고,
2. 앞 선 것부터 채워넣는 방식으로 진행
-> 그냥 시간 배열을 통째로 리스트에 넣고, 그 리스트를 매 반복마다 순회하면서 더 append 할 지 말 지 정하면 됨
'''

def solution(book_time):
    room = []
    for time in book_time:
        time[0] = int(time[0].split(":")[0]) * 60 + int(time[0].split(":")[1])
        time[1] = int(time[1].split(":")[0]) * 60 + int(time[1].split(":")[1])
    book_time = sorted(book_time, key=lambda x: [x[0]])

    for i in range(len(book_time)):
        if not room:
            room.append(book_time[i])
            continue
        room = sorted(room, key=lambda x: [x[1]])  # 빨리 끝나는 방 순서로 정렬

        # 하나도 없으면, 방 하나 더 열어야 함
        able = False
        for j in range(len(room)):
            if room[j][1] + 10 <= book_time[i][0]:
                able = True
                room[j] = book_time[i]
                break
        if not able:
            room.append(book_time[i])

    answer = len(room)
    return answer