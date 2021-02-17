# https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

import bisect
def freqQuery(queries):
    dic = {}
    freq_dic = {}
    ans = []

    for cmd, v in queries:
        if cmd == 1: # insert
            dic[v] = dic.get(v, 0) + 1
        elif cmd == 2: # delete
            if v in dic:
                if dic[v] == 1:
                    del dic[v]
                else:
                    dic[v] -= 1
        elif cmd == 3: # check frequency
            a = sorted(dic.values())
            i = bisect.bisect_left(a = a, x = v)
            if i == len(dic) or a[i] != v:
                ans.append(0)
            else:
                ans.append(1)

    return ans

from collections import defaultdict
def freqQuery2(queries):
    cnt = dict()
    freqs = defaultdict(set)
    ans = []

    for cmd, value in queries:
        freq = cnt.get(value, 0)

        if cmd == 1:
            cnt[value] = freq + 1
            freqs[freq].discard(value)
            freqs[freq + 1].add(value)
        elif cmd == 2:
            cnt[value] = max(0, freq - 1)
            freqs[freq].discard(value)
            freqs[cnt[value]].add(value)
        elif cmd == 3:
            ans.append(1 if freqs[value] else 0)

    return ans

cases = [
            ([[1,5],[1,6],[3,2],[1,10],[1,10],[1,6],[2,5],[3,2]],
                [0,1]),
            ([[3,4],[2,1003],[1,16],[3,1]], [0,1]),
            ]
for queries, answer in cases:
    assert freqQuery2(queries) == answer
