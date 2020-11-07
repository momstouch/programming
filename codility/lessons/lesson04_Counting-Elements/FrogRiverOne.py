# https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/

def solution(X, A):
    cnt = {}
    for i, a in enumerate(A):
        if a <= X:
            cnt[a] = 0
        if len(cnt) == X:
            return i
    
    return -1


cases = [
        ([1,3,1,4,2,3,5,4], 5, 6),
        ]
for x, a, gt in cases:
    assert solution(x, a) == gt
