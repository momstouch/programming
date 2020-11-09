# https://app.codility.com/programmers/lessons/8-leader/equi_leader/

from collections import Counter

def solution(A):
    front = Counter(A[:1])
    flen = 1
    mostk = A[0]
    mostn = 1
    
    back = Counter(A[1:])
    blen = len(A) - 1
    
    ans = 1 if back[A[0]] > blen // 2 else 0

    for a in A[1:]:
        front[a] = front.get(a, 0) + 1
        if front[a] > mostn:
            mostn = front[a]
            mostk = a

        back[a] -= 1
        if back[a] == 0:
            del back[a]
        
        flen += 1
        blen -= 1

        if mostn > flen // 2:
            bnum = back[mostk]
            if bnum > blen // 2:
                ans += 1

    return ans


cases = [
        ([4, 4, 2, 5, 3, 4, 4, 4], 3),
        #([4,3,4,4,4,2], 2),
        ]
for a, gt in cases:
    assert solution(a) == gt
