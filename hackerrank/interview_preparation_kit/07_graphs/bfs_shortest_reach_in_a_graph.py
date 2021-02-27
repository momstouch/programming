# https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=graphs&h_r=next-challenge&h_v=zen&page=2

from collections import deque

class Graph(object):
    def __init__(self, n):
        self.g = {}
        self.n = n

    def connect(self, x, y):
        self.g[x] = self.g.get(x, []) + [y]
        self.g[y] = self.g.get(y, []) + [x]

    def find_all_distances(self, start):
        dists = []
        for i in range(self.n):
            if i != start:
                dists.append(self.bfs(i, start))

        print(*dists)

    def bfs(self, start, target):
        q = deque([start])
        v = [0] * self.n
        v[start] = 1

        while q:
            i = q.popleft()

            for j in self.g.get(i, []):
                if j == target:
                    return v[i] * 6
                if v[j] == 0:
                    v[j] = v[i] + 1
                    q.append(j)

        return -1

t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)
