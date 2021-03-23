# https://programmers.co.kr/learn/courses/30/lessons/43164

from collections import deque

def all_used(used: dict) -> bool:
    for v in used.values():
        if len(v) > sum(v):
            return False
    return True

def dfs(graph: dict, city: str, sequence, used: dict, answer):
    if all_used(used):
        answer[0] = list(sequence)
        return

    if not city in graph:
        return

    for i, city_to in enumerate(graph[city]):
        if not used[city][i]:
            used[city][i] = True
            sequence.append(city_to)

            dfs(graph, city_to, sequence, used, answer)

            if not answer[0]:
                sequence.pop()
                used[city][i] = False
            else:
                return

def solution(tickets):
    dic = {}
    used = {}
    for f, t in tickets:
        dic[f] = dic.get(f, []) + [t]
    for key in dic.keys():
        dic[key].sort(reverse = False)
        used[key] = [False] * len(dic[key])

    seq = deque(["ICN"])
    ans = [[]]
    dfs(dic, "ICN", seq, used, ans)

    return ans[0]


def solution2(tickets):
    graph = {}
    for t in tickets:
        graph[t[0]] = graph.get(t[0], []) + [t[1]]
    for g in graph:
        graph[g].sort(reverse = True)

    stack = ["ICN"]
    path = []

    while stack:
        top = stack[-1]

        if not top in graph or not graph[top]:
            path.append(stack.pop())
        else:
            stack.append(graph[top].pop())

    return path[::-1]


cases = [
        ([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]],
            ["ICN", "JFK", "HND", "IAD"]),
        ([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]],
            ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"])
        ]
for tickets, answer in cases:
    assert solution2(tickets) == answer
