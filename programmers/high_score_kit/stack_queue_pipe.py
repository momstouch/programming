# https://programmers.co.kr/learn/courses/30/lessons/42585


def solution(arrangement):
    cur_pipe = 0
    total = 0

    for i, a in enumerate(arrangement):
        if a == '(':
            if arrangement[i - 1] == a:
                cur_pipe += 1
        else:
            if arrangement[i - 1] == '(': # laser
                total += cur_pipe
            else: # end of pipe
                total += 1
                cur_pipe -= 1

    return total



cases = [
        "()(((()())(())()))(())",   # 17
        ]
for c in cases:
    print(solution(c))
