# https://programmers.co.kr/learn/courses/30/lessons/17681

def solution(n, arr1, arr2):
    answer = []

    int2bin = "{0:0%db}" % (n)

    for x in list(map(lambda a: a[0] | a[1], zip(arr1, arr2))):
        xbin = int2bin.format(x).replace('1', '#').replace('0', ' ')
        answer.append(xbin)

    return answer


cases = [
        (
            5,
            [9,20,28,18,11],
            [30,1,21,17,28],
            ["#####","# # #", "### #", "#  ##", "#####"]
            ),
        (
            6,
            [46, 33, 33 ,22, 31, 50],
            [27 ,56, 19, 14, 14, 10],
            ["######", "###  #", "##  ##", " #### ", " #####", "### # "]
            ),
        ]
for n, arr1, arr2, ans in cases:
    assert solution(n, arr1, arr2) == ans
