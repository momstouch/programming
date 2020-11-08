# https://app.codility.com/programmers/lessons/6-sorting/triangle/

def solution(A):
    if len(A) < 3:
        return 0
        
    A.sort()
    for i in range(len(A) - 2):
        #if A[i] + A[i + 1] > A[i + 2] and A[i] + A[i + 2] > A[i + 1] and \
        #A[i + 1] + A[i + 2] > A[i]:
        if A[i] + A[i + 1] > A[i + 2]:
            return 1
    return 0


cases = [
        ([10,2,5,1,8,20], 1),
        ([10,50,5,1], 0),
        ]
for a, gt in cases:
    assert solution(a) == gt
