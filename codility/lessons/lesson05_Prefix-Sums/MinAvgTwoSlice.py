# https://app.codility.com/programmers/lessons/5-prefix_sums/min_avg_two_slice/

def solution(A):
    minavg = (A[0] + A[1]) / 2
    ans = 0
    for i in range(2, len(A)):
        avg1 = (A[i - 2] + A[i - 1] + A[i]) / 3
        avg2 = (A[i - 1] + A[i]) / 2
        avg, idx = (avg1, i - 2) if avg1 < avg2 else (avg2, i - 1)
        if minavg > avg:
            minavg = avg
            ans = idx 

    return ans


cases = [
        ([4,2,2,5,1,5,8], 1),
        ]
for a, gt in cases:
    assert solution(a) == gt
