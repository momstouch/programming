# https://programmers.co.kr/learn/courses/30/lessons/42860

def next_pos_and_weight(i, name):
    j = i
    while j < len(name) and name[j] == 'A':
        j += 1
    jcnt = j - i
    kcnt = 0

    k = i
    while len(name) + k if k < 0 else k != i + 1:
        if name[len(name) + k if k < 0 else k] != 'A':
            break
        kcnt += 1
        k -= 1

    if j >= len(name) or (name[j] == 'A' and name[k] == 'A'):
        return None, None
    if jcnt <= kcnt:
        return j, jcnt
    else:
        return k, kcnt


def solution(name):
    i = 0 # current pos over name
    lname = list(name)
    ans = 0

    while True:
        nexti, step = next_pos_and_weight(i, lname)
        if nexti is None:
            break

        #print(nexti, step, lname[nexti])
        ans += min(ord(lname[nexti]) - ord('A'), ord('Z') - ord(lname[nexti]) + 1)
        ans += step

        lname[nexti] = 'A'
        i = nexti

    #print(ans)
    return ans


cases = [
        ("JEROEN", 56),
        ("JAN", 23),
        ("BABBAABA", 9),
        ("BBBBAABB", 9),
        ]

for name, answer in cases:
    assert solution(name) == answer
