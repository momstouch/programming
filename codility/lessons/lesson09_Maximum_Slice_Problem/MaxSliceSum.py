# https://app.codility.com/c/run/trainingGS3J82-6UE/

def solution_mine(A):
    acc = ans = 0
    pos_flag = False

    for a in A:
        if a > 0:
            pos_flag = True

        acc = max(0, acc + a)
        ans = max(acc, ans)

    return ans if pos_flag else max(A)


# Kadane's algorithm
def solution(A):
    acc = ans = A[0]

    for a in A[1: ]:
        acc = max(a, acc + a)
        ans = max(ans, acc)

    return ans


cases = [
        [3, 2, -6, 4, 0],       # 5
        [3, -2, 3],             # 4
        [-1, -2, -3],           # -1
        ]
for A in cases:
    print(solution(A))
