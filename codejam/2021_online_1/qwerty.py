from collections import deque

graph = {
        "Q": "WA",
        "W": "QASE",
        "E": "WSDR",
        "R": "EDFT",
        "T": "RFGY",
        "Y": "TGHU",
        "U": "YHJI",
        "I": "UJKO",
        "O": "IKLP",
        "P": "OL",
        "A": "QWSZ",
        "S": "WEADZX",
        "D": "ERFCXS",
        "F": "RTGVCD",
        "G": "TYHBVF",
        "H": "YUJNBG",
        "J": "UIKMNH",
        "K": "IOLMJ",
        "L": "KOP",
        "Z": "ASX",
        "X": "ZSDC",
        "C": "XDFV",
        "V": "CFGB",
        "B": "VGHN",
        "N": "BHJM",
        "M": "NJK"
        }


def get_time(from_ch: str, target_ch: str) -> int:
    q = deque(from_ch)
    visit = {from_ch: 1}

    while q:
        v = q.popleft()

        if v == target_ch:
            return (visit.get(v, 0) - 1) * 2

        for ch in graph[v]:
            if visit.get(ch, 0) == 0:
                visit[ch] = visit[v] + 1
                q.append(ch)

    return -1 # error, will nothing happen

def solution(sequence: str) -> int:
    answer = len(sequence)
    for ch1, ch2 in zip(sequence[:-1], sequence[1:]):
        answer += get_time(ch1, ch2)

    return answer

T = int(input())
for case in range(T):
    seq = input()
    print(solution(seq))
