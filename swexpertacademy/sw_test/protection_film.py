# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do?contestProbId=AV5V1SYKAaUDFAWu&categoryId=AV732SG66sEDFAW7&categoryType=BOX

def check(graph):
    flag = True
    for c in list(zip(*graph)):
    #for c in [[sub[k] for sub in graph] for k in range(W)]:
        early_stop = True
        for i in range(0, D - K + 1):
            s = sum(c[i: i + K])
            if s == 0 or s == K:
                early_stop = False
                break
        if early_stop:
            flag = False
            break
    return flag

def dfs(graph, d_idx, cnt, ans):
    if cnt >= ans[0]:
        return
    if d_idx == D or cnt >= K:
        if check(graph):
            ans[0] = cnt
        return 

    dfs(graph, d_idx + 1, cnt, ans)

    if cnt + 1 <= K or cnt + 1 < ans[0]:
        graph[d_idx] = atype
        dfs(graph, d_idx + 1, cnt + 1, ans)

        graph[d_idx] = btype
        dfs(graph, d_idx + 1, cnt + 1, ans)

        graph[d_idx] = origin[d_idx]

T = int(input())
for case in range(1, T + 1):
    D, W, K = list(map(int, input().rstrip().split(' ')))
    film = [list(map(int, input().rstrip().split(' '))) for _ in range(D)]
    origin = []
    for i in range(D):
        origin.append([])
        for j in range(W):
            origin[-1].append(film[i][j])
    #origin = copy.deepcopy(film)

    atype = [0] * W
    btype = [1] * W

    ans = [D + 1]
    if check(film):
        ans[0] = 0
    else:
        dfs(film, 0, 0, ans)

    print("#%d" % (case), ans[0])
