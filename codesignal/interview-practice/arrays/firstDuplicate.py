# https://app.codesignal.com/interview-practice/task/pMvymcahZ8dY4g75q

def firstDuplicate(a):
    b = [False] * (len(a) + 1)
    for el in a:
        if b[el]:
            return el
        b[el] = True

    return -1

cases = [
        [2, 1, 3, 5, 3, 2],     # 3
        [2, 2],                 # 2
        [2, 4, 3, 5, 1],        # -1
        ]
for case in cases:
    print(firstDuplicate(case))
