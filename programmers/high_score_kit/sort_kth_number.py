# https://programmers.co.kr/learn/courses/30/lessons/42748

def solution(array, commands):
    return [sorted(array[i-1:j])[k-1] for i,j,k in commands]


cases = [
        ([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]], [5,6,3]),
        ]

for array, commands, answer in cases:
    assert solution(array, commands) == answer
