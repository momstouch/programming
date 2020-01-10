# https://programmers.co.kr/learn/courses/30/lessons/43162


def solution(n, computers):
    network = {}
    for host, clients in enumerate(computers):
        network[host] = network.get(host, []) + \
                [i for i, e in enumerate(clients) if e == 1]

    n_nets = 0
    while network:
        n_nets += 1
        visited = []
        key = list(network.keys())[0]
        queue = [key]

        while queue:
            com = queue.pop(0)
            if com not in visited:
                visited.append(com)
                queue.extend(network[com])

        for v in visited:
            network.pop(v, [])

    return n_nets

n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
# return: 2
print(solution(n, computers))
