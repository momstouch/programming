# https://programmers.co.kr/learn/courses/30/lessons/43163


def solution_dfs(begin, target, words):
    temp = [begin] + words
    n_char = len(begin)
    graph = {}

    if target not in words:
        return 0

    for i in range(len(temp)):
        for j in range(len(temp)):
            diff_cnt = 0
            for idx in range(n_char):
                if temp[i][idx] != temp[j][idx]:
                    diff_cnt += 1
            if diff_cnt == 1:
                graph[temp[i]] = graph.get(temp[i], []) + [temp[j]]


    def dfs(start, target, graph, n_path, result):
        if start == target:
            result.append(n_path)
        if start in graph and graph[start]:
            child = graph[start]
            for c in child:
                value = graph.pop(start)
                dfs(c, target, graph, n_path + 1, result)
                graph[start] = value

    result = []
    dfs(begin, target, graph, 0, result)

    return 0 if not result else min(result)


def solution_bfs(begin, target, words):
    temp = [begin] + words
    graph = {}

    for i in range(len(temp)):
        graph[temp[i]] = []
        for j in range(len(temp)):
            if sum([x != y for x, y in zip(temp[i], temp[j])]) == 1:
                graph[temp[i]] = graph.get(temp[i], []) + [temp[j]]

    answer = 0
    visited = []
    queue = [begin]
    while queue:
        n = len(queue)

        for q in queue:
            visited.append(q)

        for _ in range(n):
            node = queue.pop(0)

            if node == target:
                return answer

            for child in graph[node]:
                if child not in visited:
                    queue.append(child)

        answer += 1

    return 0


import random
begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]
random.shuffle(words)
# return 4


#begin = "hit"
#target = "hhh"
#words = ["hhh", "hht"]

print(solution_dfs(begin, target, words))
print(solution_bfs(begin, target, words))
