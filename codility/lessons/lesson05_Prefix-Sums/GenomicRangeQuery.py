# https://app.codility.com/programmers/lessons/5-prefix_sums/genomic_range_query/


def solution(S, P, Q):
    impact = {
            'A': 1, 'C': 2, 'G': 3, 'T': 4
            }
    seq = [{
        'A': 0, 'C': 0, 'G': 0, 'T': 0
        }]

    for s in S:
        seq.append(dict(seq[-1]))
        seq[-1][s] += 1

    ans = [0] * len(P)
    for i, (p, q) in enumerate(zip(P, Q)):
        if p == q:
            ans[i] = impact[S[p]]
            continue

        q += 1
        if seq[p]['A'] != seq[q]['A']:
            ans[i] = impact['A']
        elif seq[p]['C'] != seq[q]['C']:
            ans[i] = impact['C']
        elif seq[p]['G'] != seq[q]['G']:
            ans[i] = impact['G']
        else:
            ans[i] = impact['T']

    return ans


cases = [
        (("CAGCCTA", [2,5,0], [4,5,6]), [2,4,1]),
        (('AC', [0, 0, 1], [0, 1, 1]), [1, 1, 2]),
        ]
for (s, p, q), gt in cases:
    assert solution(s, p, q) == gt
