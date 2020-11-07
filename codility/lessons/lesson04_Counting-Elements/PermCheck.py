# https://app.codility.com/programmers/lessons/4-counting_elements/perm_check/

def solution(A):
    for i, a in enumerate(sorted(A), 1):
        if i != a:
            return 0
    
    return 1


cases = [
        ([4,1,3,2], 1),
        ([4,1,3], 0),
        ]
for a, gt in cases:
    assert solution(a) == gt
