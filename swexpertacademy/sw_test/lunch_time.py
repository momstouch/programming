# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do

from collections import deque
def permute(graph, people, stairs): # s can be only both 0 and 1
    result = 1e9

    for i in range(2 ** len(people)):
        for idx, j in enumerate(list(('{0:0%db}' % (len(people))).format(i))):
            people[idx][0] = int(j)

        t = 1
        cnt = 0
        wait_q = [deque() for _ in range(2)]
        on_stairs = [deque() for _ in range(2)]
        stime = [graph[i][j] for i, j in stairs]
        while cnt < len(people):
            for i, (stair, s1time, s2time) in enumerate(people):
                dist = s1time if stair == 0 else s2time
                if dist == t:
                    wait_q[stair].append(i)

            for i, on_stair in enumerate(on_stairs):
                escaped = 0
                for j in range(len(on_stair)):
                    p_id, on_time = on_stair[j]
                    if on_time + stime[i] == t:
                        escaped += 1
                for _ in range(escaped):
                    cnt += 1
                    on_stair.popleft()

            for i, q in enumerate(wait_q):
                while q and len(on_stairs[i]) < 3:
                    on_stairs[i].append((q[0], t))
                    q.popleft()

            t += 1

        result = min(result, t - 1)

    return result

def solve(graph, people, stairs):
    t = 1
    cnt = 0
    wait_q = [deque() for _ in range(2)]
    on_stairs = [deque() for _ in range(2)]
    stime = [graph[i][j] for i, j in stairs]
    while cnt < len(people):
        for i, (stair, s1time, s2time) in enumerate(people):
            dist = s1time if stair == 0 else s2time
            if dist == t:
                wait_q[stair].append(i)

        for i, on_stair in enumerate(on_stairs):
            escaped = 0
            for j in range(len(on_stair)):
                p_id, on_time = on_stair[j]
                if on_time + stime[i] == t:
                    escaped += 1
            for _ in range(escaped):
                cnt += 1
                on_stair.popleft()

        for i, q in enumerate(wait_q):
            while q and len(on_stairs[i]) < 3:
                on_stairs[i].append((q[0], t))
                q.popleft()
        t += 1

    return t - 1

def dfs(graph, people, stairs, p_id, answer):
    if p_id == len(people):
        answer[0] = min(answer[0], solve(graph, people, stairs))
        return

    people[p_id][0] = 0
    dfs(graph, people, stairs, p_id + 1, answer)
    people[p_id][0] = 1
    dfs(graph, people, stairs, p_id + 1, answer)

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    room = [list(map(int, input().rstrip().split(' '))) for _ in range(N)]
    people = []
    stairs = []
    for i in range(N):
        for j in range(N):
            if room[i][j] >= 2:
                stairs.append((i,j))
    for i in range(N):
        for j in range(N):
            if room[i][j] == 1:
                people.append([0])
                for si, sj in stairs:
                    people[-1].append(abs(i-si) + abs(j-sj) + 1)

    result = permute(room, people, stairs)
    print("#%d" % (t), result)
    #result = [1e9]
    #dfs(room, people, stairs, 0, result)
    #print("#%d" % (t), result[0])
