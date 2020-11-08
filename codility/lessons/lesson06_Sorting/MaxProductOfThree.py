# https://app.codility.com/programmers/lessons/6-sorting/max_product_of_three/

def solution(A):
    ans = 0
    a = sorted(A, reverse = True)

    ans1 = a[0] * a[1] * a[2]
    ans2 = a[0] * a[-1] * a[-2]

    return max(ans1, ans2)


cases = [
        ([-3,1,2,-2,5,6], 60),
        ]
for a, gt in cases:
    assert solution(a) == gt
