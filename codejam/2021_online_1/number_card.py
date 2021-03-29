
def solution(seq: list, a: str = "", b: str = "") -> int:
    if not seq:
        if a == "" or b == "":
            return 0
        else:
            return int(a) * int(b)

    return max(solution(seq[1:], a + seq[0], b), solution(seq[1:], a, b + seq[0]))

def solution2(seq: list) -> int:
    a = seq[0]
    b = seq[1]

    for x in seq[2:]:
        if int(a) > int(b):
            b += x
        else:
            a += x

    return int(a) * int(b)

T = int(input())
for case in range(T):
    sequence = sorted(input().strip().replace('6', '9'), reverse = True)
    print(solution2(sequence))
