# https://app.codesignal.com/interview-practice/task/5vXzdE9yzjsoMZ9sk

def get_clique(dic, key, ans):
    if not key in dic:
        return key

    ans.add(key)
    for v in dic.pop(key):
        ret = get_clique(dic, v, ans)
        if ret:
            ans.add(ret)
    
def swapLexOrder(str, pairs):
    dic = {}
    for pair in pairs:
        v1 = pair[0] - 1
        v2 = pair[1] - 1

        dic[v1] = dic.get(v1, []) + [v2]
        dic[v2] = dic.get(v2, []) + [v1]

    cliques = []
    keys = list(dic.keys())
    for k in keys:
        clique = set()
        get_clique(dic, k, clique)
        if clique:
            cliques.append(sorted(clique))

    ans = list(str)
    for cliq in cliques:
        chars = sorted([ans[i] for i in cliq], reverse = True)
        for i, c in zip(cliq, chars):
            ans[i] = c

    return "".join(ans)


cases = [
        ["abdc", [[1, 4], [3, 4]]],     # "dbca"
        ["dznsxamwoj", [[1,2], [3,4], [6,5], [8,10]]], # "zdsnxamwoj"
        ]
for str, pairs in cases:
    print(swapLexOrder(str, pairs))
