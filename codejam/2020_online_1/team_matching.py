
# solved by sorted difference values between a and b
def solution(n, k, a, b):
    c = [(i, a[i] - b[i]) for i in range(n)]
    c.sort(key = lambda x: abs(x[1]))

    ans = 0
    # diff stands for the counter indicating which group has
    # more larger value of elements
    diff = sum([1 if x > 0 else -1 for _, x in c])

    for i, x in c:
        if k < abs(diff) and x * diff > 0:
            k += 2
            ans += min(a[i], b[i])
        else:
            ans += max(a[i], b[i])

    return ans


T = int(input())
for _ in range(T):
    n, k = [int(i) for i in input().split(" ")]
    a = [int(i) for i in input().split(" ")]
    b = [int(i) for i in input().split(" ")]
    print(solution(n, k, a, b))
