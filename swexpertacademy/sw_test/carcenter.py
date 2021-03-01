# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

from collections import deque, Counter
import heapq

T = int(input())
for case in range(1, T + 1):
    N, M, K, A, B = list(map(int, input().rstrip().split(' ')))
    A -= 1
    B -= 1
    # N: reception
    # M: repair
    # K: # of customers
    # A: target reception
    # B: target repair
    a = list(map(int, input().rstrip().split(' '))) # reception speed
    b = list(map(int, input().rstrip().split(' '))) # repair speed
    t = list(map(int, input().rstrip().split(' '))) # customer sequence
    #if case != 2:
    #    continue
    customs = {}
    for person, time in enumerate(t):
        customs[time] = customs.get(time, []) + [person]

    time = t[0]
    repair = [(-1,0)] * M
    recep = [(-1,0)] * N # customer id, in time

    recep_q = deque()
    repair_q = deque()
    end_q = []

    target = Counter()

    while len(end_q) != K:
        for i in range(M): # end of repair
            if repair[i][0] != -1 and repair[i][1] + b[i] == time:
                end_q.append(repair[i][0])
                repair[i] = (-1, 0)

        for i in range(M): # into repair
            if repair[i][0] == -1 and repair_q:
                _, man = repair_q[0]
                repair_q.popleft()
                if i == B:
                    target[man + 1] += 1
                repair[i] = (man, time)

        minheap = []
        for i in range(N): # end of reception
            if recep[i][0] != -1 and recep[i][1] + a[i] == time:
                heapq.heappush(minheap, (i, recep[i][0]))
                recep[i] = (-1, 0)

        while minheap:
            repair_q.append(heapq.heappop(minheap))

        # new comer
        men = customs.get(time, [])
        recep_q.extend(men)

        for i in range(N): # into reception
            if recep[i][0] == -1 and recep_q:
                if i == A:
                    target[recep_q[0] + 1] = 1
                recep[i] = (recep_q[0], time)
                recep_q.popleft()

        time += 1

    result = sum([person for person, cnt in target.items() if cnt == 2])
    print("#%d" % (case), -1 if result == 0 else result)
