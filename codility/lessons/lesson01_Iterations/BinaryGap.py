# https://app.codility.com/c/run/trainingJ6G2EN-QJK/

def solution(N):
    b = bin(N).split('b')[-1]
    return max([len(x) for x in b.split('1')[1: -1]] + [0])

cases = [
        1041,       # 5
        32,         # 0
        ]
for N in cases:
    print(solution(N))
