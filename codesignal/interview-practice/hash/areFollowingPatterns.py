# https://app.codesignal.com/interview-practice/task/3PcnSKuRkqzp8F6BN

def areFollowingPatterns(strings, patterns):
    dic = {}
    rev_dic = {}

    for st, pa in zip(strings, patterns):
        paindic = dic.get(st, None)
        stindic = rev_dic.get(pa, None)

        if paindic is None and stindic is None:
            dic[st] = pa
            rev_dic[pa] = st
        elif st != stindic or pa != paindic:
            return False

    return True


def usingSet(strings, patterns):
    return len(set(strings)) == len(set(patterns)) == len(set(zip(strings, patterns)))


cases = [
        [["cat", "dog", "dog"], ["a", "b", "b"]],       # True
        [["cat", "dog", "doggy"], ["a", "b", "b"]],     # False
        [["cat", "dog", "dog"], ["a", "b", "c"]],       # False
        ]
for strings, patterns in cases:
    print(areFollowingPatterns(strings, patterns))
    print(usingSet(strings, patterns))
