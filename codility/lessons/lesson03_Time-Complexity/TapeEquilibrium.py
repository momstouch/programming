# https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/

def solution(A):
    lsum = A[0]
    rsum = sum(A[1:])
    ans = abs(lsum - rsum)
    for a in A[1:-1]:
        lsum += a
        rsum -= a
        ans = min(ans, abs(lsum - rsum))
        print(ans)

    return ans


cases = [
        #([3,1,2,4,3], 1),
        ([-1000,1000], 2000),
        ]
for a, gt in cases:
    assert solution(a) == gt
