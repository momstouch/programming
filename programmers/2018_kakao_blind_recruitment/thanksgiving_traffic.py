# https://programmers.co.kr/learn/courses/30/lessons/17676

from collections import deque
import heapq

def time_to_sec(time: str) -> float:
    hh, mm, ss = [float(x) for x in time.split(':')]
    return ss + 60.0 * (hh * 60.0 + mm)

def solution(lines):
    que = deque([])

    timeline = [] # (request or response time, request_id)

    for i, line in enumerate(lines):
        date, time, t = line.split(' ');
        time = int(time_to_sec(time) * 1000.0)
        t = int(float(t[:-1]) * 1000.0 - 1.0)

        heapq.heappush(timeline, (time - t, i, 1))
        heapq.heappush(timeline, (time, i, 0))

    onesec = 999
    insec = set()
    answer = 0
    while timeline:
        if not que or que[0][0] + onesec >= timeline[0][0]:
            begin, i, inout = heapq.heappop(timeline)
            insec.add(i)
            que.append((begin, i, inout))
        else:
            if answer < len(insec):
                answer = len(insec)
            if que:
                if que[0][2] == 0:
                    insec.discard(que[0][1])
                que.popleft()

    if answer < len(insec):
        answer = len(insec)
    return answer

cases = [
        (["2016-09-15 23:59:59.999 0.001s"], 1),
        ([
            "2016-09-15 01:00:04.001 2.0s",
            "2016-09-15 01:00:07.000 2s"
            ], 1),
        ([
            "2016-09-15 01:00:04.002 2.0s",
            "2016-09-15 01:00:07.000 2s"
            ], 2),
        ([
            "2016-09-15 20:59:57.421 0.351s",
            "2016-09-15 20:59:58.233 1.181s",
            "2016-09-15 20:59:58.299 0.8s",
            "2016-09-15 20:59:58.688 1.041s",
            "2016-09-15 20:59:59.591 1.412s",
            "2016-09-15 21:00:00.464 1.466s",
            "2016-09-15 21:00:00.741 1.581s",
            "2016-09-15 21:00:00.748 2.31s",
            "2016-09-15 21:00:00.966 0.381s",
            "2016-09-15 21:00:02.066 2.62s"
            ], 7),
        ]
for lines, answer in cases:
    assert solution(lines) == answer
