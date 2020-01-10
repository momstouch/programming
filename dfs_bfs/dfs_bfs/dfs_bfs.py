# https://www.acmicpc.net/problem/1260

N, M, V = list(map(int, input().split(' ')))
# node, edge, start node

graph = {}
for key in range(1, N + 1):
    graph[key] = list()

# make graph
for _ in range(M): # edges
    n1, n2 = list(map(int, input().split(' ')))
    graph[n1].append(n2)
    graph[n2].append(n1)

#for key in graph.keys():
#    graph[key].sort()


def DFS(graph : dict, v : int):
    visited = list() # queue
    need_visit = list() # stack

    need_visit.append(v)

    while need_visit:
        node = need_visit.pop()

        if node not in visited:
            visited.append(node)
            need_visit.extend(reversed(sorted(graph[node])))

    return visited


def BFS(graph : dict, v : int):
    visited = list() # queue
    need_visit = list() # queue

    need_visit.append(v)

    while need_visit:
        node = need_visit.pop(0) # dequeue

        if node not in visited:
            visited.append(node)
            need_visit.extend(sorted(graph[node]))

    return visited


print(' '.join([str(v) for v in DFS(graph, V)]))
print(' '.join([str(v) for v in BFS(graph, V)]))
