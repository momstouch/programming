# https://programmers.co.kr/learn/courses/30/lessons/43164?language=python3

def solution(tickets):
    routes = {}

    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse = True)

    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop())

    return path[::-1]


tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
print(solution(tickets))
