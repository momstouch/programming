# https://app.codesignal.com/interview-practice/task/uX5iLwhc6L5ckSyNC

def firstNotRepeatingCharacter(s):
    ss = [0] * (ord('z') - ord('a') + 1)
    first_nrc = 0
    for el in s: # this for loop can be replaced with collections.Counter
        idx = ord(el) - ord('a')
        ss[idx] += 1

    for el in s:
        idx = ord(el) - ord('a')
        if ss[idx] == 1:
            return el

    return '_'


def using_index_of_str(s):
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return '_'


def using_dict(s):
    letters = {}
    flag = [False] * (ord('z') - ord('a') + 1)
    for c in s:
        if flag[ord(c) - ord('a')]:
            letters.pop(c, False)
        else:
            letters[c] = True
            flag[ord(c) - ord('a')] = True

    letters['_'] = True
    return next(iter(letters))


cases = [
        "abacbad",          # 'c'
        "abacabaabacaba",   # '_'
        "ngrhhqbhnsipkcoqjyviikvxbxyphsnjpdxkhtadltsuxbfbrkof", # 'g'
        ]
for case in cases:
    print(firstNotRepeatingCharacter(case))
    print(using_index_of_str(case))
    print(using_dict(case))
