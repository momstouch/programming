# https://programmers.co.kr/learn/courses/30/lessons/17678

from collections import deque

def solution(n, t, m, timetable):
    minutes = [int(x.split(":")[0]) * 60 + int(x.split(":")[1]) for x in timetable]
    minutes.sort(reverse = False)
    que = deque(minutes)
    n_bus = 0
    last = []

    start = 9 * 60 # 540
    while n_bus < n and que:
        last = []
        person = 0
        while que and que[0] <= start and person < m:
            person += 1
            last.append(que.popleft())
        start += t
        n_bus += 1

    answer = start - t
    if len(last) >= m:
        if last[0] == last[-1]:
            answer = last[0] - 1
        else:
            answer = last[-1] - 1

    return "%02d:%02d" % (answer // 60, answer % 60)

cases = [
        (1, 1, 5, ["08:00", "08:01", "08:02", "08:03"], "09:00"),
        (2, 10, 2, ["09:10", "09:09", "08:00"], "09:09"),
        (2, 1, 2, ["09:00", "09:00", "09:00", "09:00"], "08:59"),
        (1, 1, 5, ["00:01", "00:01", "00:01", "00:01", "00:01"], "00:00"),
        (1, 1, 1, ["23:59"], "09:00"),
        (10, 60, 45, [
            "23:59","23:59", "23:59", "23:59",
            "23:59", "23:59", "23:59", "23:59",
            "23:59", "23:59", "23:59", "23:59",
            "23:59", "23:59", "23:59", "23:59"], "18:00"),
        ]
for n, t, m, timetable, answer in cases:
    #solution(n,t,m,timetable)
    assert solution(n, t, m, timetable) == answer
