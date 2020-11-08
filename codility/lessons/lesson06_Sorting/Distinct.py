# https://app.codility.com/programmers/lessons/6-sorting/distinct/

def solution(A):
    ans = {}
    for a in A:
        ans[a] = ans.get(a, 0) + 1
    
    return len(ans)


cases = [
        ([2,1,1,2,3,1], 3),
        ]
for a, gt in cases:
    assert solution(a) == gt
